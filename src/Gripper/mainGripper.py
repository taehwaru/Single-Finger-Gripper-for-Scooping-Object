import sys
import os
current_dir_gripper = os.path.dirname(os.path.abspath(__file__)) # 예를들어 부모 디렉토리를 만든다면 parent_dir = os.path.join(current_dir, '..') 이렇게도 가능
sys.path.append(current_dir_gripper)
from GRIPPER import Gripper
import TestMotion



######## select control signal ########
#controlSignal = 'testMotion'
#controlSignal = 'grab'
#controlSignal = 'smash'
controlSignal = 'testGetEncoder'
#controlSignal = 'testMotionStop'
#controlSignal = 'setIdleState'
######################################

def switchCase(case):
    if case == 'testMotion' :
        TestMotion.TestMotion()

    elif case == 'grab' :
        TestMotion.grab()
    
    elif case == 'smash' :
        TestMotion.smash()

    elif case == 'testGetEncoder' :
        TestMotion.TestGetEncoder()

    elif case == 'testMotionStop' :
        TestMotion.TestMotionStop()    
    
    elif case =='setIdleState' :
        Gripper.SetIdleState()

    else:
        print("Check the controlSignal")

# Gripper main is started
def mainGripper():
    switchCase(controlSignal)