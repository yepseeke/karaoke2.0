import sys
import pygame
from database import DataBase, Filter

if __name__ == '__main__':
    a = DataBase()
    f = Filter({'language': 'french'})
    print(a.filter_db(f))
