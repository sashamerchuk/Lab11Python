from model.CreativityGood import CreativityGood
from model.Needle import Needle
from model.Thread import Thread
from model.Tissue import Tissue
from model.Type import Type
from manager.CreativityManager import CreativityManager
def main():
    creativity_good_needle = Needle("Needle", 12, Type.WEAVING, 3)
    creativity_good_thread = Thread("Thread", 7, Type.WEAVING, 10)
    creativity_good_tissue = Tissue("Tissue", 10, Type.WEAVING, 15, 26)
    list_creativityGood = [creativity_good_needle,creativity_good_thread, creativity_good_tissue]
    manager = CreativityManager(list_creativityGood)
    manager.print_creativity_good(manager.sort_by_name(list_creativityGood))
    print('\n')
    manager.print_creativity_good(manager.sort_by_price(list_creativityGood))
    print('\n')
    manager.print_creativity_good(manager.find_by_type(Type.FISHING))
    return list_creativityGood
main()