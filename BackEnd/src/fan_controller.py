"""Fan Controller Class."""
import time
import lgpio


# Physical header pin to BCM GPIO mapping used by the old GPIO.BOARD code.
PHYSICAL_TO_BCM = {35: 19, 37: 26}


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
        self.__pwm_pin = PHYSICAL_TO_BCM.get(pwm_pin, pwm_pin)
        self.__tach_pin = PHYSICAL_TO_BCM.get(tach_pin, tach_pin)

        self.__start_time = 0
        self.__chip = lgpio.gpiochip_open(0)
        self.__callback = None

        lgpio.gpio_claim_output(self.__chip, 0, self.__pwm_pin, 0)
        lgpio.gpio_claim_input(self.__chip, lgpio.SET_PULL_UP, self.__tach_pin)
        self.__callback = lgpio.callback(
            self.__chip, self.__tach_pin, lgpio.FALLING_EDGE, self.__fallen_trigger
        )

        lgpio.tx_pwm(self.__chip, self.__pwm_pin, self.PWM_FREQUENCY, 0)

    def __del__(self):
        """
        Destructor for the FanController class.
        """
        if self.__callback is not None:
            self.__callback.cancel()
        if hasattr(self, "_FanController__chip"):
            lgpio.tx_pwm(self.__chip, self.__pwm_pin, 0, 0)
            lgpio.gpiochip_close(self.__chip)

    def __fallen_trigger(self, _chip, _gpio, _level, tick):
        """
        A callback function for the tachometer falling edge.

        Args:
            channel (int): The GPIO channel number.
        """
        delta_time = (tick - self.__start_time) / 1_000_000
        if delta_time < 0.005:
            return  # reject spuriously short pulses
        #print("Delta Time: " + str(delta_time))
        freq = 1 / delta_time
        self.__rpm = (freq / 2) * 60
        self.__start_time = tick

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
        if not 0 <= value <= 100:
            raise ValueError("Duty cycle must be between 0 and 100")
        lgpio.tx_pwm(self.__chip, self.__pwm_pin, self.PWM_FREQUENCY, value)
        self.__duty_cycle = value
