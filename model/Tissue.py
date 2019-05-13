from model.Type import Type
from model.CreativityGood import CreativityGood


class Tissue(CreativityGood):
    def __init__(self, name="", price=0, type=Type.WEAVING, width=0, height=0):
        super().__init__(name, price, type)
        self.width = width
        self.height = height

    def __str__(self):
        return "Tissue " + str(self.__dict__)
