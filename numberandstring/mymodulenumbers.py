TEN = 10
HUNDRED = 100
THOUSAND = 1000
SUPER_USER = True

def is_even(value):
    """Функция возвращает True если значение четное и False в противном случае
    :param value: число, четность которого нужно определить"""

    return value % 2 == 0


def power(value, level):
    """Функция возводит значение value в степень level
    :param value: число, которое нужно возвести в степень
    :param level: степень"""

    return value ** level