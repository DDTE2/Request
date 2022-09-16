from Do_list.random_data.my_random import random_name,\
    random_str,\
    random_prise,\
    random_int

def random_receipts():
    names = ('IdTovar', 'IdPostav', 'DatPrih', 'Kolvo')
    names = str(names).replace("'", '`')
    request = ''

    for c in range(1000):
        values = (random_int(1, 1000),
                  random_int(1, 1000),
                  f'{random_int(2000, 2022)}-{random_int(1, 12)}-{random_int(1, 29)}',
                  random_int(1, 1000))
        request += f'INSERT INTO `receipts` {names} VALUES {values};\n'

    return request
