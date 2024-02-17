import maya.cmds as cmds
import random as rd
import math 

'''
Constant setting
'''
ZERO_VECTOR = [0,0,0]
# Adjustable final fragment size
END_SCALE_FRAME = [0.2,0.2,0.2]
ORIGINAL_ANGULAR = [0.5,0.5,0.5]
RANDOM_SIZE = 0.002
'''
Name: traverseGroup
Function: Traverse each node under the group
'''
def traverseGroup(groupName, 
                  gravityName,
                  initialVelocity, 
                  velocityRandom, 
                  angleRandom, 
                  selfAngularVelocityRandom, 
                  keyFrameStart,
                  keyFrameDuration, 
                  keyFrameDurationRandom):
    # Check whether the team exists
    if not cmds.objExists(groupName):
        print("Group {} does not exist".format(groupName))
        return
    
    # Gets all object groups in the group
    objects_groups = cmds.listRelatives(groupName, allDescendents=False, fullPath=True)
    # Extract all object groups from the group and re-link them into a new group
    print(objects_groups)
    objects = []
    for component in objects_groups:
        objects.append(cmds.listRelatives(component,allDescendents=False, fullPath=True))
    
    if not objects:
        print("No object in group {}.".format(groupName))
        return
    print(objects)
    # Walk through each object
    for obj in objects:
        # Each child is linked to a gravitational field
        cmds.connectDynamic(obj, fields=gravityName)
        makeDisappearAnimation(obj=obj, startFrame=keyFrameStart, duration=keyFrameDuration,random=keyFrameDurationRandom)
        # Each object is endowed with an initial impulse
        giveInitialImpulse(object= obj, startFrame=keyFrameStart, initialVelocity=initialVelocity, velocityRandom=velocityRandom, angleRandom=angleRandom)

        giveSelfAngularVelocityRandom(object=obj,startFrame=keyFrameStart, selfAngularRandom=selfAngularVelocityRandom)




'''
Name: randImpulse
Function: Calculate random initial velocity
'''
def randImpulse(velocity, angleRandom, velocityRandom):
    ### velocityRandom, angleRandom is [0,1)
    magnitude = math.sqrt(sum([coord ** 2 for coord in velocity]))
    
   # Generate coordinates of random vectors
    randomCoords = [rd.uniform(0,angleRandom) for _ in range(len(velocity))]
    
    # Calculate the size of the random vector
    randomMagnitude = math.sqrt(sum([coord ** 2 for coord in randomCoords]))
    
    # Scale the random vector to keep the size equal to the original vector
    scaledCoords = [coord * (magnitude / randomMagnitude) for coord in randomCoords]
    # Scale the random vector to add the initial impulse change
    scaledCoords = [component * (rd.uniform(0,velocityRandom)+1) for component in scaledCoords]
    
    # Returns the final random vector
    return scaledCoords

'''
Name: giveInitialImpulse
Function: Assign random initial velocity
'''
def giveInitialImpulse(object, 
                       initialVelocity, 
                       startFrame,
                       angleRandom, 
                       velocityRandom):
    # cmds.rigidBody(object, e=True, i = randImpulse(velocity=initialVelocity, angleRandom = angleRandom, velocityRandom = velocityRandom))

    rigidbodyNode = getRigidbodyNode(objectName=object[0])

    if rigidbodyNode:
        print(f"The rigidBody node for {object} is: {rigidbodyNode}")
    else:
        print(f"{object} does not have a rigidBody node.")

    cmds.currentTime(startFrame)

    randValue = randImpulse(velocity=initialVelocity, angleRandom = angleRandom, velocityRandom = velocityRandom)
    
    impulseValue = initialVelocity
    impulseValue[0] += randValue[0] * RANDOM_SIZE
    impulseValue[1] += randValue[1] * RANDOM_SIZE
    impulseValue[2] += randValue[2] * RANDOM_SIZE


    # debug code---
    print("impulse_value:"+str(impulseValue))
    # ----
    cmds.setAttr(f"{rigidbodyNode}.impulse", impulseValue[0], impulseValue[1], impulseValue[2])

    # Add a keyframe to the impulse property in startFrame
    cmds.setKeyframe(rigidbodyNode, attribute='impulse')

    cmds.currentTime(startFrame-1)
    impulseValue = ZERO_VECTOR
    cmds.setAttr(f"{rigidbodyNode}.impulse", impulseValue[0], impulseValue[1], impulseValue[2])

    # Add a keyframe to the impulse property in startFrame-1
    cmds.setKeyframe(rigidbodyNode, attribute='impulse')


def getRigidbodyNode(objectName):
    print("objectName"+str(objectName))
    rigidbody_nodes = cmds.listConnections(objectName, type="rigidBody")
    print("rigidbody_nodes"+str(rigidbody_nodes))
    if rigidbody_nodes:
        return rigidbody_nodes[0]
    else:
        return None


'''
Name: randAngular
Function: Calculated spin
'''
def randAngular(selfAngularRandom):
    originalAV=ORIGINAL_ANGULAR
    AV=[component * (rd.uniform(0,selfAngularRandom)) for component in originalAV ]
    return AV

'''
Name: giveSelfAngularVelocityRandom
Function: Assign random initial spin
'''
def giveSelfAngularVelocityRandom(object, startFrame, selfAngularRandom):
    # cmds.rigidBody(object, e=True, si = randAngular(selfAngularRandom))

    rigidbodyNode = getRigidbodyNode(objectName=object[0])

    if rigidbodyNode:
        print(f"The rigidBody node for {object} is: {rigidbodyNode}")
    else:
        print(f"{object} does not have a rigidBody node.")
    
    selfAngular = randAngular(selfAngularRandom)
    cmds.currentTime(startFrame)
    # Set impulse to (0.01, 0.01, 0.01)
    # debug code---
    print("selfAngular"+str(selfAngular))
    # ----
    cmds.setAttr(f"{rigidbodyNode}.spinImpulse", selfAngular[0], selfAngular[1], selfAngular[2])

    # Add a keyframe to the impulse property in startFrame
    cmds.setKeyframe(rigidbodyNode, attribute='spinImpulse')

    cmds.currentTime(startFrame-1)
    impulse_value = ZERO_VECTOR
    cmds.setAttr(f"{rigidbodyNode}.spinImpulse", impulse_value[0], impulse_value[1], impulse_value[2])

    # Add a keyframe to the impulse property in startFrame-1
    cmds.setKeyframe(rigidbodyNode, attribute='spinImpulse')

'''
Name: makeRigidBody
Function: Attribute a rigid body
'''
def makeRigidBody(groupName, 
                  gravityName,
                  magnitude, 
                  attenuation, 
                  initialVelocity, 
                  velocityRandom, 
                  angleRandom, 
                  selfAngularVelocityRandom,
                  keyFrameStart,
                  keyFrameDuration, 
                  keyFrameDurationRandom):
    # Create a gravitational field
    cmds.select(all = True, deselect = True)
    # Dangerous constant
    gravityField = cmds.ls(gravityName)
    # print(gravity_field)
    # Constant without relation
    cmds.setAttr(gravityField[0] + ".magnitude", magnitude)
    cmds.setAttr(gravityField[0] + ".attenuation", attenuation)

    # Walk through every child object in this group
    # Assign rigidbody and initial impulse to each child
    traverseGroup(groupName=groupName, 
                  gravityName=gravityName,
                  initialVelocity=initialVelocity, 
                  velocityRandom=velocityRandom, 
                  angleRandom=angleRandom, 
                  selfAngularVelocityRandom=selfAngularVelocityRandom, 
                  keyFrameStart=keyFrameStart,
                  keyFrameDuration=keyFrameDuration,
                  keyFrameDurationRandom=keyFrameDurationRandom)


'''
Name: buildGravityField
Function: Define the internal reference gravity field
'''
def buildGravityField(gravityFieldName):
    if not cmds.objExists(gravityFieldName):
        cmds.select(deselect=True)
        return cmds.gravity(name = gravityFieldName)
    else:
        print("There have been a gravity field!")
'''
Name: makeDisappearAnimation
Function: animation
'''
def makeDisappearAnimation(obj, startFrame, duration, random):
    objName = cmds.listRelatives(obj, parent=True)[0]
    # Gets the current scaling value of the object
    print("objname"+str(obj))
    objName=obj[0]
    startScale = cmds.getAttr(objName + ".scale")[0]

    # Set the animation frame range
    startFrame = cmds.currentTime(startFrame)
    duration += random * int(rd.uniform(0,duration)) * positive_or_negative()
    endFrame = startFrame + duration

    # Create animation keyframes
    cmds.setKeyframe(objName, attribute='scaleX', t=startFrame, v=startScale[0])
    cmds.setKeyframe(objName, attribute='scaleY', t=startFrame, v=startScale[1])
    cmds.setKeyframe(objName, attribute='scaleZ', t=startFrame, v=startScale[2])

    cmds.setKeyframe(objName, attribute='scaleX', t=endFrame, v=END_SCALE_FRAME[0])
    cmds.setKeyframe(objName, attribute='scaleY', t=endFrame, v=END_SCALE_FRAME[1])
    cmds.setKeyframe(objName, attribute='scaleZ', t=endFrame, v=END_SCALE_FRAME[2])

    # Create animation curves
    cmds.selectKey(objName, attribute='scale')
    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def positive_or_negative():
    if rd.random() < 0.5:
        return 1
    else:
        return -1
