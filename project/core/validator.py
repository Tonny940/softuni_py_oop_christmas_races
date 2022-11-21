class Validator:
    @staticmethod
    def str_is_less_then_four(text, error_message):
        if len(text) < 4:
            raise ValueError(error_message)

    @staticmethod
    def raise_if_value_is_out_of_range(
            value,
            min_value,
            max_value,
            error_message):
        if value < min_value or value > max_value:
            raise ValueError(error_message)

    @staticmethod
    def raise_if_is_empty_or_whitespace_str(text, error_message):
        if text.strip() == '':
            raise ValueError(error_message)

    @staticmethod
    def check_for_driver(driver_name, list_with_drivers, error_message):
        for driver in list_with_drivers:
            if driver.name == driver_name:
                return driver
        raise Exception(error_message)

    @staticmethod
    def check_for_free_car(car_type, list_with_cars, error_message):
        for car in reversed(list_with_cars):
            if not car.is_taken and \
                    car.__class__.__name__ == car_type:
                return car
        raise Exception(error_message)

    @staticmethod
    def check_for_race(race_name, races, error_message):
        for race in races:
            if race.name == race_name:
                return race
        raise Exception(error_message)
