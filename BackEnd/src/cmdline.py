""" Command line interface for the fan controller. """
from fan_controller import FanController


controller = FanController(37, 35)

controller.duty_cycle = 50

while True:
    new_duty_cycle = int(input("Enter new duty cycle: "))
    controller.duty_cycle = new_duty_cycle
    print("Setting duty cycle to " + str(new_duty_cycle))
    print("Current RPM: " + str(controller.rpm))
