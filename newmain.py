order = {'size':'x', 'design':'y', 'colors':'z', 'words':'w', 'price':'v'}
total_price = 0
items_ordered = []
designs_used = {} 
colors_used = {}
ordered_items = {}

for thing in order[]

    t = thing[0]

    if t == "size":
        for row in order[1:]:
            x = row[1]
            item_ordered.append(x)
        for i in items_ordered:
            if i in items_ordered:
                if i not in ordered_items:
                    ordered_items[i] =0
                ordered_items[i] += 1
                for i in ordered_items[0:]:
                    x = row[0]
                    z = sqlite.current_stock(x)
                    y = ordered_items[1:]
                    w = y -+ z
                    sqlite.update(x, w)

    elif t == "design":
        for row in order[1:]:
            y = row[1]
            designs_used[y] += 1

    elif t == "color":
        for row in order[1:]:
            z = row[1]   
            colors_used.append(z)

    elif t == "words":
        for row in order[1:]:
            w = row[1]

    elif t == "price":
        for row in order[1:]:
            v = row[1]
            v = int(v)
            total_price += v

def add_stock(product, new_stock):
    if x =  sqlite.currentstock(product) and y = int(new_stock):
        x += y = new_quantity
        sqlite.update(product, new_quantity)

def remove_stock(product, bad_stock):
    if x =  sqlite.currentstock(product) and y = int(bad_stock):
        x -= y = new_quantity
        sqlite.update(product, new_quantity)

def add_product(product, starting_quantity):
    if x =  sqlite.currentstock(product) == True:
        print("error product exist")
    else:
        y = starting_quantity
        w = product
        sqlite.new_product(x, y)

#def user_request(x):
#    if x == True:
#       inventory.x() 
#    elif x == NULL or x == "":
#        break

