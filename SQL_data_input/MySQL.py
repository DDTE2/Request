import mysql.connector as MC

def create_connection(host_name, port, user_name, user_password, db_name):
    connection = None
    try:
        connection = MC.connect(
            host=host_name,
            port=port,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        cur = connection.cursor()
        connection.close()
        return {'host': host_name,
                'port': port,
                'user': user_name,
                'password': user_password,
                'database': db_name}
    except:
        return 'Error'