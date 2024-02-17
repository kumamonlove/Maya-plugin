EN-README
CityExploser.py - Generate UI and Perform Plug-in Functions
cityGeneratorLib.py - Library for City Buildings Generation
vShatterLib.py - Library for Voronoi Diagram Algorithms
RigidBodyLib.py - Library for Maya Rigid Body Simulation
shockWaveLib.py - Library for Shock Wave Simulation

1. Installation:
   To use the CityExploser Plug-in in Maya, follow these steps:
   - Copy the all python files to the maya scripts folder on your computer(such as "\Documents\maya\2023\zh_CN\scripts").
   - Once the file is placed in the correct path, you can open the script editor and open the "CityExploser.py" in the scripts folder, click run.

2. Functionality:
   CityExploser Plug-in can help you randomly generate a city complexes, and simulate the nuclear explosion process of city building fragmentation and shock wave effects:

   - Adjustment of generated city parameters to realize the effect of random building generation.
   - Use Voronoi Diagram algorithms to achieve building fragmentation.
   - Traverse objects under a group and apply rigid body physics to them.
   - Create a disappearing animation for the objects with adjustable start frame, duration, and randomness.
   - Simulating the diffusion effect of a shock wave。

3. Parameter: 
   This is the parameter list for the citygenerate tab.
   - Building_Width: the size of the building, which is multiplied by a random value when running the script.
   - Building_Height: the height of the building, which is multiplied by a random value when running the script.
   - City_Size: the size of the city, the maximum size of a city.
   - Block_Size: size of the block, the city is divided into blocks and streets are generated around the blocks.
   - Street_Width: width of the street, generates streets with different widths.
   - Building_Type_Checked: if or not to generate more types of buildings, default is no, if checked, 3 different types of buildings will be generated.

   This is the parameter list for the explosion tab.
   - Fragments/object: the number of fragments the building has broken, with a slider the maximum is 8, the minimum is 2
   - Magnitude: Gravity of the gravity field
   - lnitial_Velocity: the velocity of the fragment's rigid body motion.
   - KeyFrame_Duration: the time between the creation and disappearance of each fragment.
   - Wave1_StartTime: Start time of the shock wave. 
   - Wave1_EndTime: The end time of the shock wave.
   - Center_Height: Height of the center of the shockwave.

4. Copyright Statement:
   Author: Siyang Shen, Yunkai Xu,  Xiaohan Yan, Qi Zheng, 
   Version: 3.0
   Date: 23rd July 2023

CN-README
CityExploser.py - 生成用户界面并执行插件功能
cityGeneratorLib.py - 生成城市建筑的库
vShatterLib.py - 沃罗诺图算法库
RigidBodyLib.py - 玛雅刚体模拟库
shockWaveLib.py - 冲击波模拟库

1. 安装：
   要在 Maya 中使用 CityExploser 插件，请按照以下步骤操作：
   - 将所有 python 文件复制到计算机上的 maya scripts 文件夹（如"\Documents\maya\2023\zh_CN\scripts"）。
   - 文件放置到正确路径后，就可以打开脚本编辑器，打开脚本文件夹中的 "CityExploser.py"，点击运行。

2. 功能：
   CityExploser 插件可以帮助您随机生成城市建筑群，并模拟核爆炸过程中城市建筑的碎裂和冲击波效果：

   - 调整生成的城市参数，实现随机生成建筑的效果。
   - 使用 Voronoi 图算法实现建筑物破碎。
   - 在群组下穿越物体并对其应用刚体物理。
   - 为物体创建消失动画，可调整起始帧、持续时间和随机性。
   - 模拟冲击波的扩散效果。

3. 参数： 
   这是城市生成选项卡的参数列表。
   - Building_Width：建筑物的大小，在运行脚本时乘以一个随机值。
   - Building_Height：建筑物的高度，在运行脚本时将乘以一个随机值。
   - City_Size：城市大小，一个城市的最大大小。
   - Block_Size：街区大小，城市被划分为多个街区，街道围绕街区生成。
   - Street_Width：街道宽度，生成不同宽度的街道。
   - Building_Type_Checked：是否生成更多类型的建筑物，默认为否，如果选中，将生成 3 种不同类型的建筑物。

   这是爆炸选项卡的参数列表。
   - Fragments/object：建筑物破碎的碎片数量，使用滑块最大为 8 个，最小为 2 个。
   - Magnitude： 重力场的重力
   - lnitial_Velocity：碎片的刚体运动速度。
   - KeyFrame_Duration：每个片段从创建到消失之间的时间。
   - Wave1_StartTime：冲击波的起始时间。
   - Wave1_EndTime：冲击波的结束时间。
   - Center_Height：冲击波中心的高度。

4. 版权声明：
   Author： 沈思扬 徐云楷  颜潇涵 郑蕲
   版本: 3.0
   日期：2023 年 7 月 23 日