from getpass import getpass
from mysql.connector import connect, Error


connection = connect(
	    host="localhost",
		user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop"
	  )
select_categories_sp_query = """
CREATE PROCEDURE select_categories (type VARCHAR(7))
BEGIN
    IF type = 'coffee' THEN
    SELECT * FROM general_coffees ORDER by category;
    ELSEIF type = 'goodies' THEN
    SELECT * FROM non_coffee_categories ORDER by category;
END IF;
END  
"""
cur = connection.cursor()
cur.execute(select_categories_sp_query)
connection.commit()