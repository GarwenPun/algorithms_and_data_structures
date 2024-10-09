import random
import timeit
import functools
import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):  # Проходим по массиву до уже отсортированных элементов
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

@functools.lru_cache(maxsize=None)
def timing_decorator(ndigits: int, number: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> float:
            usage_time = timeit.timeit(
                lambda: func(*args, **kwargs),
                number=number,
            )
            return round(usage_time / number, ndigits)

        return wrapper

    return decorator

max_n = 100001
max_vector = np.array([random.randint(1, 100) for _ in range(max_n)])

ndigits = 6
number_of_runs = 5

n_values = [100, 1000, 2000, 3500, 5000, 10000]
average_times_bubble_sort = []

@timing_decorator(ndigits, number_of_runs)
def calculate_bubble_sort(vector):
    bubble_sort(vector)

for n in n_values:
    print(f"Тестирование для n = {n}")
    average_time = calculate_bubble_sort(max_vector[:n].copy())
    average_times_bubble_sort.append(average_time)

plt.plot(n_values, average_times_bubble_sort, linestyle='-', color='b', label='Bubble Sort')
plt.title('Зависимость времени выполнения пузырьковой сортировки от n')
plt.xlabel('n')
plt.ylabel('Среднее время выполнения (секунды)')
plt.legend()
plt.savefig('bubble_sort_time.png')
