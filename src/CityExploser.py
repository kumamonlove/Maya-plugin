import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore
import math
import cityGeneratorLib as cg
import vShatterLib as sl
import RigidbodyLib as rl
import shockWaveLib as sw

'''
Create a window
'''
class CityGeneratorWidget(QtWidgets.QWidget):
    buildingcount = 0
    def __init__(self, parent=None):
        super(CityGeneratorWidget, self).__init__(parent)
        self.setWindowTitle('City Explosion')
        self.resize(500, 400)
        
        self.create_widgets()
        self.create_layout()
        self.create_connections()
        
    def create_widgets(self):
        self.number_input1 = QtWidgets.QLineEdit()
        self.number_input2 = QtWidgets.QLineEdit()
        self.number_input3 = QtWidgets.QLineEdit()
        self.number_input4 = QtWidgets.QLineEdit()
        self.number_input5 = QtWidgets.QLineEdit()
        
        self.slider_input1 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.label_slider_value = QtWidgets.QLabel()
        self.number_input6 = QtWidgets.QLineEdit()
        self.number_input7 = QtWidgets.QLineEdit()
        self.number_input8 = QtWidgets.QLineEdit()
        self.number_input9 = QtWidgets.QLineEdit()
        self.number_input10 = QtWidgets.QLineEdit()
        self.number_input11 = QtWidgets.QLineEdit()
        
        self.checkbox_option = QtWidgets.QCheckBox('Option')
        
        self.button_apply = QtWidgets.QPushButton('Apply')
        self.button_close = QtWidgets.QPushButton('Close')
        
    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        
        # Create tab widget
        tab_widget = QtWidgets.QTabWidget()
        main_layout.addWidget(tab_widget)
        
        # Add tabs to tab widget
        city_tab = QtWidgets.QWidget()
        explosion_tab = QtWidgets.QWidget()
        wave_tab = QtWidgets.QWidget()
        tab_widget.addTab(city_tab, 'City Generate')
        tab_widget.addTab(explosion_tab, 'Explosion')
        
        # City Generate layout
        city_layout = QtWidgets.QFormLayout(city_tab)
        city_layout.addRow('Building_Width:', self.number_input1)
        city_layout.addRow('Building_Height:', self.number_input2)
        city_layout.addRow('City_Size:', self.number_input3)
        city_layout.addRow('Block_Size:', self.number_input4)
        city_layout.addRow('Street_Width:', self.number_input5)
        city_layout.addRow('Building_Type_Checked:',self.checkbox_option)

        
        # Explosion layout
        explosion_layout = QtWidgets.QFormLayout(explosion_tab)
        slider_layout = QtWidgets.QHBoxLayout()
        slider_layout.addWidget(self.slider_input1)
        slider_layout.addWidget(self.label_slider_value)
        explosion_layout.addRow('Fragments/object:', slider_layout)
        # explosion_layout.addRow('Fragments/object:', self.slider_input1)
        explosion_layout.addRow('Magnitude:', self.number_input6)
        explosion_layout.addRow('Initial_Velocity:', self.number_input7)
        explosion_layout.addRow('KeyFrame_Duration:', self.number_input8)
        explosion_layout.addRow('Wave1_StartTime:', self.number_input9)
        explosion_layout.addRow('Wave1_EndTime:', self.number_input10)
        explosion_layout.addRow('Center_Height:', self.number_input11)

        
        # Add buttons to a horizontal layout
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.button_apply)
        button_layout.addWidget(self.button_close)
        main_layout.addLayout(button_layout)

        # Set slider range and tick position
        self.slider_input1.setRange(2, 8)
        self.slider_input1.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.slider_input1.setTickInterval(1)
        self.slider_input1.valueChanged.connect(self.update_slider_value)
        self.label_slider_value.setText(str(self.slider_input1.value()))
        
    def create_connections(self):
        self.button_apply.clicked.connect(self.apply_changes)
        self.button_close.clicked.connect(self.close)

    def update_slider_value(self, value):
        self.label_slider_value.setText(str(value))
        
    def apply_changes(self):

        building_width = int(self.number_input1.text()) if self.number_input1.text() else 10
        building_height = int(self.number_input2.text()) if self.number_input2.text() else 30
        city_size = int(self.number_input3.text()) if self.number_input3.text() else 200
        building_gap = 8
        block_size = int(self.number_input4.text()) if self.number_input4.text() else 50
        street_width = int(self.number_input5.text()) if self.number_input5.text() else 16
        building_type_checked = self.checkbox_option.isChecked() if self.checkbox_option.isChecked() else False
        # ��ȡ Explosion ѡ��е�����
        fragments_per_object = self.slider_input1.value() if self.slider_input1.value() else 5
        magnitude = float(self.number_input6.text()) if self.number_input6.text() else 1
        initial_velocity = float(self.number_input7.text()) if self.number_input7.text() else 10
        key_frame_duration = float(self.number_input8.text()) if self.number_input8.text() else 400
        wave_start = float(self.number_input9.text()) if self.number_input9.text() else 1
        wave_end = float(self.number_input10.text()) if self.number_input10.text() else 30
        center_height = float(self.number_input11.text()) if self.number_input11.text() else 50
        end_frame = 600
        applyCityGeneration(building_width,building_height,city_size,building_gap,block_size,street_width,building_type_checked,
        fragments_per_object,magnitude,initial_velocity,key_frame_duration,wave_start,wave_end,center_height,end_frame)


'''
A function that performs the main function.
'''
def applyCityGeneration(buildingWidth,
        buildingHeight,
        cityRange,
        buildingGap,
        blockSize,
        streetWidth,
        building_type_checked,
        fragmentsPerObject,
        magnitude,
        initialVelocity,
        keyFrameDuration,
        waveStart,
        waveEnd,
        centerHeight,
        endFrame): 
    
    # speed = CityGeneratorWidget.getSpeed()
    exploserOrigin = [0, 0, 0]
    group_name0 = "Building_"
    group_name1 = "Building_"
    group_name2 = "_chunks_"
    gravity_name = "temGravity"


    buildingcount = cg.cityGene(cityRange, blockSize, streetWidth, buildingGap, buildingHeight, buildingWidth,building_type_checked)


    # selected = cmds.ls(sl=True, transforms=True)
    for i in range(0, buildingcount):
        surfaceMat = sl.surfaceMaterial(group_name0 + str(i+1), 0.2, 0.7, 0.6)
        sl.vShatter(group_name0 + str(i+1), surfaceMat, fragmentsPerObject)


    # 设置重力场
    rl.buildGravityField(gravityFieldName=gravity_name)
    # 遍历场景中建筑并制作动画
    for f in range(0, endFrame):
        for i in range(0,buildingcount):
            tempgroup_name = group_name1+str(i+1)+group_name2
            cmds.select(group_name0 + str(buildingcount+i*fragmentsPerObject+1))
            pos = cmds.xform(query=True, translation=True, worldSpace=True)  
            vector = [pos[0]-exploserOrigin[0],pos[1]-exploserOrigin[1],pos[2]-exploserOrigin[2]]
            r = math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2) 
            normalizevector = [vector[0]/r*0.02*initialVelocity,vector[1]/r*0.02*initialVelocity,vector[2]/r*0.02*initialVelocity]
            print("pos:"+str(pos))
            print(group_name0 + str(buildingcount+i*3+1) + ":" + str(normalizevector))
            r1 = (0.5*f+1)
            r2 = (0.5*f)
            if(r < r1 and r > r2):
                rl.makeRigidBody(groupName=tempgroup_name, 
                            gravityName=gravity_name,
                            keyFrameStart=f,
                            magnitude=magnitude, 
                            attenuation=0.2, 
                            initialVelocity=normalizevector, 
                            velocityRandom=0.02,
                            angleRandom=0.02,
                            selfAngularVelocityRandom=0.05, 
                            keyFrameDuration=keyFrameDuration,
                            keyFrameDurationRandom=0.2)
        

    sw.createWaveScene(waveStart, waveEnd, waveEnd, waveEnd*8, 5, 5, cityRange*0.1, centerHeight * 0.3, 5, 5, cityRange*0.3, centerHeight * 0.6, 0.98, 0,10,15,20)

'''
Display user interface
'''
def show_plugin_window():
    global plugin_window
    try:
        plugin_window.close()
    except:
        pass
    
    plugin_window = CityGeneratorWidget()
    plugin_window.show()


if __name__ == "__main__":
    show_plugin_window()
