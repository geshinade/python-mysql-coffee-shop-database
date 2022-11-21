from getpass import getpass
from mysql.connector import connect, Error


def call_find_all_sp():
    try:
        
        conn = connect(
                    host="localhost",
                    user = input("Enter username: "),
                    password = getpass("Enter password: "),
                    database="coffee_shop"
                )
        

        args = ["coffee", 3]

        cursor = conn.cursor()

        cursor.callproc('select_products', args)

        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    call_find_all_sp()


