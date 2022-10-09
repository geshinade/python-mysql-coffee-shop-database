from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop",
    ) as connection:
       create_carts_query = """
       CREATE TABLE carts(
            id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
            user_session_id CHAR(32) NOT NULL,
            product_type enum('coffee','goodies') NOT NULL,
            product_id MEDIUMINT(8) UNSIGNED NOT NULL,
            quantity TINYINT(3) UNSIGNED NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_modified TIMESTAMP NOT NULL DEFAULT '0000-00-00 00:00:00',
            PRIMARY KEY (id),
            KEY product_type (product_type, product_id),
            KEY user_session_id (user_session_id)
       ) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
       """
       with connection.cursor() as cursor:
           cursor.execute(create_carts_query)
           connection.commit()
except Error as e:
    print(e)