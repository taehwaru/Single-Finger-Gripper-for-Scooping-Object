import sys
import os
current_dir_gripper = os.path.dirname(os.path.abspath(__file__)) # 예를들어 부모 디렉토리를 만든다면 parent_dir = os.path.join(current_dir, '..') 이렇게도 가능
sys.path.append(current_dir_gripper)
import numpy as np
import odrive
from Actuator import *

FREQUENCY = 50 #Hz

SN_L0 = '394B34723331'
SN_L1 = '396634703331'
#SN_R0 = '00E848E14C9C'
#SN_R1 = '00E848E15413' 




odrv0 = odrive.find_any(serial_number=SN_L0)
odrv1 = odrive.find_any(serial_number=SN_L1)
#odrv2 = odrive.find_any(serial_number=SN_R0)
#odrv3 = odrive.find_any(serial_number=SN_R1)

LF0 = Actuator(odrv0, 0, 1, 45) # left finger
LF1 = Actuator(odrv1, 0, 1, 45)
#RF0 = Actuator(odrv2, 0, 1, 45) # right finger
#RF1 = Actuator(odrv3, 0, 1, 45)

sharedTimeList = []
sharedPositionList = []

sharedData = 0
def GetMotorVelocity():
    tempArray = np.zeros(4)
    tempArray[0] = LF0.motor_vel
    tempArray[1] = LF1.motor_vel
    #tempArray[2] = RF0.motor_vel
    #tempArray[3] = RF1.motor_vel
    return tempArray

def ClearErrors():
    LF0.clearErrors()
    LF1.clearErrors()
    #RF0.clearErrors()
    #RF1.clearErrors()

def GetCurrentsoftmax():
    tempArray = np.zeros(4)
    tempArray[0] = LF0.current_soft_max
    tempArray[1] = LF1.current_soft_max
    #tempArray[2] = RF0.current_soft_max
    #tempArray[3] = RF1.current_soft_max
    return tempArray

def Gettorquesoftmax():
    tempArray = np.zeros(4)
    tempArray[0] = LF0.torque_soft_max
    tempArray[1] = LF1.torque_soft_max
    #tempArray[2] = RF0.torque_soft_max
    #tempArray[3] = RF1.torque_soft_max
    return tempArray

def GetMotorPosition():
    tempArray = np.zeros(4)
    tempArray[0] = LF0.motor_pos
    tempArray[1] = LF1.motor_pos
    #tempArray[2] = RF0.motor_pos
    #tempArray[3] = RF1.motor_pos
    return tempArray

def GetStiffness():
    tempArray = np.zeros(4)
    tempArray[0] = LF0.stiffness
    tempArray[1] = LF1.stiffness
    #tempArray[2] = RF0.stiffness
    #tempArray[3] = RF1.stiffness
    return tempArray

def GetVelocityGains():
    tempArray = np.zeros(4)
    tempArray[0] = LF0.vel_gain
    tempArray[1] = LF1.vel_gain
    #tempArray[2] = RF0.vel_gain
    #tempArray[3] = RF1.vel_gain
    return tempArray

def GetCurrent():
    tempArray = np.zeros(4)
    tempArray[0] = LF0.iBusValue()
    tempArray[1] = LF1.iBusValue()
    #tempArray[2] = RF0.iBusValue()
    #tempArray[3] = RF1.iBusValue()
    return tempArray

def GetEncoderValue():
    tempArray = np.zeros(4)
    tempArray[0] = LF0.encoder
    tempArray[1] = LF1.encoder
    #tempArray[2] = RF0.encoder
    #tempArray[3] = RF1.encoder
    return tempArray

def SetMotorVelocity(motorVelocitys):
    LF0.motor_vel=motorVelocitys[0]
    LF1.motor_vel=motorVelocitys[1]
    #RF0.motor_vel=motorVelocitys[2]
    #RF1.motor_vel=motorVelocitys[3]

def SetCurrentsoftmax(motorCurrentsoftmax):
    LF0.current_soft_max=motorCurrentsoftmax[0]
    LF1.current_soft_max=motorCurrentsoftmax[1]
    #RF0.current_soft_max=motorCurrentsoftmax[2]
    #RF1.current_soft_max=motorCurrentsoftmax[3]

def Settorquesoftmax(motortorquesoftmax):
    LF0.current_soft_max=motortorquesoftmax[0]
    LF1.current_soft_max=motortorquesoftmax[1]
    #RF0.current_soft_max=motortorquesoftmax[2]
    #RF1.current_soft_max=motortorquesoftmax[3]
    

def SetMotorPosition(motorAngles):
    LF0.motor_pos = motorAngles[0]
    LF1.motor_pos = motorAngles[1]
    #RF0.motor_pos = motorAngles[2]
    #RF1.motor_pos = motorAngles[3]

# stiffness = position gain
def SetStiffness(stiffness):
    LF0.stiffness = stiffness[0]
    LF1.stiffness = stiffness[1]
    #RF0.stiffness = stiffness[2]
    #RF1.stiffness = stiffness[3]

def SetVelocityGain(velGains):
    LF0.vel_gain = velGains[0]
    LF1.vel_gain = velGains[1]
    #RF0.vel_gain = velGains[2]
    #RF1.vel_gain = velGains[3]

def SetControlState():
    ClearErrors()
    LF0.armed = True
    LF1.armed = True
    #RF0.armed = True
    #RF1.armed = True
    SetStiffness([30,30,30, 30])
    SetVelocityGain([0.5,0.5,0.5, 0.5])
    print("      [GRIPPER/ CONTROL STATE]")

def SetIdleState():
    ClearErrors()
    LF0.armed = False
    LF1.armed = False
    #RF0.armed = False
    #RF1.armed = False
    print("      [GRIPPER/ IDLE STATE]")


