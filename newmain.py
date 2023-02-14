class shirts:
    pass
    def __init__(self, size):
        self.size = size
    def __str__(self):
        return f"{self.size}"

class hoodies:
    pass
    def __init__(self, size):
        self.size = size
    def __str__(self):
        return f"{self.size}"


class shorts:
    pass
    def __init__(self, size):
        self.size = size
    def __str__(self):
        return f"{self.size}"


class hats:
    pass
    def __init__(self, color):
        self.colors = color
    def __str__(self):
        return f"{self.colors}"

class item:
    pass
    def __init__(self, item)
        self.item = item
    for x in self.item:
        #ask size
    for shirts in self.item:
        shirt_size = ("AS","AM","AL","AXL")
        size = input("What Size?  ", shirt_size)




















import database
#import logging
#logging.basicConfig(formate='%(asctime)s - %(message)s'level=logging.INFO,)
#logginh.info('Order Logs')

def stock():
    edit = input("What would you like to do?Track Change  ")
    if edit == "Track":
         from pprint import pprint 
         pprint(database.items)
    if edit == "Change":
        item = input("what item?  ")
        if item in database.items:
            print(database.items[item])
            new = input("what is the new number")
            database.items[item] = new
            from pprint import pprint
            pprint(database.items[item])


def order():
    product = input("What type of product? SHIRTS,HOODIES,HATS,BAGS,PLATES  ")
    if product == "SHIRTS": 
        item = input("What size?")
        if item in database.sizes:
            database.sizes[item] -= 1
            print(database.sizes[item])
        else:
            print("Out Of Stock!")
    if product == "HOODIES":
        item = input("What size?")
        if item in database.sizes:
            database.sizes[item] -= 1
            print(database.sizes[item])
        else:
            print("Out Of Stock!")
    if product == "HATS":
            item = input("What color?")
            if item in database.hat_color:
                database.hat_color[item] -= 1
                print(database.hat_color[item])
            else:
                print("Out Of Stock!")
    if product == "BAGS":
        if product in database.items:
            database.items[BAGS] -= 1
            product == item  
            print(database.items[item])
        else:
            print("Out Of Stock!")
    if product == "PLATES":
        if product in database.items:
            database.items[PLATES] -= 1
            product == item
            print(database.items[item])
        else:
            print("Out Of Stock!")

    words = input("What writing? ")

    color = input("What colors? ").split()
    for x in color:
        if x in database.colors:
            database.colors[x] += 1
            print(database.colors[x])

    design = input("Which design? ")
#    for design in database.design:
 #       datbase.design[design] += 1
  #      print(databas.design[design]) 

    price = input("how much? ")

    print(item)
    print(words)
    print(color)
    print(design)
    print(price)



#database.sizes['YXL']
#print(database.sizes)
#from pprint import pprint 
#pprint(database.sizes)


task = input("What would you like to do? stock order   ")
if task == "stock":
    stock()
if task == "order":
    order()

