class Vehicle:
    def __init__(self, wheel_size, wheel_number):
        self.wheel_number = wheel_number
        self.wheel_size = wheel_size
    def go(self):
        return "vrrrrrrrooom!"
    def fill_up_tank(self):
        return "filling up!"
my_wheel = Vehicle(48, 4)
# print(my_wheel.wheel_number)
# print(my_wheel.wheel_size)
need_fuel = my_wheel.fill_up_tank()
# print(need_fuel)
need_to_go = my_wheel.go()
# print(need_to_go)