from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop",
    ) as connection:
       create_customers_query = """
       CREATE TABLE customers(
            id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
            email VARCHAR(80) NOT NULL,
            first_name VARCHAR(20) NOT NULL,
            last_name VARCHAR(40) NOT NULL,
            address1 VARCHAR(80) NOT NULL,
            address2 VARCHAR(80) DEFAULT NULL,
            city VARCHAR(60) NOT NULL,
            state char(2) NOT NULL,
            zip MEDIUMINT(5) UNSIGNED ZEROFILL NOT NULL,
            phone CHAR(10) NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            KEY email (email)
       ) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
       """
       with connection.cursor() as cursor:
           cursor.execute(create_customers_query)
           connection.commit()
except Error as e:
    print(e)