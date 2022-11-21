from project.core.creator import Creator
from project.core.validator import Validator
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []
        self.creator = Creator()

    valid_car_types = ['MuscleCar', 'SportsCar']

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.valid_car_types:
            return
        if any(car.model == model for car in self.cars):
            raise Exception(f"Car {model} is already created!")

        car = self.creator.make_car_element(car_type, model, speed_limit)
        self.cars.append(car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if any(driver.name == driver_name for driver in self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if any(race.name == race_name for race in self.races):
            raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = Validator.check_for_driver(
            driver_name,
            self.drivers,
            f"Driver {driver_name} could not be found!")

        car = Validator.check_for_free_car(
            car_type,
            self.cars,
            f"Car {car_type} could not be found!")

        if driver.car is None:
            car.is_taken = True
            driver.car = car
            return f"Driver {driver.name} chose the car {car.model}."

        else:
            old_model = driver.car
            old_model.is_taken = False

            driver.car = car
            car.is_taken = True
            return f"Driver {driver.name} changed his car from {old_model.model} to {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = Validator.check_for_race(
            race_name,
            self.races,
            f"Race {race_name} could not be found!")

        driver = Validator.check_for_driver(
            driver_name,
            self.drivers,
            f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver.name} could not participate in the race!")

        if any(dr.name == driver.name for dr in race.drivers):
            return f"Driver {driver.name} is already added in {race.name} race."
        else:
            race.drivers.append(driver)
            return f"Driver {driver.name} added in {race.name} race."

    def start_race(self, race_name: str):

        race = Validator.check_for_race(
            race_name,
            self.races,
            f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race.name} cannot start with less than 3 participants!")

        winners = sorted(race.drivers, key=lambda d: d.car.speed_limit, reverse=True)[:3]
        result = []

        for driver in winners:
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} "
                          f"race with a speed of {driver.car.speed_limit}.")
        return '\n'.join(result)
