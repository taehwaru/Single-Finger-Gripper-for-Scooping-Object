import sys
import os
current_dir_gripper = os.path.dirname(os.path.abspath(__file__)) # 예를들어 부모 디렉토리를 만든다면 parent_dir = os.path.join(current_dir, '..') 이렇게도 가능
sys.path.append(current_dir_gripper)
#from GRIPPER import Gripper
from GRIPPER import Spatula
import TestMotion

######## select control signal ########
#controlSignal = 'testFinger'
#controlSignal = 'testEdge'
controlSignal = 'Scoop'
#controlSignal = 'testGetEncoder'
#controlSignal = 'testMotionStop'
######################################

def switchCase(case):
    if case == 'testFinger' :
        TestMotion.Test_fingerTip()

    elif case == 'testEdge' :
        TestMotion.Test_linkageEdge()

    elif case == 'Scoop' :
        TestMotion.Scoop()

    elif case == 'testGetEncoder' :
        TestMotion.TestGetEncoder()

    elif case == 'testMotionStop' :
        TestMotion.TestMotionStop()    

    else:
        print("Check the controlSignal")

# Gripper main is started
def mainGripper():
    switchCase(controlSignal)