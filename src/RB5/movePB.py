import rbpodo as rb
import numpy as np

ROBOT_IP = "192.168.0.25"


def _main():
    try:
        robot = rb.Cobot(ROBOT_IP)
        rc = rb.ResponseCollector()
        #robot.set_speed_multiplier(rc, 1.0)
        # robot.set_operation_mode(rc, rb.OperationMode.Real)
        robot.set_speed_bar(rc, 1)
        # #robot.set_speed_acc_l(80,300)
        # robot.set_speed_multiplier(1)
        # robot.set_acc_multiplier(0.1)

        robot.move_pb_clear(rc)
        robot.move_pb_add(rc, np.array([-110.65, -388.68, 250, 180, 0.1, 0.1]), 2000.0, rb.BlendingOption.Ratio, 1)
        robot.move_pb_add(rc, np.array([-110.65, -388.68, 160, 180, 0.1, 0.1]), 2000.0, rb.BlendingOption.Ratio, 1)
        robot.move_pb_add(rc, np.array([-110.65, -520, 160, 180, 0.1, 0.1]), 2000.0, rb.BlendingOption.Ratio, 1)
        robot.move_pb_add(rc, np.array([-110.65, -600, 240, 180, 0.1, 0.1]), 2000.0, rb.BlendingOption.Ratio, 1)
        # robot.move_pb_add(rc, np.array([300, 300, 400, 0, 0, 0]), 400.0, rb.BlendingOption.Ratio, 0.5)
        # robot.move_pb_add(rc, np.array([0, 200, 400, 90, 0, 0]), 200.0, rb.BlendingOption.Ratio, 0.5)
        # robot.move_pb_add(rc, np.array([100, 200, 200, 90, 0, 0]), 200.0, rb.BlendingOption.Ratio, 0.5)
        # robot.move_pb_add(rc, np.array([100, 200, 200, 90, 0, 0]), 200.0, rb.BlendingOption.Ratio, 0.5)
        # **Important**
        # Before you start move, flush buffer to response collector to avoid unexpected behavior in 'wait' function
        robot.flush(rc)
        rc = rc.error().throw_if_not_empty()
        rc.clear()

        robot.move_pb_run(rc, 1000, rb.MovePBOption.Intended)
        if robot.wait_for_move_started(rc, 0.1).type() == rb.ReturnType.Success:
            robot.wait_for_move_finished(rc)
        rc = rc.error().throw_if_not_empty()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    _main()