import maya.cmds as cmds
import random

def surfaceMaterial(obj, R, G, B):
    """
    Create a surface material with the specified color and apply it to the given object.

    Args:
        obj (str): The name of the object to apply the material to.
        R (float): The red component of the material color (0 to 1).
        G (float): The green component of the material color (0 to 1).
        B (float): The blue component of the material color (0 to 1).

    Returns:
        str: The name of the created material.
    """
    name = (obj + '_shardMaterial')
    if ( cmds.objExists(name) == 0 ):
        cmds.shadingNode( 'lambert', asShader = True, name = name )
        cmds.sets( renderable = True, noSurfaceShader = True, empty = True, name = (name + 'SG'))
        cmds.connectAttr( (name + '.outColor'), (name + 'SG.surfaceShader'), force = True)
        cmds.setAttr((name + '.color'), R, G, B, type = "double3") 
    return name

def vShatter(obj, surfaceMat, num):
    """
    Perform voronoi shattering on the specified object.

    Args:
        obj (str): The name of the object to shatter.
        num (int): The number of voronoi cuts to perform.

    Returns:
        None
    """
    # Shut down the history
    cmds.undoInfo(openChunk=True, chunkName='vShatter', state = False)
    cmds.bakePartialHistory(obj, prePostDeformers=True)
    # Evaluate the bounding box points [minX, minY, minZ, maxX, maxY, maxZ]
    bbPoints = cmds.exactWorldBoundingBox(obj) 
    print(bbPoints)
    
    # Place the random points for polycut, based on the bounding box
    numPoints = num
    voroX = [random.uniform(bbPoints[0], bbPoints[3]) for i in range(numPoints)]
    voroY = [random.uniform(bbPoints[1], bbPoints[4]) for i in range(numPoints)]
    voroZ = [random.uniform(bbPoints[2], bbPoints[5]) for i in range(numPoints)]
    voroPoints = list(zip(voroX, voroY, voroZ))
    
    cmds.setAttr(obj+'.visibility',0)
    
    cmds.progressWindow(title = "Voronoi Calculating", progress = 0, isInterruptable = True, maxValue = numPoints)
    cmds.undoInfo(state = False)
    cmds.setAttr( str(obj) + '.visibility' , 0)
    step = 0
    
    chunksGrp = cmds.group(em=True, name=obj + '_chunks_')

    for voroFrom in voroPoints:
        if cmds.progressWindow(q=True, isCancelled=True ): break
        if cmds.progressWindow(q=True, progress=True ) >= numPoints: break
        step = step + 1
    	
        cmds.progressWindow( edit=True, progress=step, status=("Shattering step %d of %d completed..." % (step, numPoints)) )
        cmds.refresh()
        
        # Duplicate the object to cut as shatters
        workingObj = cmds.duplicate(obj)
        cmds.setAttr(str(workingObj[0])+'.visibility',1)
        chunkName = obj + '_chunk_' + str(step)
        chunkGrp = cmds.group(em=True, name=chunkName)
        cmds.parent(workingObj, chunkGrp)
        cmds.parent(chunkGrp, chunksGrp)
        
        for voroTo in voroPoints:
            if voroFrom != voroTo:
                # Calculate the Perpendicular Bisector Plane
                aim = [(vec1-vec2) for (vec1,vec2) in list(zip(voroFrom,voroTo))]
                voroCenter = [(vec1 + vec2)/2 for (vec1,vec2) in list(zip(voroTo,voroFrom))]
                planeAngle = cmds.angleBetween( euler=True, v1=[0,0,1], v2=aim )
                # Bullet Shatter
                cmds.polyCut(workingObj[0], df=True, cutPlaneCenter = voroCenter, cutPlaneRotate = planeAngle)
                
                # Applying the material to the cut faces
                oriFaces = cmds.polyEvaluate(workingObj[0], face=True)
                cmds.polyCloseBorder(workingObj[0], ch=False)
                aftFaces = cmds.polyEvaluate(workingObj[0], face=True)
                newFaces = aftFaces - oriFaces
                

                cutFaces = ( '%s.f[ %d ]' % (workingObj[0], (aftFaces + newFaces - 1)))
                cmds.sets(cutFaces, forceElement = (surfaceMat + 'SG'), e=True)                    
        
        cmds.xform(workingObj, cp=True)
        print(str(workingObj))
        
    cmds.xform(chunksGrp, cp=True)
    cmds.progressWindow(endProgress=1)
    cmds.undoInfo(state = True)
    # Reopen the history
    cmds.bakePartialHistory(obj, prePostDeformers=True)
    cmds.undoInfo(closeChunk=True, chunkName='vShatter', state=True)
