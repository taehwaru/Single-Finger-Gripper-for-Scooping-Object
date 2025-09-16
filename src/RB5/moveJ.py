import rbpodo as rb
import numpy as np


def _main():
    robot = rb.Cobot("192.168.0.25")
    rc = rb.ResponseCollector()

    try:
        robot.set_operation_mode(rc, rb.OperationMode.Real)
        rc = rc.error().throw_if_not_empty()

        joint = np.array([-90, 6,140, -53, 90, 0])
        robot.move_j(rc, joint, 60, 80)
        rc = rc.error().throw_if_not_empty()

        if robot.wait_for_move_started(rc, 0.5).is_success():
            robot.wait_for_move_finished(rc)
        rc = rc.error().throw_if_not_empty()
    finally:
        print('Exit')


if __name__ == '__main__':
    _main()

# https://github.com/RainbowRobotics/rbpodo/blob/main/examples/move_j.py 참고