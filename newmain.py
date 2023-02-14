def addstock(product, num1):
    sum = current_stock(product) += num1
    update(product, sum)

def substock(product, num1):
    sum = current_stock(product) -= num1
    update(product, sum)

def updatestock(product, num1):
    x = product
    y =num1
    if x, y == True:
    update(x, y)

product-variable= product

def itemsale()
    for i in orders():
        if i == stock:
            stock -= 1

def itemsale(product, total):
    stock = seeql.current_stock(product)
    newstock = stock -= total
    return f"{product}{newstock}"


for x in orders:
    itemsale(x)
