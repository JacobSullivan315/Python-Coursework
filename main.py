import re
import string

def createfreqfile():
    with open('produce.txt') as f:
        item_list = f.read().split()
        produceSet = set(item_list)
    with open("frequency.txt", "w") as w:

        for item in produceSet:
            groceryItem = item
            groceryQuantity = str(item_list.count(item))
            groceryInfo = groceryItem + " " + groceryQuantity + "\n"
            w.write(groceryInfo)




createfreqfile()
