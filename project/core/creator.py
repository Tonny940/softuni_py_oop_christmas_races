from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class Creator:
    car_types = {
        'SportsCar': SportsCar,
        'MuscleCar': MuscleCar
    }

    def make_car_element(self, car_type: str, model: str, speed_limit: int):
        return self.__class__.car_types[car_type](model, speed_limit)
