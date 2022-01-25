"""Задача 1"""


def func(a=float, b=float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return 'Бесконечность'
    except TypeError:
        return 'Неверно введеы данные'


a, b = map(int, input('Введите делимое и делитель: ').split())
print(func(a, b))


"""Задача 2"""


def user(**kwargs):
    return f"Имя: {kwargs['name']}, Фамилия: {kwargs['surname']}, Год рождения: {kwargs['birth_date']}," \
           f" Город проживания: {kwargs['city']}, Почта: {kwargs['email']}, Номер телефона: {kwargs['phone_number']}"


name, surname, birth_date, city, email, phone_number = input('Введите данные: ').split()
print(user(name=name, surname=surname, birth_date=birth_date, city=city, email=email, phone_number=phone_number))


"""Задача 3"""


def my_func(a, b, c):
    d = [a, b, c]
    d.sort(reverse=True)
    return sum(d[:2])


a, b, c = map(int, input('Введите 3 значения: ').split())
print(my_func(a, b, c))


"""Задача 4"""


def my_func(x = float, y = int) -> float:
    """
Функция для возведения числа в степень
    :param x: Действительное положительное число, целое либо дробное - основание степени
    :param y: Целое отрицательное число - степень
    :return: float
    """
    result = 1
    if y < 0:
        for i in range(abs(y)):
            result /= x
    elif y > 0:
        for i in range(y):
            result *= x
    return result


print(my_func(2, -3))
print(my_func(2, 3))
print(my_func(2, 0))

"""Либо"""


def my_func_2(x, y):
    result = x**y
    return result


print(my_func_2(2, -3))
print(my_func_2(2, 3))
print(my_func_2(2, 0))


"""Задача 5"""


def new_sum(string):
    global global_sum
    numbers = string.split()
    sum = i = 0
    for element in numbers:
        i += 1
        if i == len(numbers):
            try:
                sum += int(element)
            except ValueError:
                pass
            global_sum += sum
            return global_sum
        try:
            sum += int(element)
        except ValueError:
            pass


global_sum = 0

while True:
    string = input()
    if string[len(string) - 1] == '!':
        print(new_sum(string))
        break
    print(new_sum(string))


"""Задача 6"""


# int_func = lambda text: text.title()
def int_func(text):
    return text.capitalize()


word = input('Введите слово с маленькой буквы: ')
print(int_func())


"""Задача 7"""


text = input('Введите текст с маленькой буквы: ')
words = text.split()
for el in words:
    print(int_func(el), end=' ')