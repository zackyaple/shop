
def addstock():
    product = #name of new product
    num1 = #of stock to add
    if sqlite.product_lookup(product) == True:
        while True:
           old_stock = sqlite.current_stock(product)
           new_stock = 0ld_stock += num1
           sqlite.update(product, new_stock)
           break
    else:
        print("The product dosent exists")

def substock():
    product = #name of product
    num1 = #of stock to subtract
    if sqlite.product_lookup(product) == True:
        while True:
           old_stock = sqlite.current_stock(product)
           new_stock = 0ld_stock -= num1
           sqlite.update(product, new_stock)
           break
    else:
        print("The product dosent exists")


