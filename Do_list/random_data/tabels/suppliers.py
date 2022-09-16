from Do_list.random_data.my_random import random_name,\
    random_str,\
    random_prise,\
    random_int

def random_suppliers():
    names = ('Postav', 'Gorod', 'Ulica', 'Dom', 'Korpus', 'Kv', 'Telef')
    names = str(names).replace("'", '`')
    request = ''

    for c in range(1000):
        values = (random_name(),
                  random_name(),
                  random_name(),
                  random_name(),
                  random_name(),
                  random_name(),
                  str(random_int(10**11, 10**12-1)))
        request += f'INSERT INTO `suppliers` {names} VALUES {values};\n'

    return request
