from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
my_car = Car(36, 4)
my_car.go()
my_car.fill_up_tank()
need_car_fuel = my_car.fill_up_tank()
# print(need_car_fuel)
car_is_on_the_go = my_car.go()
# print(car_is_on_the_go)