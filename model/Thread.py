from model.Type import Type
from model.CreativityGood import CreativityGood


class Thread(CreativityGood):
    def __init__(self, name="", price=0, type=Type.WEAVING, length=0):
        super().__init__(name, price, type)
        self.length = length

    def __str__(self):
        return "Thread " + str(self.__dict__)
