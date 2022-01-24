"""Задача 1"""

my_list = [1, 2, 'text', None, 2.5, False]
for i in range(len(my_list)):
    print(type(my_list[i]))

"""Задача 2"""

my_list = []
while True:
    my_list.append(input('Введите элементы списка, условие остановки - enough: '))
    if my_list[len(my_list)-1] == 'enough':
        my_list.pop(len(my_list)-1)
        break
print('Получившийся список:', my_list)
i = 0
my_list2 = []
if len(my_list) % 2 == 0:
    while i < len(my_list):
        my_list2.append(my_list[i+1])
        my_list2.append(my_list[i])
        i += 2
    print('Список с перевернутыми элементами:', my_list2)
else:
    while i < len(my_list)-1:
        my_list2.append(my_list[i + 1])
        my_list2.append(my_list[i])
        i += 2
    my_list2.append(my_list[len(my_list)-1])
    print('Список с перевернутыми элементами при нечетном количестве:', my_list2)

"""Задача 3"""

month = int(input('Введите месяц в виде числа: '))
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]
seasons = dict(winter=winter, spring=spring, summer=summer, fall=fall)
print(seasons)
for i in seasons.values():
    for j in i:
        if month == j:
            if j in winter:
                print('Месяц зимний')
            elif j in spring:
                print('Месяц весенний')
            elif j in summer:
                print('Месяц летний')
            else:
                print('Месяц осенний')
            break


"""Задача 4"""

string = input('Введите текст: ')
# print(string)
word = []
text = []
x = ''
y = ''
z = ''
j = 0
Flag_10 = False
Flag_space = False
for i in string:
    j += 1
    if Flag_10 is False and Flag_space is False:
        if j != len(string):
            word.append(i)
    if len(word) == 10:
        Flag_10 = True
    try:
        if string[j] == ' ':
            Flag_space = True
    except Exception:
        pass
    if j == len(string) and Flag_10 is False:
        word.append(i)
        for k in word:
            x += k
        text.append(x)
        x = ''
    if j == len(string) and Flag_10 is True:
        for k in word:
            y += k
        text.append(y)
        y = ''
    if i == ' ':
        Flag_space = False
        Flag_10 = False
        for k in word:
            z += k
        text.append(z)
        z = ''
        word.clear()
for i, el in enumerate(text):
    print(f'{i}) {el}')

"""Задача 5"""

rate = [7, 5, 3, 3, 2]
el = int(input('Введите новый элемент рейтинга: '))
rate.append(el)
rate.sort()
rate.reverse()
print(rate)

"""Задача 6"""

name, price, quantity, dimension = input('Ведите наименование торвара, цену, количество и единицы измерения: ').split()
dict_1 = {'название': name, 'цена': price, 'количество': quantity, 'eд': dimension}
name, price, quantity, dimension = input('Ведите наименование торвара, цену, количество и единицы измерения: ').split()
dict_2 = {'название': name, 'цена': price, 'количество': quantity, 'eд': dimension}
name, price, quantity, dimension = input('Ведите наименование торвара, цену, количество и единицы измерения: ').split()
dict_3 = {'название': name, 'цена': price, 'количество': quantity, 'eд': dimension}

my_tuple_1 = (1, dict_1)
my_tuple_2 = (2, dict_2)
my_tuple_3 = (3, dict_3)

struct = [my_tuple_1, my_tuple_2, my_tuple_3]
structure = {}
final = {}
for tup in struct:
    number, info = tup
    for key, value in info.items():
        value_list = structure.get(key, [])
        if value not in value_list:
            value_list.append(value)
        structure[key] = value_list

for item in structure.items():
    print(item)