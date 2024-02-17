import maya.cmds as cmds

def createWaveScene(waveStartTime1, waveStartTime2, waveStopTime1, waveStopTime2, wavescalestartX1, wavescalestartY1, wavescalestopX1, wavescalestopY1, wavescalestartX2, wavescalestartY2, wavescalestopX2, wavescalestopY2, transparency, height,delay1,delay2,delay3):

    # Color of the shock wave
    colorR = 1
    colorG = 1
    colorB = 1

    # Create a plane as the ground
    ground = cmds.polyPlane(width=200, height=200)[0]

    # Create a sphere as the shock wave
    wave = cmds.polySphere(radius=2)[0]

    # Create a material and apply it to the shock wave
    wave_material = cmds.shadingNode('lambert', asShader=True)
    cmds.setAttr(wave_material + ".color", colorR, colorG, colorB, type="double3")


    cmds.select(wave)
    cmds.hyperShade(assign=wave_material)

    # Create a particle system
    particle_system = cmds.nParticle()

    # Make the particle system collide with the shock wave sphere
    cmds.select(wave, particle_system)
    cmds.collision

    # Create shock wave 1
    cmds.setKeyframe(wave, attribute='translateY', time=waveStartTime1, value=height)
    cmds.setKeyframe(wave, attribute='scaleX', time=waveStartTime1, value=wavescalestartX1)
    cmds.setKeyframe(wave, attribute='scaleY', time=waveStartTime1, value=wavescalestartY1)
    cmds.setKeyframe(wave, attribute='scaleZ', time=waveStartTime1, value=wavescalestartX1)

    cmds.setKeyframe(wave, attribute='translateY', time=waveStopTime1, value=height)
    cmds.setKeyframe(wave, attribute='scaleX', time=waveStopTime1, value=wavescalestopX1)
    cmds.setKeyframe(wave, attribute='scaleY', time=waveStopTime1, value=wavescalestopY1)
    cmds.setKeyframe(wave, attribute='scaleZ', time=waveStopTime1, value=wavescalestopX1)

    

    wave2 = cmds.polySphere(radius=2)[0]

    # Create a material and apply it to the shock wave
    wave2_material = cmds.shadingNode('lambert', asShader=True)
    cmds.setAttr(wave2_material + ".color", colorR, colorG, colorB, type="double3")

    # Set transparency
    cmds.setAttr(wave2_material + ".transparency", transparency, transparency, transparency, type="double3")
    cmds.select(wave2)
    cmds.hyperShade(assign=wave2_material)

    particle_system = cmds.nParticle()

    # Make the particle system collide with the shock wave sphere
    cmds.select(wave2, particle_system)
    cmds.collision

    # Create shock wave 2
    cmds.setKeyframe(wave2, attribute='translateY', time=waveStartTime2, value=height)
    cmds.setKeyframe(wave2, attribute='scaleX', time=waveStartTime2, value=wavescalestartX2)
    cmds.setKeyframe(wave2, attribute='scaleY', time=waveStartTime2, value=wavescalestartY2)
    cmds.setKeyframe(wave2, attribute='scaleZ', time=waveStartTime2, value=wavescalestartX2)

    cmds.setKeyframe(wave2, attribute='translateY', time=waveStopTime2, value=height)
    cmds.setKeyframe(wave2, attribute='scaleX', time=waveStopTime2, value=wavescalestopX2)
    cmds.setKeyframe(wave2, attribute='scaleY', time=waveStopTime2, value=wavescalestopY2)
    cmds.setKeyframe(wave2, attribute='scaleZ', time=waveStopTime2, value=wavescalestopX2)

    wave3 = cmds.polySphere(radius=2)[0]

    # Create a material and apply it to the shock wave
    wave3_material = cmds.shadingNode('lambert', asShader=True)
    cmds.setAttr(wave3_material + ".color", colorR, colorG, colorB, type="double3")

    # Set transparency
    cmds.setAttr(wave3_material + ".transparency", transparency*0.8, transparency*0.8, transparency*0.8, type="double3")
    cmds.select(wave3)
    cmds.hyperShade(assign=wave3_material)

    particle_system = cmds.nParticle()

    # Make the particle system collide with the shock wave sphere
    cmds.select(wave3, particle_system)
    cmds.collision

    # Create shock wave 2
    cmds.setKeyframe(wave3, attribute='translateY', time=waveStartTime2-delay1, value=height)
    cmds.setKeyframe(wave3, attribute='scaleX', time=waveStartTime2-delay1, value=wavescalestartX2)
    cmds.setKeyframe(wave3, attribute='scaleY', time=waveStartTime2-delay1, value=wavescalestartY2)
    cmds.setKeyframe(wave3, attribute='scaleZ', time=waveStartTime2-delay1, value=wavescalestartX2)

    cmds.setKeyframe(wave3, attribute='translateY', time=waveStopTime2-delay1, value=height)
    cmds.setKeyframe(wave3, attribute='scaleX', time=waveStopTime2-delay1, value=wavescalestopX2)
    cmds.setKeyframe(wave3, attribute='scaleY', time=waveStopTime2-delay1, value=wavescalestopY2)
    cmds.setKeyframe(wave3, attribute='scaleZ', time=waveStopTime2-delay1, value=wavescalestopX2)



    wave4 = cmds.polySphere(radius=2)[0]

    # Create a material and apply it to the shock wave
    wave4_material = cmds.shadingNode('lambert', asShader=True)
    cmds.setAttr(wave4_material + ".color", colorR, colorG, colorB, type="double3")

    # Set transparency
    cmds.setAttr(wave4_material + ".transparency", transparency*0.75, transparency*0.75, transparency*0.75, type="double3")
    cmds.select(wave4)
    cmds.hyperShade(assign=wave4_material)

    particle_system = cmds.nParticle()

    # Make the particle system collide with the shock wave sphere
    cmds.select(wave4, particle_system)
    cmds.collision

    # Create shock wave 2
    cmds.setKeyframe(wave4, attribute='translateY', time=waveStartTime2-delay2, value=height)
    cmds.setKeyframe(wave4, attribute='scaleX', time=waveStartTime2-delay2, value=wavescalestartX2)
    cmds.setKeyframe(wave4, attribute='scaleY', time=waveStartTime2-delay2, value=wavescalestartY2)
    cmds.setKeyframe(wave4, attribute='scaleZ', time=waveStartTime2-delay2, value=wavescalestartX2)

    cmds.setKeyframe(wave4, attribute='translateY', time=waveStopTime2-delay2, value=height)
    cmds.setKeyframe(wave4, attribute='scaleX', time=waveStopTime2-delay2, value=wavescalestopX2)
    cmds.setKeyframe(wave4, attribute='scaleY', time=waveStopTime2-delay2, value=wavescalestopY2)
    cmds.setKeyframe(wave4, attribute='scaleZ', time=waveStopTime2-delay2, value=wavescalestopX2)



    wave5 = cmds.polySphere(radius=2)[0]

    # Create a material and apply it to the shock wave
    wave5_material = cmds.shadingNode('lambert', asShader=True)
    cmds.setAttr(wave5_material + ".color", colorR, colorG, colorB, type="double3")

    # Set transparency
    cmds.setAttr(wave5_material + ".transparency", transparency*0.7, transparency*0.7, transparency*0.7, type="double3")
    cmds.select(wave5)
    cmds.hyperShade(assign=wave3_material)

    particle_system = cmds.nParticle()

    # Make the particle system collide with the shock wave sphere
    cmds.select(wave5, particle_system)
    cmds.collision

    # Create shock wave 2
    cmds.setKeyframe(wave5, attribute='translateY', time=waveStartTime2-delay1, value=height)
    cmds.setKeyframe(wave5, attribute='scaleX', time=waveStartTime2-delay1, value=wavescalestartX2)
    cmds.setKeyframe(wave5, attribute='scaleY', time=waveStartTime2-delay1, value=wavescalestartY2)
    cmds.setKeyframe(wave5, attribute='scaleZ', time=waveStartTime2-delay1, value=wavescalestartX2)

    cmds.setKeyframe(wave5, attribute='translateY', time=waveStopTime2-delay1, value=height)
    cmds.setKeyframe(wave5, attribute='scaleX', time=waveStopTime2-delay1, value=wavescalestopX2)
    cmds.setKeyframe(wave5, attribute='scaleY', time=waveStopTime2-delay1, value=wavescalestopY2)
    cmds.setKeyframe(wave5, attribute='scaleZ', time=waveStopTime2-delay1, value=wavescalestopX2)

