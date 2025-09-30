import sys
import os
current_dir_gripper = os.path.dirname(os.path.abspath(__file__)) # 예를들어 부모 디렉토리를 만든다면 parent_dir = os.path.join(current_dir, '..') 이렇게도 가능
sys.path.append(current_dir_gripper)
import numpy as np
import odrive
from Actuator import *

FREQUENCY = 50 #Hz

SN_M1 = 'serial_no_of_motor1'
SN_M2 = 'serial_no_of_motor２'

odrv0 = odrive.find_any(serial_number=SN_M1)
odrv1 = odrive.find_any(serial_number=SN_M2)

MOTOR1 = Actuator(odrv0, 0, 1, 45) # left finger
MOTOR2 = Actuator(odrv1, 0, 1, 45)

sharedTimeList = []
sharedPositionList = []

sharedData = 0
def GetMotorVelocity():
    tempArray = np.zeros(2)
    tempArray[0] = MOTOR1.motor_vel
    tempArray[1] = MOTOR2.motor_vel
    return tempArray

def ClearErrors():
    MOTOR1.clearErrors()
    MOTOR2.clearErrors()

def GetCurrentsoftmax():
    tempArray = np.zeros(2)
    tempArray[0] = MOTOR1.current_soft_max
    tempArray[1] = MOTOR2.current_soft_max
    return tempArray

def Gettorquesoftmax():
    tempArray = np.zeros(2)
    tempArray[0] = MOTOR1.torque_soft_max
    tempArray[1] = MOTOR2.torque_soft_max
    return tempArray

def GetMotorPosition():
    tempArray = np.zeros(2)
    tempArray[0] = MOTOR1.motor_pos
    tempArray[1] = MOTOR2.motor_pos
    return tempArray

def GetStiffness():
    tempArray = np.zeros(2)
    tempArray[0] = MOTOR1.stiffness
    tempArray[1] = MOTOR2.stiffness
    return tempArray

def GetVelocityGains():
    tempArray = np.zeros(2)
    tempArray[0] = MOTOR1.vel_gain
    tempArray[1] = MOTOR2.vel_gain
    return tempArray

def GetCurrent():
    tempArray = np.zeros(2)
    tempArray[0] = MOTOR1.iBusValue()
    tempArray[1] = MOTOR2.iBusValue()
    return tempArray

def GetEncoderValue():
    tempArray = np.zeros(2)
    tempArray[0] = MOTOR1.encoder
    tempArray[1] = MOTOR2.encoder
    return tempArray

def SetMotorVelocity(motorVelocitys):
    MOTOR1.motor_vel=motorVelocitys[0]
    MOTOR2.motor_vel=motorVelocitys[1]

def SetCurrentsoftmax(motorCurrentsoftmax):
    MOTOR1.current_soft_max=motorCurrentsoftmax[0]
    MOTOR2.current_soft_max=motorCurrentsoftmax[1]

def Settorquesoftmax(motortorquesoftmax):
    MOTOR1.current_soft_max=motortorquesoftmax[0]
    MOTOR2.current_soft_max=motortorquesoftmax[1]

def SetMotorPosition(motorAngles):
    MOTOR1.motor_pos = motorAngles[0]
    MOTOR2.motor_pos = motorAngles[1]


# stiffness = P-Gain
def SetStiffness(stiffness):
    MOTOR1.stiffness = stiffness[0]
    MOTOR2.stiffness = stiffness[1]

def SetVelocityGain(velGains):
    MOTOR1.vel_gain = velGains[0]
    MOTOR2.vel_gain = velGains[1]

def SetControlState():
    ClearErrors()
    MOTOR1.armed = True
    MOTOR2.armed = True
    SetStiffness([30,30,30, 30])
    SetVelocityGain([0.5,0.5,0.5, 0.5])
    print("      [SPATULA/ CONTROL STATE]")

def SetIdleState():
    ClearErrors()
    MOTOR1.armed = False
    MOTOR2.armed = False
    print("      [SPATULA/ IDLE STATE]")

