from model.Type import Type
from abc import ABC


class CreativityGood(ABC):

    def __init__(self, name="", price=0, type=Type.WEAVING):
        self.name = name
        self.price = price
        self.type = type

    def __del__(self):
        print("Destructor was called")

    def __str__(self):
        return str(self.__dict__)
