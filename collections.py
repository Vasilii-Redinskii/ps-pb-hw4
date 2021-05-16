from collections import namedtuple


# Создаем описание (т.е. некую структуру) для объекта
student = namedtuple('student','first_name last_name age')

# Создаем сам объект, используя описание
student1 = student(first_name='Иван', last_name='Иванов', age=18)

# Обращаемся к полям объекта через точку
print(student1.first_name)
print(student1.last_name)
print(student1.age)
