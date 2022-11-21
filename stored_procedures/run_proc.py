from getpass import getpass
from mysql.connector import connect, Error


def call_find_items(x, p, y):

    db = x

    try:
        
        conn = connect(
                    host="localhost",
                    user = input("Enter username: "),
                    password = getpass("Enter password: "),
                    database = db
                )
            
        inp = p
        args = y

        cursor = conn.cursor()

        cursor.callproc(inp, args)

        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

call_find_items('coffee_shop', 'select_sale_items', [0])


