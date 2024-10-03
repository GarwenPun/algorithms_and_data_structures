import random
import time
import matplotlib.pyplot as plt

# измерение времени выполнения ф-ии
def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    return time.time() - start_time

# создание случайного вектора длины n c неотрицательными элементами
def random_vector(n):
    return [random.random() for _ in range(n)]

# функция вычисления суммы элементов вектора
def sum_elements(v):
    total = 0
    for value in v:
        total += value
    return total

# функция вычисления произведения элементов вектора
def product_elements(v):
    product = 1
    for value in v:
        product *= value
    return product

# функция для нахождения максимального элемента вектора
def max_element(v):
    max_value = v[0]
    for i in range(1, len(v)):
        if v[i] > max_value:
            max_value = v[i]
    return max_value

# функция для нахождения среднего арифметического элементов
def average_elements(v):
    total = sum_elements(v)
    return total / len(v)

# Параметры
Student_number = 1
N = 20 - Student_number
n_values = range(1, 100000 * N + 1, 100 * N)
timings_sum = []
timings_product = []
timings_max = []
timings_average = []

# Цикл для замера времени
for n in n_values:
    v = random_vector(n)

    # Задание 1: замер времени для четырех функций
    sum_time = measure_time(sum_elements, v)
    product_time = measure_time(product_elements, v)
    max_time = measure_time(max_element, v)
    average_time = measure_time(average_elements, v)

    # Добавляем значения в списки
    timings_sum.append(sum_time)
    timings_product.append(product_time)
    timings_max.append(max_time)
    timings_average.append(average_time)

# Построение графиков
plt.figure(figsize=(14, 7))
plt.plot(n_values, timings_sum, label='Сумма элементов', linewidth=0.5)
plt.plot(n_values, timings_product, label='Произведение элементов', linewidth=0.5)
plt.plot(n_values, timings_max, label='Максимум', linewidth=0.5)
plt.plot(n_values, timings_average, label='Среднее арифметическое', linewidth=0.5)
plt.xlabel('Размер n')
plt.ylabel('Время (секунды)')
plt.title('Время выполнения функций в зависимости от n')
plt.legend()
plt.grid()
plt.show()

