import random
import threading
from time import sleep


class FanController():

    def __init__(self, pwm_pin, tach_pin) -> None:
        self.__rpm = 0
        self.__duty_cycle = 0
        self.__alive = False
        thread = threading.Thread(target=self.__update_loop, args=())
        thread.start()

    def __update_loop(self):
        self.__alive = True
        while (self.__alive):
            self.__rpm = random.randint(0, 1000)
            sleep(0.5)

    @property
    def rpm(self):
        return self.__rpm

    @property
    def duty_cycle(self):
        return self.__duty_cycle

    @duty_cycle.setter
    def duty_cycle(self, value):
        self.__duty_cycle = value
        print("Duty Cycle Set to: " + str(value))
