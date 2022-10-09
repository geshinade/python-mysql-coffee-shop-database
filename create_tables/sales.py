from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop",
    ) as connection:
       create_sales_query = """
       CREATE TABLE sales(
            id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
            product_type enum('coffee','goodies') DEFAULT NULL,
            product_id MEDIUMINT(8) UNSIGNED NOT NULL,
            price INT(10) UNSIGNED NOT NULL,
            start_date date NOT NULL,
            end_date date DEFAULT NULL,
            PRIMARY KEY (id),
            KEY start_date (start_date),
            KEY product_type (product_type, product_id)
       ) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
       """
       with connection.cursor() as cursor:
           cursor.execute(create_sales_query)
           connection.commit()
except Error as e:
    print(e)