import numpy as np

first = [x ** (1 / 2) for x in range(100)]
second = [x ** (1 / 3) for x in range(100, 200)]
third = [x / y for x in range(200, 300, 2) for y in [3, 5]]

great_secret = np.array([first, second, third]).T
print(great_secret)
print(great_secret.shape)
result1 = 0
result1 = np.cos(great_secret[0][0]) + np.cos(great_secret[0][1]) + np.cos(great_secret[0][2])
print('Сумма косинусов первой строки массива: {}'.format(result1))

# Чему равна сумма элементов массива great_secret, значение которых больше 50?
result2 = 0
for i in range(len(great_secret)):
    for j in range(len(great_secret[i])):
        if great_secret[i][j] > 50:
            result2 = result2 + great_secret[i][j]
print(result2)

# Переведите массив great_secret в одномерную форму. Какое значение в получившемся массиве имеет элемент с индексом 150? Скопируйте ответ из Jupyter Notebook без изменений.
print(np.repeat(great_secret, 1)[150])

# Отсортируйте значения столбцов массива great_secret по возрастанию. Чему равна сумма элементов последней строки отсортированного массива? Ответ округлите до двух цифр после запятой.
a = np.sort(great_secret, axis=0)
print(a)


def filas(array):
    summed_list = [sum(i) for i in array]
    print(summed_list[-1])


filas(a)
