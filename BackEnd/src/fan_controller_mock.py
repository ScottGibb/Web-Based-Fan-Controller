"""A mock class for the FanController class."""
import random


class FanControllerMock():
    """A mock class for the FanController class.
    """

    def __init__(self):
        """
        Initialize the FanControllerMock object.
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
