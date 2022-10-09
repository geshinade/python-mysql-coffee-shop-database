from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop",
    ) as connection:
       create_general_coffees_query = """
       CREATE TABLE general_coffees(
            id TINYINT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
            category  VARCHAR(40) NOT NULL,
            description  TINYTEXT,
            image  VARCHAR(45) NOT NULL,
            PRIMARY KEY (id),
            UNIQUE KEY type (category)
       ) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
       """
       with connection.cursor() as cursor:
           cursor.execute(create_general_coffees_query)
           connection.commit()
except Error as e:
    print(e)