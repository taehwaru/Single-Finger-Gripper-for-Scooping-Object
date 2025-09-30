from odrive.enums import *

class Actuator(object):

    def __init__(self, odrv, encoder_offset, direction, link_offset):
        self.odrv = odrv
        self.axis = odrv.axis0
        self.encoder_offset = encoder_offset
        self.direction = direction
        self.link_offset = link_offset
        self.setPointOffset = encoder_offset

    
    @property
    def encoder(self):
        posEstimate = self.odrv.axis0.pos_estimate
        calibratedEncoder = posEstimate
        return calibratedEncoder

    @property
    def motor_pos(self):
        tempEncoderValue = self.odrv.axis0.pos_estimate
        return 360 * (tempEncoderValue - self.setPointOffset)
        
   
    @motor_pos.setter
    def motor_pos(self, desiredMotorPosition):
        desiredSetPoint = desiredMotorPosition / 360 + self.setPointOffset
        self.axis.controller.input_pos = desiredSetPoint

    @property
    def theta(self):
        return self.motor_pos + self.link_offset

    @theta.setter
    def theta(self, setpoint):
        self.motor_pos = setpoint - self.link_offset

    @property
    def armed(self):
        return self.axis.current_state is AxisState.CLOSED_LOOP_CONTROL

    @armed.setter
    def armed(self, val):
        if val:  # arm
            self.axis.controller.config.input_mode = InputMode.PASSTHROUGH
            self.axis.requested_state = AxisState.CLOSED_LOOP_CONTROL
        else:  # disarm
            self.axis.requested_state = AxisState.IDLE

    @property
    def stiffness(self):
        return self.axis.controller.config.pos_gain

    @stiffness.setter
    def stiffness(self, val):
        self.axis.controller.config.pos_gain = val
    @property
    def current_soft_max(self):
        return self.axis.config.motor.current_soft_max
    
    @current_soft_max.setter
    def current_soft_max(self,val):
        self.axis.config.motor.current_soft_max=val

    @property
    def torque_soft_max(self):
        return self.axis.config.torque_soft_max
        
    @torque_soft_max.setter
    def torque_soft_max(self,val):
        self.axis.config.torque_soft_max=val


    @property
    def motor_vel(self):
        return self.axis.controller.input_vel

    @motor_vel.setter
    def motor_vel(self, val):
        self.axis.controller.input_vel = val

    @property
    def vel_gain(self):
        return self.axis.controller.config.vel_gain

    @vel_gain.setter
    def vel_gain(self, val):
        self.axis.controller.config.vel_gain = val

    @property
    def bandwidth(self):
        return self.axis.controller.config.input_filter_bandwidth

    @bandwidth.setter
    def bandwidth(self, val):
        self.axis.controller.config.input_filter_bandwidth = val

    def iBusValue(self):
        return self.odrv.ibus

    def clearErrors(self):
        self.odrv.clear_errors()