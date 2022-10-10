from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop"
    ) as connection:
       insert_customers_query = """ 
       INSERT INTO customers 
       (email, `first_name`, `last_name`, address1, address2, `city`, `state`, `zip`, phone, date_created)
       VALUES
           ('johndoe@example.com', 'John', 'Doe', 'John Doe Street', NULL, 'Fantasy Island', 'FI', '12345', '12345678', NOW()),
           ('willville@example.com', 'William', 'Ville', 'William Ville Street', NULL, 'WillVille', 'WV', '23456', '8765432', NOW())
       """
       with connection.cursor() as cursor:
           cursor.execute(insert_customers_query)
           connection.commit()
except Error as e:
    print(e)