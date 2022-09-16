from mysql.connector import connect


def table_gen(database_data, path):
    try:
        with connect(host=database_data['host'],
                     port=database_data['port'],
                     user=database_data['user_name'],
                     password=database_data['password'],
                     database=database_data['db_name']) as connection:
            with connection.cursor() as cursor:
                with open(path + '/Do_list/request.SQL', 'rb') as file:
                    cursor.execute(file.read())
                    cursor.fetchone()
    except Exception as error:
        print(error)
