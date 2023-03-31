"""Fan Controller Class"""
from time import sleep
import time
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
        self.PWM_FREQUENCY = 1000
        self.__rpm = 0
        self.__duty_cycle = 0
        # Pins
        self.__pwm_pin = pwm_pin
        self.__tach_pin = tach_pin

        self.__start_time = 0

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.__pwm_pin, GPIO.OUT)
        GPIO.setup(self.__tach_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self.__pwm = GPIO.PWM(self.__pwm_pin, self.PWM_FREQUENCY)
        self.__pwm.start(0)
        GPIO.add_event_detect(
            self.__tach_pin, GPIO.FALLING, self.__fallen_trigger)

    def __del__(self):
        """
        Destructor for the FanController class.
        """
        self.__pwm.stop()
        GPIO.cleanup()

    def __fallen_trigger(self, channel):
        """
        A callback function for the tachometer falling edge.

        Args:
            channel (int): The GPIO channel number.
        """
        delta_time = time.time() - self.__start_time
        if delta_time < 0.005:
            return  # reject spuriously short pulses
        print("Delta Time: " + str(delta_time))
        freq = 1 / delta_time
        self.__rpm = (freq / 2) * 60
        self.__start_time = time.time()

    @ property
    def rpm(self):
        """
        Gets the current RPM value.

        Returns:
            int: The current RPM value.
        """
        return self.__rpm

    @ property
    def duty_cycle(self):
        """
        Gets the current duty cycle value.

        Returns:
            int: The current duty cycle value.
        """
        return self.__duty_cycle

    @ duty_cycle.setter
    def duty_cycle(self, value):
        """
        Sets the duty cycle value.

        Args:
            value (int): The desired duty cycle value (0-100).
        """
        print("Duty Cycle Set to: " + str(value))
        self.__pwm.ChangeDutyCycle(value)
        self.__duty_cycle = value
