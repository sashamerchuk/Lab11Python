from model.Type import Type
from model.CreativityGood import CreativityGood


class Needle(CreativityGood):
    def __init__(self, name="", price=0, type=Type.WEAVING, diameter=0):
        super().__init__(name, price, type)
        self.diameter = diameter

    def __str__(self):
        return "Needle " + str(self.__dict__)
