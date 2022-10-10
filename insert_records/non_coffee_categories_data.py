from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop",
    ) as connection:
       insert_non_coffee_categories_query = """ 
       INSERT INTO non_coffee_categories (category, description, image)
       VALUES
           (
            'Edibles', 
            'A wonderful assortment of goodies to eat. Includes biscotti, baklava, lemon bars, and more!', 
            'goodies.jpg'
           ),
           (
             'Gift Baskets', 
             'Gift baskets for any occasion! Including our many coffees and other goodies.', 
             'gift_basket.jpg'
           ),
           (
             'Mugs', 
             'A selection of lovely mugs for enjoying your coffee, tea, hot cocoa or other hot beverages.', 
             '781426_32573620.jpg'
           ),
           ( 'Books', 
             'Our recommended books about coffee, goodies', 
             'books.jpg')
       """
       with connection.cursor() as cursor:
           cursor.execute(insert_non_coffee_categories_query)
           connection.commit()
except Error as e:
    print(e)