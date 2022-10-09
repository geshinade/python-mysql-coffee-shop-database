from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop",
    ) as connection:
       create_order_contents_query = """
       CREATE TABLE order_contents(
            id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
            order_id INT(10) UNSIGNED NOT NULL,
            product_type enum('coffee','goodies') DEFAULT NULL,
            product_id MEDIUMINT(8) UNSIGNED NOT NULL,
            quantity TINYINT(3) UNSIGNED NOT NULL,
            price_per INT(10) UNSIGNED NOT NULL,
            ship_date date DEFAULT NULL,
            PRIMARY KEY (id),
            KEY ship_date (ship_date),
            KEY product_type (product_type, product_id),
            KEY (order_id)
       ) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
       """
       with connection.cursor() as cursor:
           cursor.execute(create_order_contents_query)
           connection.commit()
except Error as e:
    print(e)