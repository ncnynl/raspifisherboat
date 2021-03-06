# Motors . skid steering - control two motors

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor


class Motors:
    def __init__(self, brainz=None, verbose=False):
        self.verbose = verbose
        self.brainz = brainz
        self.started = False
        self.cycle_time = 0

    def __print(self, str):
        if self.verbose:
            print ( str)

    def start(self):
        self.started = True
        self.mh = Adafruit_MotorHAT(addr=0x60)
        self.leftMotor = self.mh.getMotor(1)
        self.leftMotor.setSpeed(0)
        self.leftMotor.run(Adafruit_MotorHAT.FORWARD)
        self.leftMotor.run(Adafruit_MotorHAT.RELEASE)
        self.rightMotor = self.mh.getMotor(2)
        self.rightMotor.setSpeed(0)
        self.rightMotor.run(Adafruit_MotorHAT.FORWARD)
        self.rightMotor.run(Adafruit_MotorHAT.RELEASE)

    def stop(self):
        self.leftMotor.run(Adafruit_MotorHAT.RELEASE)
        self.rightMotor.run(Adafruit_MotorHAT.RELEASE)

    def tick(self,interval):

        if not self.started:
            return
        self.cycle_time += interval
        self.set_speed()

    def set_speed(self):
        new_speed = 0
        self.__print("Speed:" + str(self.brainz.speed))
        if self.brainz.low_speed_percent < 1:
            new_speed = float(self.brainz.speed)
        else:
            if self.cycle_time > float(self.brainz.speed_change_cycle):
                self.cycle_time = 0
            if self.cycle_time > int(self.brainz.speed_motors_full_percent) *  float(self.brainz.speed_change_cycle) / 100.0:
                new_speed = float(self.brainz.speed) * int(self.brainz.low_speed_percent) / 100.0
            else:
                new_speed = float(self.brainz.speed)

        # Divide speed to two motors

        new_right_motor_speed = min(1.0, new_speed * (1.0 - float(self.brainz.turn)))
        new_left_motor_speed = min(1.0, new_speed * (1.0 + float(self.brainz.turn)))

        self.rightMotor.run(Adafruit_MotorHAT.FORWARD)
        self.leftMotor.run(Adafruit_MotorHAT.FORWARD)
        self.leftMotor.setSpeed(int(new_left_motor_speed * 255) )
        self.rightMotor.setSpeed(int(new_right_motor_speed * 255))

        self.__print("Set speedright:" + str(int(new_right_motor_speed * 255)) + " " + str(int(new_left_motor_speed * 255)))

