import sys
from time import sleep
import numpy as np
import Gripper
from GRIPPER.Gripper import FREQUENCY
from fivebar import ik_5bar_angles_deg
#from gripperendpoint import ik_from_gripper_tip
#from gripperendpoint import select_best_solution
import RB5
import numpy as np


# 로봇 객체 정의 (전역 변수 또는 클래스로 관리)
# ROBOT_IP = "192.168.0.25"
# robot = rb.Cobot(ROBOT_IP)
# rc = rb.ResponseCollector()






def TestGetEncoder():
    
    while True:
        pos = Gripper.GetMotorPosition()
        print(f"motor_pos : [{pos[0]:.4f}, {pos[1]:.4f},{pos[2]:.4f} ,{pos[3]:.4f} ]  deg")
        sleep(0.3)
         #0.3 간격으로 motor_pos값 받아서 출력


def TestCurrent():
    print("   [GRIPPER/ TEST CURRENT]")
    timeStep = 0.0
    readyPosition = [17, 27, -15, -24]
    Gripper.SetControlState()
    Gripper.SetMotorPosition(readyPosition)
    sleep(1.0)

    Gripper.SetStiffness([30,30,30,30])
    Gripper.SetVelocityGain([0.3,0.3,0.3,0.3])

    while(timeStep < 30):

        # print(Gripper.GetCurrent())
        # Gripper.sharedData = 3
        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)

    Gripper.SetIdleState()

def TestMotion():
    print("   [GRIPPER/ TEST MOTION]")
    pos = Gripper.GetMotorPosition()
    Gripper.SetControlState()
    Gripper.SetStiffness([50,50,50,50])
    Gripper.SetVelocityGain([0.2,0.2,0.2,0.2])
    # 원하는 좌표
    x=-80
    y=0
    shoulder1, shoulder2 = ik_5bar_angles_deg(x, y)
    position0=[shoulder1,shoulder2,0,0]
    Gripper.SetControlState()
    Gripper.SetMotorPosition(position0)
    sleep(0.3)    

    # x=70
    # y=0
    # shoulder1, shoulder2 = ik_5bar_angles_deg(x, y)
    # position0=[shoulder1,shoulder2,0,0]
    # Gripper.SetControlState()
    # Gripper.SetMotorPosition(position0)
    # sleep(0.3)  
    # #sleep(2)    

    # x=82
    # y=0
    # shoulder1, shoulder2 = ik_5bar_angles_deg(x, y)
    # position0=[shoulder1,shoulder2,0,0]
    # Gripper.SetControlState()
    # Gripper.SetMotorPosition(position0)
    # sleep(0.5)  
    # #sleep(2) 

    # x=0
    # y=82
    # shoulder1, shoulder2 = ik_5bar_angles_deg(x, y)
    # position0=[shoulder1,shoulder2,0,0]
    # Gripper.SetMotorPosition(position0)
    # sleep(0.3)  
    # #sleep(2)

    # x=0
    # y=50
    # shoulder1, shoulder2 = ik_5bar_angles_deg(x, y)
    # position0=[shoulder1,shoulder2,0,0]
    # Gripper.SetMotorPosition(position0)
    # sleep(0.3)  
    # #sleep(2)

    # x=0
    # y=82
    # shoulder1, shoulder2 = ik_5bar_angles_deg(x, y)
    # position0=[shoulder1,shoulder2,0,0]
    # Gripper.SetMotorPosition(position0)
    # sleep(0.5)  
    # #sleep(2)

    # x=-82
    # y=0
    # shoulder1, shoulder2 = ik_5bar_angles_deg(x, y)
    # position0=[shoulder1,shoulder2,0,0]
    # Gripper.SetMotorPosition(position0)
    # sleep(0.3)  
    # #sleep(2)

    # x=-70
    # y=0
    # shoulder1, shoulder2 = ik_5bar_angles_deg(x, y)
    # position0=[shoulder1,shoulder2,0,0]
    # Gripper.SetMotorPosition(position0)
    # sleep(0.3)  
    # #sleep(2)

    # x=-82
    # y=0
    # shoulder1, shoulder2 = ik_5bar_angles_deg(x, y)
    # position0=[shoulder1,shoulder2,0,0]
    # Gripper.SetMotorPosition(position0)
    # sleep(0.3)  
    #sleep(2)

    # x=50
    # y=0
    # shoulder1, shoulder2 = ik_5bar_angles_deg(x, y)
    # position0=[shoulder1,shoulder2,0,0]
    # Gripper.SetMotorPosition(position0)
    # sleep(2)

    # x=50
    # y=0
    # shoulder1, shoulder2 = ik_5bar_angles_deg(x, y)
    # position0=[shoulder1,shoulder2,0,0]
    # Gripper.SetMotorPosition(position0)
    # sleep(2)


    
    
    
def grab():
    
    Gripper.SetControlState()
    position0=[40.41,43,44.29,20.07]
    position1=[23.7,62.3,40.2,10]
    sensitivity=20  # 오차 범위 ±10
    sensi=sensitivity*0.5
    pos = Gripper.GetMotorPosition()
    # position9=[65,-19.75,pos[2],pos[3]]
    position10=[77.32,-53.85,52.55,20.38] # flat floor
    position12=[23.7,62.3,55.3,-11]
    position11=[84.7,-56.2,55.3,-11] # angled floor
    pgain=[100,100,50,50]
    cnt=0  
    while True:
        pos = Gripper.GetMotorPosition()
        print(f"motor_pos : [{pos[0]:.4f}, {pos[1]:.4f},{pos[2]:.4f} ,{pos[3]:.4f} ]  deg")
        if ((pos[0] < position1[0]-sensi or pos[0] > position1[0]+sensi or pos[1] < position1[1]-sensi or pos[1] > position1[1]+sensi 
            or pos[2] < position1[2]-sensi or pos[2] > position1[2]+sensi or pos[3] < position1[3]-sensi or pos[3] > position1[3]+sensi ) and (cnt==0)): # 0.3초 간격으로 모터 위치 확인
             Gripper.SetStiffness(pgain)
             Gripper.SetMotorPosition(position12)
             cnt+=1
             

        sleep(0.3)

    
            
def smash():
    x0=-50
    y0=50
    shoulder01, shoulder02 = ik_5bar_angles_deg(x0, y0)

    x1=60
    y1=10
    shoulder11, shoulder12 = ik_5bar_angles_deg(x1, y1)
    position1=[shoulder01,shoulder02,0,0] # start point
    Gripper.SetControlState()
    Gripper.SetMotorPosition(position1)
    sensitivity=10 # 오차 범위 ±5
    sensi=sensitivity*0.5
    pos = Gripper.GetMotorPosition()
    position12=[shoulder11, shoulder12,0,0]# end point
    pgain=[200,200,0,0]
    softmax=[4,4,0,0] # 원래 값 2, 원래값 2 
    torquemax=[2,2,0,0] # 원래 값 0.45, 원래값 0.45
    
    cnt=0  
    sleep(3)
    # robot = rb.Cobot(ROBOT_IP)
    # rc = rb.ResponseCollector()

    # robot.set_operation_mode(rc, rb.OperationMode.Simulation)
    # robot.set_speed_bar(rc, 0.5)

    # robot.move_pb_clear(rc)
    # robot.move_pb_add(rc, np.array([-110, -388, 180, 180, 0.1, 0.1]), 200.0, rb.BlendingOption.Ratio, 0.5)
    # robot.move_pb_add(rc, np.array([-110, -388, 125, 180, 0.1, 0.1]), 200.0, rb.BlendingOption.Ratio, 0.5)
    # robot.move_pb_add(rc, np.array([-110, -520, 130, -180, 0.1, 0]), 200.0, rb.BlendingOption.Ratio, 0.5)

    # robot.flush(rc)
    # rc = rc.error().throw_if_not_empty()
    # rc.clear()

    # robot.move_pb_run(rc, 800, rb.MovePBOption.Intended)
    # if robot.wait_for_move_started(rc, 0.1).type() == rb.ReturnType.Success:
    #     robot.wait_for_move_finished(rc)
    #     rc = rc.error().throw_if_not_empty()
    
    while True:
        pos = Gripper.GetMotorPosition()
        print(f"motor_pos : [{pos[0]:.4f}, {pos[1]:.4f},{pos[2]:.4f} ,{pos[3]:.4f} ]  deg")
        if (cnt==1):
            break
        if ((pos[0] < position1[0]-sensi or pos[0] > position1[0]+sensi or pos[1] < position1[1]-sensi or pos[1] > position1[1]+sensi ) and (cnt==0)): # 0.01초 간격으로 모터 위치 확인
            #  robot.stop(rc)
            #  rc.error().throw_if_not_empty()
            
            # 새로운 지점으로 이동
            #  robot.move_l(rc, np.array([-110, -600, 180, -180, 0.1, 0]), 200.0, rb.MoveOption.Abs)
            #  rc.error().throw_if_not_empty()
             Gripper.Settorquesoftmax(torquemax)
             Gripper.SetCurrentsoftmax(softmax)
             Gripper.SetStiffness(pgain)
             sleep(0.1)
             Gripper.SetMotorPosition(position12)
             sleep(5)
             cnt+=1
             
        sleep(0.01)
    Gripper.SetIdleState()
       
    

def TestMotionStop():
    print("   [GRIPPER/ TEST MOTION]")

    position1 = [14, 25, -16, -20]
    position2 = [-36, 100, 37, -100]
    position3 = [-35, 44, 39, -45]
    position4 = [35, 24, 5, -14]
    position5 = [-9, 23, -40, -15]

    Gripper.SetControlState()

    Gripper.SetStiffness([50,50,50,50])
    Gripper.SetVelocityGain([0.15,0.15,0.15,0.15])

    Gripper.SetMotorPosition(position1)
    # Gripper.SetIdleState()
