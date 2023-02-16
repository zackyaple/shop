import pymysqlrsors

#CREATE TABLE inventory(id INTERGER PRIMARY KEY, product_name TEXT, quantity INTEGER, UNIQUE(product_name), AUTO_INCREMENT=1)

#connect to database file on machine
connection = pymysql.connect(
        host='local_host',
        user='user',
        password='passwd',
        database='db',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)


def new_product(product, starting_quantity):
    with connection:
        with connection.cursor() as cursor:
            #create a new record
            sql = "INSERT INTO 'inventory' ('product_name', 'quantity') VALUES (%s, %s)"
            cursor.execute(sql, (product, starting_quantity))
        #connections arent autocommited by defualt, so we commit changes next
        connection.commit()
    connection.close()

def update(product, new_quantity):
    with connection:
        with connection.cursor() as cursor:
            #sets new quantity for product 
            sql = "UPDATE 'inventory' SET 'product_name'=%s  WHERE 'quantity'=%s"
            cursor.execute(sql, (product, new_quantity))
       #connections arent autocommited by defualt, so we commit changes next
        connection.commit()
    connection.close()

def remove_product(product):
    with connection:
        with connection.cursor() as cursor:
            #removes product from table
            sql = "DELETE FROM 'inventory' WHERE 'product'=%s"
            cursor.execute(sql, (product))
       #connections arent autocommited by defualt, so we commit changes next
        connection.commit()
    connection.close()

def current_stock(product):
    with connection:

        with connection.cursor() as cursor:
            #read a single record contianing same variable name to confirm change
            sql = "SELECT ONLY 'quantity' FROM 'inventory' WHERE 'product_name'=%S"
            cursor.execute(sql, (product))
            result = cursor.fetchone()
            return result
    connection.close()

def product_lookup(product):
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM 'inventory' WHERE 'product_name'=%s"
            cursor.execute(sql, (product))
            index = cursor.fetchone() 
            if index == []:
               return None
            else:
                result = print(bool(index))
                return result
    connection.close()
