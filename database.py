import csv
import json


class Filter:
    def __init__(self, filters):
        self.filter_list = []
        if 'singer' in filters:
            self.filter_list.append(lambda item: item.get('singer') == filters['singer'])
        if 'song' in filters:
            self.filter_list.append(lambda item: item.get('song') == filters['song'])
        if 'language' in filters:
            self.filter_list.append(lambda item: item.get('language') == filters['language'])
        if 'id' in filters:
            self.filter_list.append(lambda item: item.get('id') == filters['id'])

    def is_valid(self, item) -> bool:
        for my_filter in self.filter_list:
            if not my_filter(item):
                return False
        return True


class Singleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in Singleton.__instance:
            Singleton.__instance[cls] = cls.__new__(cls)
            Singleton.__instance[cls].__init__(*args, **kwargs)
        return Singleton.__instance[cls]


class DataBase(metaclass=Singleton):
    def __init__(self):
        data_path = 'data/list.json'
        with open(data_path, 'r', encoding='UTF-8') as file:
            self.data = json.load(file)

    def filter_db(self, filters: Filter):
        filtered_list = []
        for element in self.data:
            if filters.is_valid(element):
                filtered_list.append(element)

        return filtered_list

    def get_data(self):
        return self.data
