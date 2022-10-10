from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop",
    ) as connection:
       insert_non_coffee_products_query = """ 
       INSERT INTO non_coffee_products (non_coffee_category_id, name, description, image, price, stock, date_created)
       VALUES
           (
             3, 
             'Pretty Flower Coffee Mug', 
             'A pretty coffee mug with a flower design on a white background.', 
             'd9996aee5639209b3fb618b07e10a34b27baad12.jpg', 
             650, 
             100, 
             NOW()
           ),
           (
             3, 
             'Red Dragon Mug', 
             'An elaborate, painted gold dragon on a red background. With partially detached, fancy handle.', 
             '847a1a3bef0fb5c2f2299b06dd63669000f5c6c4.jpg', 
             795, 
             4, 
             NOW()
           )
       """
       with connection.cursor() as cursor:
           cursor.execute(insert_non_coffee_products_query)
           connection.commit()
except Error as e:
    print(e)