from model.Type import Type


class CreativityManager:
    def __init__(self, list_creativity_good=None):
        self.list_creativity_good = list_creativity_good

    def find_by_type(self, type=Type.WEAVING):
        return list(filter(lambda creativity: creativity.type == type.WEAVING, self.list_creativity_good))

    def sort_by_price(self, price, reverse=False):
        return sorted(self.list_creativity_good, key=lambda creativity: creativity.price, reverse=reverse)

    def sort_by_name(self, name, reverse=True):
        return sorted(self.list_creativity_good, key=lambda creativity: creativity.name, reverse=reverse)

    def print_creativity_good(self, creativity):
        for i in creativity:
            print(i)
           
