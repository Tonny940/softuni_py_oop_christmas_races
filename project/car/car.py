from abc import ABC, abstractmethod

from project.core.validator import Validator


class Car(ABC):
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validator.str_is_less_then_four(value, f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        Validator.raise_if_value_is_out_of_range(
            value,
            self.min_limit,
            self.max_limit,
            f"Invalid speed limit! Must be between {self.min_limit} and {self.max_limit}!")

        self.__speed_limit = value

    @property
    @abstractmethod
    def min_limit(self):
        pass

    @property
    @abstractmethod
    def max_limit(self):
        pass
