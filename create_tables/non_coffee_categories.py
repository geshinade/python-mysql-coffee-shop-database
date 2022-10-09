from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop",
    ) as connection:
       create_non_coffee_categories_query = """
       CREATE TABLE non_coffee_categories(
            id TINYINT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
            category  VARCHAR(40) NOT NULL,
            description  TINYTEXT,
            image  VARCHAR(45) NOT NULL,
            PRIMARY KEY (id),
            UNIQUE KEY category (category)
       ) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
       """
       with connection.cursor() as cursor:
           cursor.execute(create_non_coffee_categories_query)
           connection.commit()
except Error as e:
    print(e)