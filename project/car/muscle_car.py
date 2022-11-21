from project.car.car import Car


class MuscleCar(Car):
    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

    @property
    def min_limit(self):
        return 250

    @property
    def max_limit(self):
        return 450