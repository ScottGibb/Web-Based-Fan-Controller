from fan_controller import FanController


controller = FanController(37,35)

controller.duty_cycle = 50
print(controller.rpm)