from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop",
    ) as connection:
       create_specific_coffees_query = """
       CREATE TABLE specific_coffees(
            id MEDIUMINT(8) UNSIGNED NOT NULL AUTO_INCREMENT,
            general_coffee_id TINYINT(3) UNSIGNED NOT NULL,
            size_id TINYINT(3) UNSIGNED NOT NULL,
            caf_decaf enum('caf','decaf') DEFAULT NULL,
            ground_whole enum('ground','whole') DEFAULT NULL,
            price INT(10) UNSIGNED NOT NULL,
            stock MEDIUMINT(8) UNSIGNED NOT NULL DEFAULT '0',
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            KEY general_coffee_id (general_coffee_id),
            KEY size (size_id)
       ) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
       """
       with connection.cursor() as cursor:
           cursor.execute(create_specific_coffees_query)
           connection.commit()
except Error as e:
    print(e)