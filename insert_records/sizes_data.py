from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop",
    ) as connection:
       insert_sizes_query = """ 
       INSERT INTO sizes (size)
       VALUES
           ('2 oz. Sample'),
           ('Half Pound'),
           ('1 lb.'),
           ('2 lbs.'),
           ('5 lbs.')
       """
       with connection.cursor() as cursor:
           cursor.execute(insert_sizes_query)
           connection.commit()
except Error as e:
    print(e)