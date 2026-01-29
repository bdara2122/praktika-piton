# ПРАКТИЧЕСКАЯ 8
# ВАРИАНТ 1 (1)

# Функция для вычисления суммы и количества положительных элементов над главной диагональю
def count_positive_above_diagonal(matrix):
    n = len(matrix)  # Размер матрицы
    sum_positive = 0  # Сумма положительных элементов
    count_positive = 0 # Количество положительных элементов
    # Проходим по элементам над главной диагональю
    for i in range(n):
        for j in range(i + 1, n):  # Начинаем с i+1, чтобы быть над диагональю
            if matrix[i][j] > 0:
                sum_positive += matrix[i][j]
                count_positive += 1

    return sum_positive, count_positive
# Пример использования
# Создаем пример матрицы 3x3
A = [
    [1, -2, 3],
    [-4, 5, 6],
    [7, -8, 9]
]
sum_result, count_result = count_positive_above_diagonal(A)
print(f"Сумма положительных элементов: {sum_result}")
print(f"Количество положительных элементов: {count_result}")

# ВАРИАНТ 2 (1)

def is_magic(matrix):
    summ = sum(matrix[0])
    for i in range(len(matrix)):
        temp = 0
        for j in range(len(matrix)):
            temp += matrix[j][i]
        if temp != summ or sum(matrix[i]) != summ:
            return False
    return True
mat = [[4, 3, 3], [3, 4, 3], [3, 3, 4]]
print(is_magic(mat))
mat = [[4, 3, 4], [3, 4, 3], [3, 3, 4]]
print(is_magic(mat))

# ВАРИАНТ 3 (1)

from random import randint
n = int(input('Введите размерность матрицы: '))
arr = [[randint(0, 100) for col in range(n)] for row in range(n)]
[print(*i) for i in arr]
n = int(input('Введите размерность матрицы: '))
arr =[list(map(int, input(f'Вводите в строчку через пробел, не более {n} значений: ').split())) for row in range(n)]
[print(*i) for i in arr]
n = int(input('Введите размерность матрицы: '))
arr = [[0 for col in range(n)] for row in range(n)]
for row in range(n):
    for col in range(n):
        arr[row][col] = int(input(f'Введите элемент матрицы по индексу {row} {col}: '))
[print(*i) for i in arr]

# ВАРИАНТ 4 (1)

def find_min_max_rows(matrix):
    # Проверяем, что матрица не пустая
    if not matrix or not matrix:
        return None, None
    min_sum = float('inf')  # Бесконечность для поиска минимума
    max_sum = -float('inf') # Бесконечность для поиска максимума
    min_row = max_row = None
    # Проходим по всем строкам матрицы
    for i, row in enumerate(matrix):
        current_sum = sum(row)  # Считаем сумму элементов строки
        # Обновляем минимум и максимум
        if current_sum < min_sum:
            min_sum = current_sum
            min_row = i
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = i
    return min_row, min_sum, max_row, max_sum
# Пример использования
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
min_index, min_value, max_index, max_value = find_min_max_rows(matrix)
print(f"Строка с минимальной суммой: {matrix[min_index]}")
print(f"Сумма элементов минимальной строки: {min_value}")
print(f"\nСтрока с максимальной суммой: {matrix[max_index]}")
print(f"Сумма элементов максимальной строки: {max_value}")

# ВАРИАНТ 5(1)

from random import randint
 
N, M = 4, 3
lst = [[randint(-50, 50) for _ in range(M)] for _ in range(N)]
 
print(list([(1 if min(i) % 2 else 0) if j == min(i) else j for j in i] for i in lst))

# ВАРИАНТ 6(1)

arr = [[2, 4, 6], [3, 10, 9], [-1, 5, 7]]
mi = float('inf')
ma = float('-inf')
for row in arr:
    ma = max(ma, max(row))
    mi = min(mi, min(row))
print(ma, mi)

# ВАРИАНТ 7(1)

def restore_symmetric_matrix(upper_triangle, n):
    """
    Восстанавливает симметричную матрицу n×n по верхнему треугольнику.
    
    Параметры:
        upper_triangle — список чисел (верхний треугольник по строкам);
        n — размерность квадратной матрицы.
    
    Возвращает:
        Двумерный список (матрицу n×n).
    """
    # Создаём пустую матрицу n×n
    matrix = [[0] * n for _ in range(n)]
    
    idx = 0  # индекс в массиве upper_triangle
    
    # Заполняем верхний треугольник (включая диагональ)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = upper_triangle[idx]
            idx += 1
    # Зеркально копируем в нижний треугольник (симметрия относительно главной диагонали)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[j][i] = matrix[i][j]
    return matrix
def print_matrix(matrix):
    """Печатает матрицу по строкам."""
    for row in matrix:
        print(" ".join(map(str, row)))
def main():
    try:
        # Ввод размера матрицы
        n = int(input("Введите размерность матрицы n: "))
        if n <= 0:
            print("Размерность должна быть положительным числом.")
            return
        
        # Вычисляем, сколько элементов должно быть в верхнем треугольнике
        expected_length = n * (n + 1) // 2
        print(f"Введите {expected_length} элементов верхнего треугольника (по строкам):")
        
        # Ввод массива
        upper_triangle = list(map(int, input().split()))
        
        
        if len(upper_triangle) != expected_length:
            print(f"Ошибка: нужно ровно {expected_length} чисел.")
            return
        
        # Восстанавливаем матрицу
        matrix = restore_symmetric_matrix(upper_triangle, n)
        
        # Выводим результат
        print("Восстановленная симметричная матрица:")
        print_matrix(matrix)
    
    except ValueError:
        print("Ошибка: введите целые числа.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
if __name__ == "__main__":
    main()

# ВАРИАНТ 8(1)

import numpy as np
N = 10
k = np.random.randint(N)
a = np.random.randint(10, 100, size=(N, N))
print(a)
 
for n in range(0, len(a)):
    print(a[k, n],'/',a[n,n], '=',  a[k,n] / a[n, n])

# ВАРИАНТ 9(1)

from random import randint
 
n = m = 10
arr = [[randint(-10, 10) for _ in range(m)] for _ in range(n)]
k = int(input('k='))
ma = 0
c = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]%k == 0:
            c +=1
            if arr[i][j] > ma:
                ma = arr[i][j]
print(*arr, sep='\n')
print(f'Count {c}')
print(f'Max {ma}')

# ВАРИАНТ 10(1)

def find_max_in_sorted_rows(matrix):
    max_value = float('-inf')  # Инициализируем минимальное возможное значение
    
    for row in matrix:
        # Проверяем, упорядочена ли строка по возрастанию или убыванию
        is_sorted = all(row[i] <= row[i+1] for i in range(len(row)-1)) or \
                   all(row[i] >= row[i+1] for i in range(len(row)-1))
        
        if is_sorted:
            # Находим максимум в отсортированной строке
            current_max = max(row)
            if current_max > max_value:
                max_value = current_max
    
    return max_value

# Пример использования:
matrix = [
    [1, 2, 3],    # Упорядочена по возрастанию
    [5, 4, 3],    # Упорядочена по убыванию
    [3, 2, 1],    # Упорядочена по убыванию
    [4, 5, 6]     # Не упорядочена
]

result = find_max_in_sorted_rows(matrix)
print("Максимальный элемент:", result)  # Выведет: Максимальный элемент: 6

# ВАРИАНТ 11(1)

def main():
    try:
        # Ввод размера матрицы
        n = int(input("Введите порядок квадратной матрицы n: "))
        if n <= 0:
            print("Ошибка: порядок матрицы должен быть положительным числом.")
            return
        
        # Ввод элементов матрицы
        print(f"Введите {n} строк матрицы {n}×{n} (элементы через пробел):")
        matrix = []
        for i in range(n):
            row_input = input().strip()
            if not row_input:
                print(f"Ошибка: строка {i+1} пуста.")
                return
            row = list(map(float, row_input.split()))
            if len(row) != n:
                print(f"Ошибка: в строке {i+1} должно быть ровно {n} элементов.")
                return
            matrix.append(row)
        
        # Поиск минимального элемента и номера его строки
        min_val = matrix[0][0]
        min_row_idx = 0
        
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < min_val:
                    min_val = matrix[i][j]
                    min_row_idx = i
        
        # Вычисление суммы элементов строки с минимальным элементом
        row_sum = sum(matrix[min_row_idx])
        
        # Вывод результатов
        print("\nИсходная матрица:")
        for row in matrix:
            print(" ".join(f"{x:8.3f}" for x in row))
        
        print(f"\nМинимальный элемент: {min_val} (находится в строке {min_row_idx + 1})")
        print(f"Сумма элементов этой строки: {row_sum}")
        
    except ValueError:
        print("Ошибка: введите корректные числовые значения.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()

# ВАРИАНТ 12(1)

def find_matching_row_col_indices(matrix):
    """
    Находит индексы k (от 1 до n), для которых k-я строка совпадает с k-м столбцом.
    
    Параметры:
        matrix — список списков, квадратная матрица n×n.
    
    Возвращает:
        Список индексов k (в человекочитаемой нумерации, от 1).
    """
    n = len(matrix)
    result = []
    
    for k in range(n):  # k — индекс в нулевом отсчёте (0, 1, ..., n-1)
        row = matrix[k]  # k-я строка
        col = [matrix[i][k] for i in range(n)]  # k-й столбец
        
        if row == col:
            result.append(k + 1)  # перевод в нумерацию с 1
    
    
    return result

def print_matrix(matrix, title="Матрица"):
    """Печатает матрицу по строкам."""
    print(title + ":")
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    try:
        # Ввод размера матрицы
        n = int(input("Введите порядок квадратной матрицы n: "))
        if n <= 0:
            print("Порядок матрицы должен быть положительным числом.")
            return
        
        
        # Ввод элементов матрицы
        print(f"Введите элементы матрицы {n}×{n} (построчно, через пробел):")
        matrix = []
        for i in range(n):
            row = list(map(float, input().split()))
            if len(row) != n:
                print(f"Ошибка: в строке {i+1} должно быть ровно {n} чисел.")
                return
            matrix.append(row)
        
        
        # Печатаем матрицу
        print_matrix(matrix, "Введённая матрица")
        
        # Находим совпадающие строки и столбцы
        matches = find_matching_row_col_indices(matrix)
        
        # Выводим результат
        if matches:
            print(f"\nИндексы k, для которых k-я строка совпадает с k-м столбцом: {matches}")
        else:
            print("\nНет таких k, при которых k-я строка совпадает с k-м столбцом.")
            
    except ValueError:
        print("Ошибка: введите числа (целые или вещественные).")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()

# ВАРИАНТ 13(1)

def find_min_in_even_rows(matrix, m, n):
    """
    Находит наименьший элемент в каждой чётной строке матрицы (2-я, 4-я, ... в нумерации с 1).
    
    Параметры:
        matrix — список списков, матрица размером m×n;
        m — число строк;
        n — число столбцов.
    
    Возвращает:
        Список пар (номер_строки, минимальный_элемент) для чётных строк.
    """
    result = []
    
    # Проходим по строкам с нечётными индексами (это чётные строки в нумерации с 1)
    for i in range(1, m, 2):  # i = 1, 3, 5, ...
        min_val = min(matrix[i])
        result.append((i + 1, min_val))  # номер строки (с 1) и минимум
    
    
    return result

def print_matrix(matrix, title="Матрица"):
    """Печатает матрицу по строкам."""
    print(title + ":")
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    try:
        # Ввод размеров матрицы
        m = int(input("Введите количество строк M: "))
        n = int(input("Введите количество столбцов N: "))
        
        if m <= 0 or n <= 0:
            print("Размеры матрицы должны быть положительными числами.")
            return
        
        
        # Ввод элементов матрицы
        print(f"Введите элементы матрицы {m}×{n} (построчно, через пробел):")
        matrix = []
        for i in range(m):
            row = list(map(float, input().split()))
            if len(row) != n:
                print(f"Ошибка: в строке {i+1} должно быть ровно {n} чисел.")
                return
            matrix.append(row)
        
        
        # Печатаем матрицу
        print_matrix(matrix, "Введённая матрица")
        
        # Находим минимумы в чётных строках
        minima = find_min_in_even_rows(matrix, m, n)
        
        
        # Выводим результат
        if minima:
            print("\nНаименьшие элементы в чётных строках:")
            for row_num, min_val in minima:
                print(f"Строка {row_num}: минимальный элемент = {min_val}")
        else:
            print("\nЧётных строк в матрице нет (либо матрица пуста).")
            
    except ValueError:
        print("Ошибка: введите числа (целые или вещественные).")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()

# ВАРИАНТ 14(1)

def print_matrix(matrix, title="Матрица"):
    """Печатает матрицу построчно."""
    print(title + ":")
    for row in matrix:
        print(" ".join(map(str, row)))

def find_max_diag_row_index(matrix):
    """
    Находит индекс строки, содержащей максимальный элемент на главной диагонали.
    
    Параметры:
        matrix — квадратная матрица (список списков).
    
    Возвращает:
        Индекс строки (от 0) с макс. элементом на диагонали.
    """
    n = len(matrix)
    max_val = matrix[0][0]
    max_idx = 0
    
    for i in range(1, n):
        if matrix[i][i] > max_val:
            max_val = matrix[i][i]
            max_idx = i
    return max_idx

def swap_rows(matrix, row1, row2):
    """
    Меняет местами две строки матрицы (по индексам).
    """
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

def main():
    try:
        # Ввод размера матрицы
        n = int(input("Введите порядок квадратной матрицы n: "))
        if n <= 0:
            print("Порядок матрицы должен быть положительным числом.")
            return
        
        # Ввод элементов матрицы
        print(f"Введите элементы матрицы {n}×{n} (построчно, через пробел):")
        matrix = []
        for i in range(n):
            row = list(map(float, input().split()))
            if len(row) != n:
                print(f"Ошибка: в строке {i+1} должно быть ровно {n} чисел.")
                return
            matrix.append(row)
        
        # Ввод номера строки m (нумерация с 1)
        m = int(input(f"Введите номер строки m для обмена (от 1 до {n}): "))
        if m < 1 or m > n:
            print(f"Номер строки m должен быть от 1 до {n}.")
            return
        m_idx = m - 1  # перевод в нумерацию с 0
        
        # Печатаем исходную матрицу
        print_matrix(matrix, "Исходная матрица")
        
        # Находим строку с макс. элементом на главной диагонали
        max_diag_row = find_max_diag_row_index(matrix)
        max_diag_val = matrix[max_diag_row][max_diag_row]
        print(f"\nМаксимальный элемент на главной диагонали: {max_diag_val}")
        print(f"Он находится в строке {max_diag_row + 1} (индекс {max_diag_row})")
        
        # Если строка уже та, что нужна — сообщать, но не менять
        if max_diag_row == m_idx:
            print(f"\nСтрока {m} уже содержит максимальный элемент диагонали — обмен не требуется.")
        else:
            # Меняем строки
            swap_rows(matrix, max_diag_row, m_idx)
            print(f"\nСтроки {max_diag_row + 1} и {m} поменяны местами.")
        
        # Выводим результат
        print_matrix(matrix, "Матрица после обмена")
        
    except ValueError:
        print("Ошибка: введите целые числа для n и m, числа (целые/вещественные) для элементов матрицы.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()

# ВАРИАНТ 15(1)

def print_matrix(matrix, title="Матрица"):
    """Печатает матрицу построчно, элементы разделены пробелом."""
    print(title + ":")
    for row in matrix:
        print(" ".join(map(str, row)))


def find_and_multiply_rows(matrix, c, d):
    """
    Находит строки, где есть элемент == c, и умножает всю строку на d.
    
    Параметры:
        matrix — список списков (матрица M×N);
        c — значение для поиска;
        d — множитель.
    Возвращает:
        Список номеров строк (с 1), которые были изменены.
    """
    changed_rows = []
    
    for i in range(len(matrix)):
        if c in matrix[i]:  # есть ли c в строке i?
            # Умножаем все элементы строки на d
            matrix[i] = [x * d for x in matrix[i]]
            changed_rows.append(i + 1)  # нумерация с 1
    
    return changed_rows

def main():
    try:
        # Ввод размеров матрицы
        M = int(input("Введите количество строк M: "))
        N = int(input("Введите количество столбцов N: "))
        
        if M <= 0 or N <= 0:
            print("Размеры матрицы должны быть положительными числами.")
            return
        
        
        # Ввод элементов матрицы
        print(f"Введите элементы матрицы {M}×{N} (построчно, через пробел):")
        matrix = []
        for i in range(M):
            row = list(map(float, input().split()))
            if len(row) != N:
                print(f"Ошибка: в строке {i+1} должно быть ровно {N} чисел.")
                return
            matrix.append(row)
        
        
        # Ввод значений c и d
        c = float(input("Введите значение c для поиска: "))
        d = float(input("Введите множитель d: "))
        
        
        # Печатаем исходную матрицу
        print_matrix(matrix, "Исходная матрица")
        
        # Обрабатываем матрицу
        modified_rows = find_and_multiply_rows(matrix, c, d)
        
        # Выводим результат
        if modified_rows:
            print(f"\nСтроки, содержащие элемент {c}: {modified_rows}")
            print(f"Все элементы этих строк умножены на {d}.")
            print_matrix(matrix, "Изменённая матрица")
        else:
            print(f"\nНи в одной строке нет элемента, равного {c}. Матрица не изменена.")
            
    except ValueError:
        print("Ошибка: введите числа (целые или вещественные).")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()
