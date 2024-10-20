import os
from typing import Union

from src.models import Car, CarFullInfo, CarStatus, Model, ModelSaleStats, Sale


class DbIndex:
    def __init__(self, id: str, symbol_position: str):
        self.id: str = id
        self.symbol_position: str = symbol_position

class CarService:

    def __init__(self):
        self.root_dir = '/data'
        self.models_file_name = 'models.txt'
        self.models_index_file_name = 'models_index.txt'
        self.models_index: Union[list[DbIndex], list] = self._add_index_in_cache_db(self._join_dir_vs_file(self.root_dir,self.models_file_name))
        self.cars_file_name = 'cars.txt'
        self.cars_index_file_name = 'cars_index.txt'
        self.cars_index: Union[list[DbIndex], list] = self._add_index_in_cache_db(self._join_dir_vs_file(self.root_dir,self.cars_file_name))

    @staticmethod
    def _join_dir_vs_file(dir_path: str, file_name: str) -> str:
        return '/'.join([dir_path, file_name])

    @staticmethod
    def _add_index_in_cache_db(table_dir) -> list:
        cache_index: list = []
        if os.path.exists(table_dir):
            with open(table_dir, 'r') as table_file:
                lines: list[str] = table_file.readlines()
                split_lines = [line.strip().split(',') for line in lines]
                print(f'{split_lines=}')
                return [DbIndex(id=s_line[0], symbol_position=s_line[1]) for s_line in split_lines]
        return cache_index

    # Задание 1. Сохранение автомобилей и моделей
    def add_model(self, model: Model) -> Model:
        with open(self._join_dir_vs_file(self.root_dir,self.models_file_name), 'a') as model_file:
            models_string: str = f'{model.id},{model.name},{model.brand}\n'.ljust(500)
            model_file.write(models_string)

        model_index: DbIndex = DbIndex(id=model.index(), symbol_position=str(len(self.models_index)))

        self.models_index.append(model_index)
        self.models_index.sort(key=lambda x: x.id)

        with open(self._join_dir_vs_file(self.root_dir,self.models_index_file_name), 'w') as model_index_file:
            for model_index in self.models_index:
                string_index_model: str = f'{model_index.id},{model_index.symbol_position}\n'.ljust(50)
                model_index_file.write(string_index_model)
        return model

    # Задание 1. Сохранение автомобилей и моделей
    def add_car(self, car: Car) -> Car:
        with open(self._join_dir_vs_file(self.root_dir,self.cars_file_name), 'a') as cars_file:
            cars_string: str = f'{car.vin},{car.model},{car.price},{car.date_start},{car.status}\n'.ljust(500)
            cars_file.write(cars_string)

        car_index: DbIndex = DbIndex(id=car.index(), symbol_position=str(len(self.cars_index)))
        self.cars_index.append(car_index)
        self.cars_index.sort(key=lambda x: x.id)

        with open(self._join_dir_vs_file(self.root_dir,self.cars_index_file_name), 'w') as cars_index_file:
            for cars_index in self.cars_index:
                string_index_model: str = f'{cars_index.id},{cars_index.symbol_position}\n'.ljust(50)
                cars_index_file.write(string_index_model)
        return car

    # Задание 2. Сохранение продаж.
    def sell_car(self, sale: Sale) -> Car:
        raise NotImplementedError

    # Задание 3. Доступные к продаже
    def get_cars(self, status: CarStatus) -> list[Car]:
        raise NotImplementedError

    # Задание 4. Детальная информация
    def get_car_info(self, vin: str) -> CarFullInfo | None:
        raise NotImplementedError

    # Задание 5. Обновление ключевого поля
    def update_vin(self, vin: str, new_vin: str) -> Car:
        raise NotImplementedError

    # Задание 6. Удаление продажи
    def revert_sale(self, sales_number: str) -> Car:
        raise NotImplementedError

    # Задание 7. Самые продаваемые модели
    def top_models_by_sales(self) -> list[ModelSaleStats]:
        raise NotImplementedError
