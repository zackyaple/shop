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

#def user_request(x):
#    if x == True:
#       inventory.x() 
#    elif x == NULL or x == "":
#        break

