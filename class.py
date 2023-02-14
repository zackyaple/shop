class items:
    def __init__(self, item):
        self.item = item
        clothing = clothing.printinfo
        hat = hats.printinfo
        plate = plates.printinfo
    
class clothing(items):
#    def __init__(self, item, size):
#        self.item = item
#        self.size = size
    def printinfo(self):
        print(self.item)
class hats():
    pass
    def __init__(self, item, color):
        self.item = item
        self.color = color
    def printinfo(self):
        print(self.item + self.color)
class plates():
    pass
    def __init__(self, item):
        self.item = item
    def printinfo(self):
        print(self.item)

x = input("item?  ")
order = items(x)
if x == "shirt" or "hoodie":
    order.clothing()
elif x == "hats":
    order.hat
elif x == "plates":
    order.plate
else:
    print("error")
