from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop",
    ) as connection:
       create_non_coffee_products_query = """
       CREATE TABLE non_coffee_products(
            id MEDIUMINT(8) UNSIGNED NOT NULL AUTO_INCREMENT,
            non_coffee_category_id TINYINT(3) UNSIGNED NOT NULL,
            name VARCHAR(60) NOT NULL,
            description TINYTEXT,
            image VARCHAR(45) NOT NULL,
            price INT(10) UNSIGNED NOT NULL,
            stock MEDIUMINT(8) UNSIGNED NOT NULL DEFAULT '0',
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            KEY non_coffee_category_id (non_coffee_category_id)
       ) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
       """
       with connection.cursor() as cursor:
           cursor.execute(create_non_coffee_products_query)
           connection.commit()
except Error as e:
    print(e)