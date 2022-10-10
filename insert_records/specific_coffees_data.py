from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop",
    ) as connection:
       insert_specific_coffees_query = """ 
       INSERT INTO specific_coffees (general_coffee_id, size_id, caf_decaf, ground_whole, price, stock, date_created)
       VALUES
           (3, 1, 'caf', 'ground', 200, 20, NOW()),
           (3, 2, 'caf', 'ground', 450, 30, NOW()),
           (3, 2, 'decaf', 'ground', 500, 20, NOW()),
           (3, 3, 'caf', 'ground', 800, 50, NOW()),
           (3, 3, 'decaf', 'ground', 850, 20, NOW()),
           (3, 3, 'caf', 'whole', 750, 50, NOW()),
           (3, 3, 'decaf', 'whole', 800, 20, NOW()),
           (3, 4, 'caf', 'whole', 1500, 30, NOW()),
           (3, 4, 'decaf', 'whole', 1550, 15, NOW()),
           (3, 5, 'caf', 'whole', 3250, 5, NOW())
       """
       with connection.cursor() as cursor:
           cursor.execute(insert_specific_coffees_query)
           connection.commit()
except Error as e:
    print(e)