from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database="coffee_shop",
    ) as connection:
       insert_general_coffees_query = """ 
       INSERT INTO general_coffees (category, description, image)
       VALUES
           (
            'Original Blend', 
            'Our original blend, featuring a quality mixture of bean and a medium roast for a rich color and smooth flavor.', 
            'original_coffee.jpg'
           ),
		   (
            'Dark Roast', 
            'Our darkest, non-espresso roast, with a full flavor and a slightly bitter aftertaste.', 
            'dark_roast.jpg'
           ),
		   (
            'Kona', 
            'A real treat! Kona coffee, fresh from the lush mountains of Hawaii. Smooth in flavor and perfectly roasted!', 
            'kona.jpg'
           )
       """
       with connection.cursor() as cursor:
           cursor.execute(insert_general_coffees_query)
           connection.commit()
except Error as e:
    print(e)