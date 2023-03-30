import random


class FanControllerMock():

    def __init__(self, pwm_pin, tach_pin):
        """
        Initialize the FanControllerMock object.

        Parameters:
        pwm_pin (int): The PWM pin number.
        tach_pin (int): The tachometer pin number.
        """
        self.__rpm = 0
        self.__duty_cycle = 0

    def update(self):
        """
        Update the RPM and duty cycle variables with random values.
        """
        self.__rpm = random.randint(0, 1000)

    @property
    def rpm(self):
        """
        Get the current RPM value.

        Returns:
        int: The current RPM value.
        """
        return self.__rpm

    @property
    def duty_cycle(self):
        """
        Get the current duty cycle value.

        Returns:
        int: The current duty cycle value.
        """
        return self.__duty_cycle

    @duty_cycle.setter
    def duty_cycle(self, value):
        """
        Set the duty cycle value.

        Parameters:
        value (int): The duty cycle value to set.
        """
        self.__duty_cycle = value
