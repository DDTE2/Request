from random import choice, randint

def random_str(min_len=0, max_len=1000):
    if min_len > max_len:
        max_len, min_len = min_len, max_len
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' + 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = [choice(letters) for c in range(randint(min_len, max_len))]

    return ''.join(text)
def random_name():
    AL = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    UL = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    text = [choice(UL)] + [choice(AL) for c in range(randint(1,19))]
    return ''.join(text)

def random_prise(_min, _max):
    if _min > _max:
        _max, _min = _min, _max

    i = randint(_min, _max)

    if randint(0, 1):
        if i == _max:
            return _max - 1 + randint(0, 100)/100
        else:
            return i + randint(0, 100) / 100
    else:
        return i
def random_int(_min, _max):
    if _min > _max:
        _max, _min = _min, _max
    return randint(_min, _max)
