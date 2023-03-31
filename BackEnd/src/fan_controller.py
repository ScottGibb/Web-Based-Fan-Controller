"""Fan Controller Class"""
import random
import threading
from time import sleep
from RPi import GPIO


class FanController():
    """
    A class for controlling a fan using PWM and a tachometer.

    Args:
        pwm_pin (int): The GPIO pin number for PWM control.
        tach_pin (int): The GPIO pin number for tachometer feedback.
    """

    def __init__(self, pwm_pin, tach_pin):
        """
        Initializes a new instance of the FanController class.

        Args:
            pwm_pin (int): The GPIO pin number for PWM control.
            tach_pin (int): The GPIO pin number for tachometer feedback.
        """
        self.__rpm = 0
        self.__duty_cycle = 0
        self.__alive = False
        self.__pwm_pin = pwm_pin
        self.__tach_pin = tach_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__pwm_pin, GPIO.OUT)
        GPIO.setup(self.__tach_pin, GPIO.IN)

        self.__pwm = GPIO.PWM(self.__pwm_pin, 100)
        self.__pwm.start(0)

        thread = threading.Thread(target=self.__update_loop, args=())
        thread.start()

    def __update_loop(self):
        """
        A private method to continuously update the RPM value.
        """
        self.__alive = True
        while self.__alive:
            self.__rpm = random.randint(0, 1000)
            sleep(0.5)

    @property
    def rpm(self):
        """
        Gets the current RPM value.

        Returns:
            int: The current RPM value.
        """
        return self.__rpm

    @property
    def duty_cycle(self):
        """
        Gets the current duty cycle value.

        Returns:
            int: The current duty cycle value.
        """
        return self.__duty_cycle

    @duty_cycle.setter
    def duty_cycle(self, value):
        """
        Sets the duty cycle value.

        Args:
            value (int): The desired duty cycle value (0-100).
        """
        self.__duty_cycle = value
        print("Duty Cycle Set to: " + str(value))
        self.__pwm.ChangeDutyCycle(value)
