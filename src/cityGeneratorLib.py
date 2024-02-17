import maya.cmds as cmds
import random

'''
Generates the city.  
The function creates a ground plane, divides the city into blocks, and generates buildings within each block.

Args:  
    isSquare (bool): Determines whether the city is square-shaped or not. Default value is True. 
    blockSize (int)
    streetWidth (int)
    buildingGap (int)
    buildingHeight (int)
    buildingWidth (int)
    buildingTypeChecked (int)
    sSquare (bool): Default is True
'''
def cityGene(cityRange, blockSize, streetWidth, buildingGap, buildingHeight, buildingWidth,buildingTypeChecked, isSquare = True):

    # Clearing existing objects in the scene
    clearScreen()
    
    # If you want to generate square cities
    if(isSquare):
        # Generate city planes and assign rigid body properties
        cmds.polyPlane(w=cityRange*4, h=cityRange*4, n="ground")
        cmds.move(0, 0, 0)
        addPassiveRigidBody("ground")

        # Cyclic generation of city blocks
        for i in range(0, int((cityRange)/(blockSize+streetWidth))):
            for j in range(0, int((cityRange)/(blockSize+streetWidth))):
                # Calculating neighborhood locations
                xBlockPos = int((i+0.5)*(blockSize+streetWidth) - cityRange*0.5 )
                zBlockPos = int((j+0.5)*(blockSize+streetWidth) - cityRange*0.5 )
                squareBlockGen(xBlockPos, zBlockPos, blockSize, buildingGap, buildingHeight, buildingWidth, buildingTypeChecked)
    # If you don't want to generate square cities
    # Not yet realized
    else:
        pass

    return Building.getBuildingCount()


    
'''
Generates buildings within a square block. 
The function generates random buildings of different sizes and heights within the block.


Args:  
    xPos (float): The x-coordinate of the block
    yPos (float): The x-coordinate of the block
    blockSize (int)
    buildingGap (int)
    buildingHeight (int)
    buildingWidth (int)
    buildingTypeChecked (int)
'''
def squareBlockGen(xPos, zPos, blockSize, buildingGap, buildingHeight, buildingWidth, buildingTypeChecked):

    xSpace = 0
    zSpace = 0
    biggestX = 0
    smallestX = int(buildingWidth * 0.6)


    # Cyclic generation of city buildings
    while (xSpace < blockSize):
        zSpace = 0
        while(zSpace<blockSize):
            # Randomly generated building length, width and height
            randomX = randomWidth(smallestX, buildingWidth)
            randomZ = randomWidth(randomX, randomX)
            randomH = randomWidth(buildingHeight, buildingHeight)

            # Smaller chance of generating higher buildings
            if(random.randrange(0, 100) > 90):
                randomH = randomH + (randomH * 0.7)

            # Getting the maximum building length
            if(randomX>biggestX):
                biggestX = randomX

            # Determine if the city block boundaries are exceeded
            if(zSpace + randomZ + buildingGap + 1 > blockSize):
                break

            if buildingTypeChecked:
                buildingType = random.randrange(0,3)
            else:
                buildingType = 0

            # Generate individual buildings, and move to the specified position
            building = Building(randomX, randomZ, randomH, buildingType)
            building.createBuilding()

            zBuildingPos = (zSpace + randomZ*0.5)
            wBuildingPos = (xSpace + randomX*0.5)
            building.moveBuilding(xPos+wBuildingPos, randomH * 0.5 + 0.2, zPos+zBuildingPos)

            # Record the current position
            zSpace = zSpace + randomZ + buildingGap

        # Record the current position
        xSpace = xSpace + biggestX + buildingGap
        biggestX = 0

        # Determine if the city block boundaries are exceeded
        if(blockSize - xSpace < smallestX):
            break


'''
Clears the Maya scene by deleting all objects.
'''
def clearScreen():
    Building.clearCount()
    cmds.select(all=True)
    cmds.delete()


'''
A class representing a building. 
It has properties like width, height, depth, building type, and name. 
It also has methods for creating and moving the building.
'''
class Building:
    # the generated building counts
    buildingCount = 0

    """  
    Initializes a Building object with the given properties.  

    Args:  
        width (float): The width of the building.  
        height (float): The height of the building.  
        depth (float): The depth of the building.  
        building_type (int): The type of the building.  
    """  
    def __init__(self, inWidth, inDepth, inHeight, typeOfBuilding = 0):
        # Setting Building Parameters
        Building.buildingCount += 1
        print(self.buildingCount)
        self.buildingName = "Building_" + str(self.buildingCount)

        self.width = inWidth
        self.height = inHeight
        self.depth = inDepth

        self.buildingType = typeOfBuilding

        self.xDiv = 10
        self.yDiv = 10
        self.zDiv = 10

    
    """  
    Creates the building in the Maya scene at the specified position.   
    """  
    def createBuilding(self):
        # Generate Square Buildings
        if(self.buildingType == 0):
            cmds.polyCube(w = self.width, d = self.depth, h = self.height, n =  str(self.buildingName))
        # Generate Towers
        elif(self.buildingType == 1):
            cmds.polyCube(w = self.width, d = self.depth, h = int(self.height), n =  str(self.buildingName))

            for i in range(0, random.randrange(0,3)):
                cmds.polyExtrudeFacet(str(self.buildingName) + ".f[1]", kft = False, ls = (0.75, 0.75, 0))
                cmds.polyExtrudeFacet(str(self.buildingName) + ".f[1]", kft = False, ltz = random.randrange(15, 30))
        # Generating buildings with windows
        else:
            cmds.polyCube(w = self.width, d = self.depth, h = self.height, sx = self.xDiv, sy = self.yDiv, sz = self.zDiv, n = str(self.buildingName))
            
            sides = []

            for i in range(0, 8):
                if(i != 1 and i != 3):
                    sides.append(str(self.buildingName) + ".f[" + str(self.xDiv * self.yDiv * i) + ":" + str((self.xDiv * self.yDiv * (i+1)) - 1) + "]")
        
            cmds.polyExtrudeFacet(sides[0], sides[1], sides[2], sides[3], sides[4], sides[5], kft = False, ls = (0.8, 0.8, 0))
            windows = cmds.ls(sl = True)
            print(len(windows))
            cmds.polyExtrudeFacet(windows[1], windows[2], kft = False, ltz = -0.2)
            cmds.select(self.buildingName)

    
    """  
    Move the generated building to the specified location

    Args:  
        x (float): The x-coordinate of the building
        y (float): The x-coordinate of the building
        z (float): The x-coordinate of the building
    """  
    def moveBuilding(self, x, y, z):
        cmds.select(self.buildingName)
        cmds.move(x,y,z)
        cmds.select(cl=True)


    '''
    Clear building counts.
    '''
    def clearCount():
        Building.buildingCount = 0

    '''
    Getting building counts.
    '''
    def getBuildingCount():
        return Building.buildingCount


'''

'''
def randomWidth(smallP, largeP):
    return int(random.randrange(smallP*6, largeP*24)/10)



'''
A helper function that returns a random float within a range with a specified step.
'''
def addPassiveRigidBody(ground):
    # Check if the object exists
    if cmds.objExists(ground):
        # Add passive rigid body properties
        cmds.select(ground, replace=True)
        cmds.rigidBody(passive=True)