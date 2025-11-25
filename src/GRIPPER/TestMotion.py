import sys
from time import sleep
import numpy as np
import Spatula
from GRIPPER.Spatula import FREQUENCY
from fivebar import ik_5bar_Edge
from fivebar import ik_5bar_fingerTip
from fivebar import fk_5bar_Edge
from fivebar import fk_5bar_fingerTip
import RB5
import numpy as np

# 로봇 객체 정의 (전역 변수 또는 클래스로 관리)
# ROBOT_IP = "192.168.0.25"
# robot = rb.Cobot(ROBOT_IP)
# rc = rb.ResponseCollector()

def TestGetTheta():
    
    while True:
        pos = Spatula.GetMotorPosition()
        print(f"motor_pos : [{pos[0]:.4f}, {pos[1]:.4f}]  deg")
        sleep(0.3)
         #0.3 간격으로 motor_pos값 받아서 출력

def TestGetEdge():
    
    while True:
        pos = Spatula.GetMotorPosition()
        xE, yE = fk_5bar_Edge(pos[0], pos[1])
        print(f"Edge : [{xE:.4f}, {yE:.4f}]  mm")
        sleep(0.3)
         #0.3 간격으로 motor_pos값 받아서 출력


def TestGetFingerTip():
    
    while True:
        pos = Spatula.GetMotorPosition()
        xT, yT = fk_5bar_fingerTip(pos[0], pos[1])        
        print(f"fingerTip : [{xT:.4f}, {yT:.4f}]  mm")
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
    xT, yT= 100, 0
    th1_T, th2_T = ik_5bar_fingerTip(xT, yT)
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
    th1_E, th2_E = ik_5bar_Edge(xE, yE)
    position0=[th1_E, th2_E]
    Spatula.SetControlState()
    Spatula.SetMotorPosition(position0)
    sleep(0.3)    
            
def Scoop():
    x0=-40
    y0=130
    shoulder01, shoulder02 = ik_5bar_fingerTip(x0, y0)

    x1=100
    y1=10
    shoulder11, shoulder12 = ik_5bar_fingerTip(x1, y1)
    initialConfiguration=[shoulder01,shoulder02] # start point
    Spatula.SetControlState()
    Spatula.SetMotorPosition(initialConfiguration)
    sensitivity=10 # 오차 범위 ±5
    sensi=sensitivity*0.5
    pos = Spatula.GetMotorPosition()
    goalConfiguration=[shoulder11, shoulder12]# end point
    pgain=[15,15]
    softmax=[4,4]
    cnt=0  
    sleep(3)
    
    while True:
        pos = Spatula.GetMotorPosition()
        x_cur, y_cur = fk_5bar_fingerTip(pos[0], pos[1])
        print(f"tip_pos: [{x_cur:.2f}, {y_cur:.2f}] mm")
        if (cnt==1):
            break
        if ((pos[0] < initialConfiguration[0]-sensi or pos[0] > initialConfiguration[0]+sensi or pos[1] < initialConfiguration[1]-sensi or pos[1] > initialConfiguration[1]+sensi ) and (cnt==0)): # 0.01초 간격으로 모터 위치 확인
             Spatula.SetCurrentsoftmax(softmax)
             Spatula.SetStiffness(pgain)
             sleep(0.1)
             Spatula.SetMotorPosition(goalConfiguration)
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
