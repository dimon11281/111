from enum import Enum, auto
from abc import ABC, abstractmethod


class Shoes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Specifications_Shoes(Enum):
    men = auto()
    women = auto()

class Types_Shoes(Enum):
    sneakers = auto()
    boots = auto()
    sandals = auto()
    shoes = auto()

class Colors_Shoes(Enum):
    black = auto()
    pink = auto()
    grey = auto()
    brown = auto()
    blue = auto()
    yellow = auto()

class List_type_shoes(Enum):
    type_shoes = "тип обуви"
    type_of_shoes = "вид обуви"
    color_shoes = "цвет"
    price_shoes = "цена"
    manufacturer_shoes = "производитель"
    size_shoes = "размер"






