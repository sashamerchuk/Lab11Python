from model.CreativityGood import CreativityGood
from model.Needle import Needle
from model.Thread import Thread
from model.Tissue import Tissue
from model.Type import Type
from manager.CreativityManager import CreativityManager


creativityGoodNeedle = Needle("Needle", 12, Type.WEAVING, 3)
creativityGoodThread = Thread("Thread", 7, Type.WEAVING, 10)
creativityGoodTissue = Tissue("Tissue", 10, Type.FISHING, 15, 26)

list_creativityGood = [creativityGoodNeedle,
                       creativityGoodThread, creativityGoodTissue]
manager = CreativityManager(list_creativityGood)
manager.print_creativity_good(manager.sort_by_name(list_creativityGood))
manager.print_creativity_good(manager.sort_by_price(list_creativityGood))
manager.print_creativity_good(manager.find_by_type(Type.FISHING))
