import random
import timeit
import functools
import matplotlib.pyplot as plt
import numpy as np

def slowsort(arr, i, j):
    if i >= j:
        return
    mid = (i + j) // 2
    slowsort(arr, i, mid)               # Рекурсивная сортировка первой половины
    slowsort(arr, mid + 1, j)
    if arr[mid] > arr[j]:
        arr[mid], arr[j] = arr[j], arr[mid]
    slowsort(arr, i, j - 1)             # Рекурсивная проверка оставшихся элементов

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

max_n = 170
max_vector = np.array([random.randint(1, 100) for _ in range(max_n)])

ndigits = 6
number_of_runs = 4

n_values = list(range(10, max_n + 1, 10))
average_times_slowsort = []

@timing_decorator(ndigits, number_of_runs)
def calculate_slowsort(vector):
    slowsort(vector, 0, len(vector) - 1)

for n in n_values:
    print(f"Тестирование для n = {n}")
    average_time = calculate_slowsort(max_vector[:n].copy())
    average_times_slowsort.append(average_time)

plt.plot(n_values, average_times_slowsort, linestyle='-', color='b', label='Slowsort')
plt.title('Зависимость времени выполнения Slowsort от n')
plt.xlabel('n')
plt.ylabel('Среднее время выполнения (секунды)')
plt.legend()
plt.savefig('slowsort_time.png')
