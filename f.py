product = ["shirt", "hoodie", "hat", "plate"]
colors = ["red", "blue", "black", "white", "pink"]
sizes = ["small", "med", "large", "xl"]
class SHIRTS():
    def item(self):
        size = input("What size?  ")
        print("The size is " + size)

class HOODIES():
    def item(self, size):
        print("The size is " + size)

class HATS():
    def item(self, size):
        print("The size is " + size)

class PLATES():
    def item(self, size):
        print("The size is " + size)

class items:
            shirt = SHIRTS.item
            hoodie = HOODIES.item
            hat = HATS.item
            plate = PLATES.item

order = items("shirt")
#order.fuck()
#order.shirt()
# make shirt variable

x = input("item?  ")
    order = items()
    if x == "shirt" or "hoodie":
        order.clothing()
    elif x == "hats":
        order.hat
    elif x == "plates":
        order.plate
    else:
        print("error")
    
class clothing():
    def __init__(self, item, size):
        self.item = item
        self.size = size
    def printinfo(self)
        print(self.item + self.size)
class hats():
    def __init__(self, item, color):
        self.item = item
        self.color = color
    def printinfo(self)
        print(self.item + self.color)
class plates():
    def __init__(self, item):
        self.item = item
    def printinfo(self)
        print(self.item)
class items:
            clothing = clothing.item
            hat = HATS.item
            plate = PLATES.item


