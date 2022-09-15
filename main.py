from os.path import dirname, exists

path = dirname(__file__)

with open(path + '/Data/database.data', 'r') as file:
    flag = file.read() == ''

if flag:
    from SQL_data_input.main import SQL_data

    SQL = SQL_data(path)
    SQL.run()

else:
    from Start.main import autorization
    start = autorization(path)
    start.run()