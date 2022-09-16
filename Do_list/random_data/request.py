from Do_list.random_data.goods import random_goods as RG
from mysql.connector import connect

def table_gen(database_data, path):
    request = RG()

    try:
        with connect(host=database_data['host'],
                     port=database_data['port'],
                     user=database_data['user_name'],
                     password=database_data['password'],
                     database=database_data['db_name'],
                     buffered=True) as connection:
            with connection.cursor() as cursor:
                print(request)
                cursor.execute(request)
                cursor.fetchone()
    except Exception as error:
        print(error)