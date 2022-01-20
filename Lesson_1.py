"""Задача 1"""

a, b, c = map(int, input('Введите 3 числа: ').split())
x, y, z = input('Введите 3 строки: ').split()
print('Числа: ', a, b, c)
print('Строки: ', x, y, z)

"""Задача 2"""

time_seconds = int(input('Введите время в секундах: '))
hours = time_seconds // 3600
minutes = (time_seconds - hours * 3600) // 60
seconds = time_seconds - hours * 3600 - minutes * 60
hours = str(hours)
minutes = str(minutes)
seconds = str(seconds)

if len(hours) < 2:
    hours = '0' + hours
if len(minutes) < 2:
    minutes = '0' + minutes
if len(seconds) < 2:
    seconds = '0' + seconds
time_classic = hours + ":" + minutes + ":" + seconds
print('Текущее время:', time_classic)
print(f'Текущее время: {hours}:{minutes}:{seconds}')

"""Задача 3"""

n = input('Введите число: ')
number = int(n) + int(2*n) + int(3*n)
print(number)

"""Задача 4"""

def max_digit(x):
    i = 0
    max = 0
    max_current = 0
    while i < len(x)-1:
        if int(x[i]) <= int(x[i+1]):
            max_current = int(x[i+1])
        elif int(x[i]) > int(x[i+1]):
            max_current = int(x[i])
        if max_current >= max:
            max = max_current
        i += 1
    return max

x = input('Введите целое положительное число: ')
print(max_digit(x))

"""Задачи 5-6"""

gain, expenses = map(int, input('Введите прибыль и издержки: ').split())
result = gain - expenses
if result < 0:
    print('Убыток:', abs(result))
else:
    print('Выручка:', result)
    ROI = gain / result
    print(f'{ROI * 100}%')
    staff_number = int(input('Введите численность персонала:'))
    print('Выручка на одного сотрудника:', result / staff_number)

"""Задача 7"""

a, b = map(float, input('Введите результат пробежки первого дня и конечный результат, км: ').split())
day = 1
result = a
while result < b:
    result *= 1.1
    day += 1
print(f'Результат составит не менее {b} км на {day} день')
