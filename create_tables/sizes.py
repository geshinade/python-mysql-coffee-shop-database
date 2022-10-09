from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop",
    ) as connection:
       create_sizes_query = """
       CREATE TABLE sizes(
            id TINYINT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
            size VARCHAR(40) NOT NULL,
            PRIMARY KEY (id),
            UNIQUE KEY size (size)
       ) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
       """
       with connection.cursor() as cursor:
           cursor.execute(create_sizes_query)
           connection.commit()
except Error as e:
    print(e)