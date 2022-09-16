from Do_list.random_data.tabels.goods import random_goods as RG
from Do_list.random_data.tabels.suppliers import random_suppliers as RS
from Do_list.random_data.tabels.receipts import random_receipts as RR
from mysql.connector import connect

def table_gen(database_data, path):
    request = RG() + RS() + RR()
    print(request)

    ##try:
    with connect(host=database_data['host'],
                 port=database_data['port'],
                 user=database_data['user_name'],
                 password=database_data['password'],
                 database=database_data['db_name'],
                 autocommit=True) as connection:
        with connection.cursor() as cursor:
            cursor.execute(request)
            ##cursor.fetchone()
    ##except Exception as error:
        ##print(error)