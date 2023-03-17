import math


class Car:
    def __init__(self, model, tank_capacity, fuel_consumption, average_speed, type_car):
        self.model = model
        self.tank_capacity = tank_capacity
        self.fuel_consumption = fuel_consumption
        self.average_speed = average_speed
        self.type_car = type_car

    def info(self):
        print(f'Model_name: {self.model}')
        print(f'Type of car is: {self.type_car}')
        print(f'Tank capacity {self.tank_capacity}')
        print(f'Fuel consumption: {self.fuel_consumption}')
        print(f'Average speed: {self.average_speed}')

    def max_way(self):
        print(f'The car can drive {math.floor((self.tank_capacity / self.fuel_consumption) * self.average_speed)} km')

class Bus(Car):
    def __init__(self, model, tank_capacity, fuel_consumption, average_speed, type_car, occupancy):
        super().__init__(model, tank_capacity, fuel_consumption, average_speed, type_car)
        self.occupancy = occupancy
    def info(self):
        super().info()
        print(f'The bus can accommodate {self.occupancy} passengers')

    def max_way(self):
        print(f'The bus can go {math.ceil((self.tank_capacity / self.fuel_consumption) * self.average_speed )} km on one tank of gasoline')

    def ratio(self):
        print(f'Ratio= {math.ceil(self.occupancy /  (250 / self.fuel_consumption ))} ')

class Truck(Bus):
    def __init__(self, model, tank_capacity, fuel_consumption, average_speed, type_car, occupancy, speed_advantage):
        super().__init__(model, tank_capacity, fuel_consumption, average_speed, type_car, occupancy)

        self.tank_capacity += self.occupancy
        self.speed_advantage = speed_advantage
        self.average_speed += self.speed_advantage

    def info(self):
        super().info()
        print(f'This truck can go  {self.speed_advantage + self.average_speed} km/min faster then a bus')
        print(f'The truck can accommodate {self.occupancy} weights')


    def max_way(self):
        print(f'The bus can go {math.ceil((self.tank_capacity / self.fuel_consumption) * self.average_speed )} km on one tank of gasoline')

    def ratio(self):
        print(f'Ratio= {math.ceil(self.occupancy / (250 / self.fuel_consumption ))} ')






car = Car('Honda', 70, 6, 61, 'SUV')
car.info()
car.max_way()
print('-----')



bus = Bus('Volgabus', 95, 30, 65, 'Passenger', 80)
bus.info()
bus.max_way()
bus.ratio()

truck = Truck('Man', 350, 16, 80, 'All-metal', 2000, 20)
truck.info()
truck.max_way()
truck.ratio()
print('-----')