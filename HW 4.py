# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

# # Чтобы не растягивать удовольствие от проверки задачи я добавил автогенерацию массива,
# # ибо сам усталь вводить его тридцать раз вручную, а уж каково преподавателям...
# firstList = [randint(-10,10) for i in range(int(input('Введите длину первого массива: ')))]
# secondList = [randint(-10,10) for i in range(int(input('Введите длину второго массива : ')))]
# resultList = []

# print(firstList, secondList)

# for i in firstList:
#     for j in secondList:
#         if i == j & i not in resultList:
#             resultList.append(i)
# print(sorted(resultList))

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод
# — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого
# куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# Снова
bushes = [randint(1, 50) for i in range(int(input('Введите, сколько кустов черники: ')))]
res = 0
print(bushes)
for i in range(len(bushes)):
    sum_of_list = 0
    if i == 0:
        sum_of_list = bushes[-1] + bushes[0] + bushes[1]
    elif i == len(bushes) - 1 :
        sum_of_list = bushes[i-1] + bushes[i] + bushes[0]
    else:
        sum_of_list = bushes[i-1] + bushes[i] + bushes[i+1]
    if sum_of_list > res:
        res = sum_of_list
print(res)