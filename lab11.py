import random
import time
import matplotlib.pyplot as plt

# измерение времени выполнения ф-ии
def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    return time.time() - start_time

# ф-я генерирует случайную матрицу размера n x n с неотрицательными элементами
def random_matrix(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

# ф-я произведения матриц
def matrix_multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Параметры
matrix_sizes = range(10, 201, 10)  # Размеры матриц от 10 до 200 с шагом 10
matrix_multiply_timings = []

# Основной цикл для замера времени
for size in matrix_sizes:
    A = random_matrix(size)
    B = random_matrix(size)
    multiply_time = measure_time(matrix_multiply, A, B)
    matrix_multiply_timings.append(multiply_time)

    print(f"\nМатрица A ({size} x {size}):")
    for row in A:
        print(row)

    print(f"\nМатрица B ({size} x {size}):")
    for row in B:
        print(row)

    C = matrix_multiply(A, B)
    print(f"\nРезультат произведения матриц A и B ({size} x {size}):")
    for row in C:
        print(row)

# Построение графика для перемножения матриц
plt.figure(figsize=(14, 7))
plt.plot(matrix_sizes, matrix_multiply_timings, label='Перемножение матриц', marker='o', linewidth=0.5)
plt.xlabel('Размер матрицы n')
plt.ylabel('Время (секунды)')
plt.title('Время выполнения перемножения матриц в зависимости от размера n')
plt.legend()
plt.grid()
plt.show()
