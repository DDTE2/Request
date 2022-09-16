from Do_list.random_data.my_random import random_name,\
    random_str,\
    random_prise

def random_goods():
    names = ('Artikul', 'Name', 'Edizm', 'Zena')
    names = str(names).replace("'", '`')
    request = ''

    for c in range(1000):
        values = (random_str(2, 255),
                  random_name(),
                  random_str(2,10),
                  random_prise(10, 10000))
        request += f'INSERT INTO `goods` {names} VALUES {values};\n'

    return request
