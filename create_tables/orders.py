from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop",
    ) as connection:
       create_orders_query = """
       CREATE TABLE orders(
            id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
            customer_id INT(10) UNSIGNED NOT NULL,
            total INT(10) UNSIGNED DEFAULT NULL,
            shipping INT(10) UNSIGNED NOT NULL DEFAULT 0,
            credit_card_number MEDIUMINT(4) ZEROFILL UNSIGNED NOT NULL,
            order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            KEY order_date (order_date),
            KEY customer_id (customer_id)
       ) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
       """
       with connection.cursor() as cursor:
           cursor.execute(create_orders_query)
           connection.commit()
except Error as e:
    print(e)