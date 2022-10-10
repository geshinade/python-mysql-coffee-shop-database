from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop",
    ) as connection:
       insert_sales_query = """ 
       INSERT INTO sales (product_type, product_id, price, start_date, end_date)
       VALUES
           ('goodies', 1, 500, '2013-08-16', '2013-10-31'),
           ('coffee', 7, 700, '2013-08-19', NULL),
           ('coffee', 9, 1300, '2013-08-19', '2013-08-26'),
           ('goodies', 2, 700, '2013-08-22', NULL),
           ('coffee', 8, 1300, '2013-08-22', '2013-10-31'),
           ('coffee', 10, 3000, '2013-08-22', '2013-11-30')
       """
       with connection.cursor() as cursor:
           cursor.execute(insert_sales_query)
           connection.commit()
except Error as e:
    print(e)