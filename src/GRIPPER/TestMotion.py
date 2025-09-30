import sys
from time import sleep
import numpy as np
import Spatula
from GRIPPER.Spatula import FREQUENCY
from fivebar import ik_5bar_angles_deg
from fivebar import ik_fingerTip_to_Edge
import RB5
import numpy as np

# 로봇 객체 정의 (전역 변수 또는 클래스로 관리)
# ROBOT_IP = "192.168.0.25"
# robot = rb.Cobot(ROBOT_IP)
# rc = rb.ResponseCollector()

def TestGetEncoder():
    
    while True:
        pos = Spatula.GetMotorPosition()
        print(f"motor_pos : [{pos[0]:.4f}, {pos[1]:.4f},{pos[2]:.4f} ,{pos[3]:.4f} ]  deg")
        sleep(0.3)
         #0.3 간격으로 motor_pos값 받아서 출력

def TestCurrent():
    print("   [SPATULA / TEST CURRENT]")
    timeStep = 0.0
    readyPosition = [17, 27]
    Spatula.SetControlState()
    Spatula.SetMotorPosition(readyPosition)
    sleep(1.0)

    Spatula.SetStiffness([30,30])
    Spatula.SetVelocityGain([0.3,0.3])

    while(timeStep < 30):

        # print(Spatula.GetCurrent())
        # Spatula.sharedData = 3
        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)

    Spatula.SetIdleState()

def Test_fingerTip():
    print("fingertip(T) Control")
    pos = Spatula.GetMotorPosition()
    Spatula.SetControlState()
    Spatula.SetStiffness([50,50])
    Spatula.SetVelocityGain([0.2,0.2])
    xT=-80
    yT=0
    th1_T, th2_T = ik_fingerTip_to_Edge(xT, yT)
    position0=[th1_T, th2_T]
    Spatula.SetControlState()
    Spatula.SetMotorPosition(position0)
    sleep(0.3)    

def Test_linkageEdge():
    print("Edge of the 5-bar linkage(E) Control")
    pos = Spatula.GetMotorPosition()
    Spatula.SetControlState()
    Spatula.SetStiffness([50,50])
    Spatula.SetVelocityGain([0.2,0.2])
    xE = 0
    yE = 0
    th1_E, th2_E = ik_5bar_angles_deg(xE, yE)
    position0=[th1_E, th2_E]
    Spatula.SetControlState()
    Spatula.SetMotorPosition(position0)
    sleep(0.3)    
            
def Scoop():
    x0=-10
    y0=130
    shoulder01, shoulder02 = ik_fingerTip_to_Edge(x0, y0)

    x1=100
    y1=10
    shoulder11, shoulder12 = ik_fingerTip_to_Edge(x1, y1)
    position1=[shoulder01,shoulder02] # start point
    Spatula.SetControlState()
    Spatula.SetMotorPosition(position1)
    sensitivity=10 # 오차 범위 ±5
    sensi=sensitivity*0.5
    pos = Spatula.GetMotorPosition()
    position12=[shoulder11, shoulder12]# end point
    pgain=[15,15]
    softmax=[4,4]
    torquemax=[2,2]
    
    cnt=0  
    sleep(3)
    
    while True:
        pos = Spatula.GetMotorPosition()
        print(f"motor_pos : [{pos[0]:.4f}, {pos[1]:.4f}]  deg")
        if (cnt==1):
            break
        if ((pos[0] < position1[0]-sensi or pos[0] > position1[0]+sensi or pos[1] < position1[1]-sensi or pos[1] > position1[1]+sensi ) and (cnt==0)): # 0.01초 간격으로 모터 위치 확인
             Spatula.Settorquesoftmax(torquemax)
             Spatula.SetCurrentsoftmax(softmax)
             Spatula.SetStiffness(pgain)
             sleep(0.1)
             Spatula.SetMotorPosition(position12)
             sleep(5)
             cnt+=1
             
        sleep(0.01)
    Spatula.SetIdleState()
       
def TestMotionStop():
    print("   [SPATULA / TEST MOTION]")

    position1 = [14, 25]
    position2 = [-36, 100]
    position3 = [-35, 44]
    position4 = [35, 24]
    position5 = [-9, 23]

    Spatula.SetControlState()

    Spatula.SetStiffness([50,50])
    Spatula.SetVelocityGain([0.15,0.15])

    Spatula.SetMotorPosition(position1)
    # Spatula.SetIdleState()
