# ПРАКТИЧЕСКАЯ 7
# ВАРИАНТ 1(2)

def process_array(arr, num):
    """Обрабатывает массив: выводит сумму и среднее."""
    total = sum(arr)
    average = total / len(arr)
    print(f"Массив {num}: {arr}")
    print(f"  Сумма элементов: {total}")
    print(f"  Среднеарифметическое: {average:.2f}")  # 2 знака после запятой
    print()  # пустая строка для разделения
# Ввод трёх массивов
print("Введите элементы трёх массивов (целые числа).")
print("Каждый массив — через пробел; максимум 15 элементов.\n")
arrays = []
for i in range(1, 4):
    while True:
        try:
            line = input(f"Массив {i}: ").strip()
            if not line:
                print("Ошибка: пусто. Повторите ввод.")
                continue
            arr = list(map(int, line.split()))
            if len(arr) > 15:
                print("Ошибка: больше 15 элементов. Повторите ввод.")
                continue
            arrays.append(arr)
            break
        except ValueError:
            print("Ошибка: введите только целые числа. Повторите ввод.")
# Обработка и вывод результатов
print("\nРезультаты:")
for idx, arr in enumerate(arrays, start=1):
    process_array(arr, idx)

# ВАРИАНТ 2(2)

def rectangle_area(a, b):
    """Вычисляет площадь прямоугольника по двум сторонам."""
    return a * b
def main():
    print("Введите стороны трёх прямоугольников (длина и ширина).")
    rectangles = []  # список для хранения данных о прямоугольниках
    for i in range(1, 4):  # цикл для трёх прямоугольников
        print(f"\nПрямоугольник {i}:")
        while True:
            try:
                side_a = float(input("  Введите первую сторону: "))
                side_b = float(input("  Введите вторую сторону: "))
                
                if side_a <= 0 or side_b <= 0:
                    print("  Ошибка: стороны должны быть положительными числами. Повторите ввод.")
                    continue
                rectangles.append((side_a, side_b))
                break
            except ValueError:
                print("  Ошибка: введите числовое значение. Повторите ввод.")
    # Вывод результатов
    print("\nПлощади прямоугольников:")
    for i, (a, b) in enumerate(rectangles, start=1):
        area = rectangle_area(a, b)
        print(f"Прямоугольник {i}: стороны {a} и {b} → площадь = {area}")
# Запуск программы
if __name__ == "__main__":
    main()

# ВАРИАНТ 3(2)

text = input("Введите строку: ")
# Разбиваем строку на слова, сортируем буквы в каждом, собираем обратно
result = []
for word in text.split():
    sorted_word = ''.join(sorted(word.lower()))  # сортируем и объединяем в строку
    result.append(sorted_word)
# Собираем слова в строку
final_result = ' '.join(result)
print("Результат:", final_result)

# ВАРИАНТ 4(2)

import math
def is_point_inside_circle(x, y, a, b, R):
    """
    Проверяет, лежит ли точка (x, y) внутри окружности с центром (a, b) и радиусом R.
    Возвращает True, если точка внутри, иначе False.
    """
    distance_squared = (x - a)**2 + (y - b)**2
    return distance_squared < R**2  # строго внутри (на границе — не считаем)
def main():
    print("Введите параметры окружности:")
    a = float(input("  Координата центра по x (a): "))
    b = float(input("  Координата центра по y (b): "))
    R = float(input("  Радиус окружности (R): "))
    
    if R < 0:
        print("Ошибка: радиус не может быть отрицательным.")
        return
    print("\nВведите координаты трёх точек:")
    points = []
    for name in ['P', 'F', 'L']:
        print(f"Точка {name}:")
        x = float(input(f"  x{name}: "))
        y = float(input(f"  y{name}: "))
        points.append((x, y))
    # Подсчёт точек внутри окружности
    count_inside = 0
    inside_points = []
    for i, (x, y) in enumerate(points):
        if is_point_inside_circle(x, y, a, b, R):
            count_inside += 1
            inside_points.append(f"{['P', 'F', 'L'][i]}({x}, {y})")
    # Вывод результата
    print("\nРезультат:")
    print(f"Количество точек внутри окружности: {count_inside}")
    if inside_points:
        print("Точки внутри окружности:", ", ".join(inside_points))
    else:
        print("Точек внутри окружности нет.")
# Запуск программы
if __name__ == "__main__":
    main()

# ВАРИАНТ 5(2)

n = int(input("Введите число: "))
divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
print(" ".join(map(str, divisors)))

# ВАРИАНТ 6(2)

import math
def heron_area(a, b, c):
    """
    Вычисляет площадь треугольника по трём сторонам (формула Герона).
    Возвращает площадь или 0, если треугольник не существует.
    """
    # Проверяем существование треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        return 0.0
    p = (a + b + c) / 2  # полупериметр
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area
def quadrilateral_area(sides, diagonal):
    """
    Вычисляет площадь выпуклого четырёхугольника по 4 сторонам и диагонали.
    sides: список [a, b, c, d] — длины сторон по порядку.
    diagonal: длина диагонали, соединяющей вершины между сторонами a‑b и c‑d.
    """
    a, b, c, d = sides
    # Диагональ разбивает четырёхугольник на два треугольника:
    # Треугольник 1: стороны a, b и диагональ
    # Треугольник 2: стороны c, d и диагональ
    area1 = heron_area(a, b, diagonal)
    area2 = heron_area(c, d, diagonal)
    return area1 + area2
def main():
    print("Вычисление площади выпуклого четырёхугольника")
    print("Введите длины четырёх сторон и одной диагонали.")
    try:
        a = float(input("Сторона a: "))
        b = float(input("Сторона b: "))
        c = float(input("Сторона c: "))
        d = float(input("Сторона d: "))
        diag = float(input("Диагональ (соединяет вершины между a‑b и c‑d): "))
        if a <= 0 or b <= 0 or c <= 0 or d <= 0 or diag <= 0:
            print("Ошибка: длины должны быть положительными.")
            return
        sides = [a, b, c, d]
        total_area = quadrilateral_area(sides, diag)
        if total_area == 0:
            print("Ошибка: один из треугольников не существует (невыполнимо неравенство треугольника).")
        else:
            print(f"Площадь четырёхугольника: {total_area:.2f}")  
    except ValueError:
        print("Ошибка: введите числовые значения.")
# Запуск программы
if __name__ == "__main__":
    main()

# ВАРИАНТ 7(2)

def to_octal_code(number):
    # Проверяем, что число неотрицательное
    if number < 0:
        raise ValueError("Число должно быть неотрицательным")
    # Преобразуем число в восьмеричную систему
    oct_str = oct(number)[2:]  # [2:] убирает префикс '0o'
    # Дополняем нулями до 10 символов
    return oct_str.zfill(10)
# Пример использования
try:
    n = int(input("Введите число: "))
    result = to_octal_code(n)
    print(f"10-значный восьмеричный код: {result}")
except ValueError as e:
    print(e)

# ВАРИАНТ 8(2)

def swap_first_last(arr):
    """
    Процедура, меняющая местами первый и последний элементы массива.
    Если массив содержит менее 2 элементов — ничего не делает.
    """
    if len(arr) < 2:
        return  # В массиве меньше 2 элементов — менять нечего
    
    arr[0], arr[-1] = arr[-1], arr[0]  # Обмен значений
def main():
    try:
        # Ввод длины массива
        m = int(input("Введите длину массива m: "))
        if m <= 0:
            print("Длина массива должна быть положительным числом.")
            return
        # Ввод элементов массива
        print(f"Введите {m} элементов массива (через пробел):")
        elements = input().strip().split()
        if len(elements) != m:
            print(f"Ошибка: нужно ввести ровно {m} элементов.")
            return
        # Преобразуем в числа (int)
        A = [int(x) for x in elements]
        # Выводим исходный массив
        print("Исходный массив:", A)
        # Меняем местами первый и последний элементы
        swap_first_last(A)
        # Выводим полученный массив
        print("Массив после обмена:", A)
    except ValueError:
        print("Ошибка: введите только целые числа.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
# Запуск программы
if __name__ == "__main__":
    main()

# ВАРИАНТ 9(2)

from functools import reduce  # Функция для свёрки последовательности
from operator import mul  # Функция, перемножающая 2 числа
spisok = [16, 15, 9, 14, 13]  # Исходный список
 
result = reduce(mul, spisok)
#                    /\ Список для свёртки
#               /\ Используем умножение
#        /\ Сворачиваем контейнер
print("произведение: ", result)
 
result2 = sum(spisok) / len(spisok)
print("ср. арифметическое: ", result2)

# ВАРИАНТ 10(2)

def reverse_words(input_string):
    # Разбиваем строку на слова
    words = input_string.split()
    
    # Переворачиваем список слов
    reversed_words = words[::-1]
    
    # Объединяем слова обратно в строку
    result = ' '.join(reversed_words)
    return result
# Пример использования
input_str = "Привет мир программирования"
output_str = reverse_words(input_str)
print("Исходная строка:", input_str)
print("Перевернутая строка:", output_str)

# ВАРИАНТ 11(2)

def find_max_position(matrix):
    """
    Процедура: находит позицию (строка, столбец) максимального элемента в матрице.
    Возвращает: (max_value, row, col)
    """
    if not matrix or not matrix[0]:
        raise ValueError("Матрица пуста")

    max_val = matrix[0][0]
    max_row, max_col = 0, 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_row, max_col = i, j

    return max_val, max_row, max_col
def swap_max_elements(A, B):
    """
    Меняет местами максимальные элементы матриц A и B.
    Использует процедуру find_max_position.
    """
    # Находим максимумы и их позиции
    max_A, i_A, j_A = find_max_position(A)
    max_B, i_B, j_B = find_max_position(B)
    # Меняем местами
    A[i_A][j_A], B[i_B][j_B] = B[i_B][j_B], A[i_A][j_A]
def print_matrix(matrix, name):
    """Вспомогательная процедура для вывода матрицы."""
    print(f"{name}:")
    for row in matrix:
        print("  ", row)
    print()
def main():
    # Пример входных матриц (можно заменить на ввод с клавиатуры)
    A = [
        [1, 5, 3],
        [8, 2, 7],
        [4, 6, 9]
    ]
    B = [
        [10, 3, 8],
        [2, 15, 1],
        [7, 4, 6]
    ]
    print("Исходные матрицы:")
    print_matrix(A, "Матрица A")
    print_matrix(B, "Матрица B")
    # Меняем максимальные элементы
    swap_max_elements(A, B)
    print("Матрицы после обмена максимальных элементов:")
    print_matrix(A, "Матрица A")
    print_matrix(B, "Матрица B")
if __name__ == "__main__":
    main()

# ВАРИАНТ 12(2)

def med(m, n, k):
    global a, b, c
    a = (2*(n**2+k**2)-m**2)**0.5/2
    b = (2*(m**2+k**2)-n**2)**0.5/2
    c = (2*(m**2+n**2)-k**2)**0.5/2
a, b, c = map(float, input().split())
if a<b+c and b<a+c and c<a+b:
    med(a, b, c)
    med(a, b, c)
    print(round(a, 2), round(b, 2), round(c, 2))
else:
    print('треугольник с такими сторонами не существует')

# ВАРИАНТ 13(2)

def acos(x, y) :
    return x  / ((x * x + y * y) ** 0.5)
###################
# вариант 1 для трех точек
x1, x2 = map(float,input().split())
y1, y2 = map(float,input().split())
z1, z2 = map(float,input().split())
res = [x1, x2]
acosx = acos(x1, x2)
acosy = acos(y1, y2)
if acosy > acosx :
    acosx = acosy
    res = [y1, y2]
acosz = acos(z1, z2)
if acosz > acosx :
    acosz = acosz
    res = [z1, z2]
print(*res)
###########
# вариант 2 для "n" точек
n = 3
res = [tuple(map(float,input().split())) for i in range(n)]
rcos = [acos(*res[i]) for i in range(n)]
k = rcos.index(max(rcos))
print(res[k])

# ВАРИАНТ 14(2)

import math
def distance(point1, point2):
    """
    Процедура: вычисляет расстояние между двумя точками на плоскости.
    point1, point2 — кортежи (x, y).
    Возвращает: расстояние (float).
    """
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
def find_max_distance(points):
    """
    Находит пару точек с максимальным расстоянием между ними.
    points — словарь {имя: (x, y)}.
    Возвращает: (имя1, имя2, max_distance)
    """
    max_dist = -1
    pair = (None, None)
    # Перебираем все пары точек
    for name1, coord1 in points.items():
        for name2, coord2 in points.items():
            if name1 != name2:
                dist = distance(coord1, coord2)
                if dist > max_dist:
                    max_dist = dist
                    pair = (name1, name2)
    
    return pair[0], pair[1], max_dist
def main():
    print("Введите координаты четырёх точек (x, y):")
    try:
        # Ввод точек
        x1 = float(input("X, x1 = "))
        x2 = float(input("X, x2 = "))
        y1 = float(input("Y, y1 = "))
        y2 = float(input("Y, y2 = "))
        z1 = float(input("Z, z1 = "))
        z2 = float(input("Z, z2 = "))
        p1 = float(input("P, p1 = "))
        p2 = float(input("P, p2 = "))
        # Словарь точек: имя → (x, y)
        points = {
            'X': (x1, x2),
            'Y': (y1, y2),
            'Z': (z1, z2),
            'P': (p1, p2)
        }
        # Находим максимальное расстояние
        name1, name2, max_dist = find_max_distance(points)
        print(f"\nМаксимальное расстояние: {max_dist:.4f}")
        print(f"Между точками: {name1} и {name2}")
    except ValueError:
        print("Ошибка: введите числовые значения.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
if __name__ == "__main__":
    main()

# ВАРИАНТ 15(2)

import math
def distance(point1, point2):
    """
    Процедура: вычисляет расстояние между двумя точками в 3D-пространстве.
    point1, point2 — кортежи (x, y, z).
    Возвращает: расстояние (float).
    """
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
def find_min_distance(points):
    """
    Находит пару точек с минимальным расстоянием между ними.
    points — словарь {имя: (x, y, z)}.
    Возвращает: (имя1, имя2, min_distance)
    """
    if len(points) < 2:
        raise ValueError("Нужно минимум две точки.")
    min_dist = float('inf')  # начальное значение — «бесконечность»
    pair = (None, None)
    # Перебираем все уникальные пары точек
    for name1, coord1 in points.items():
        for name2, coord2 in points.items():
            if name1 != name2:
                dist = distance(coord1, coord2)
                if dist < min_dist:
                    min_dist = dist
                    pair = (name1, name2)
    
    return pair[0], pair[1], min_dist
def main():
    print("Введите координаты четырёх точек в 3D (x, y, z):")
    try:
        # Ввод точки X
        x1 = float(input("X, x1 = "))
        x2 = float(input("X, x2 = "))
        x3 = float(input("X, x3 = "))
        # Ввод точки Y
        y1 = float(input("Y, y1 = "))
        y2 = float(input("Y, y2 = "))
        y3 = float(input("Y, y3 = "))
        # Ввод точки Z
        z1 = float(input("Z, z1 = "))
        z2 = float(input("Z, z2 = "))
        z3 = float(input("Z, z3 = "))
        # Ввод точки T
        t1 = float(input("T, t1 = "))
        t2 = float(input("T, t2 = "))
        t3 = float(input("T, t3 = "))
        # Словарь точек: имя → (x, y, z)
        points = {
            'X': (x1, x2, x3),
            'Y': (y1, y2, y3),
            'Z': (z1, z2, z3),
            'T': (t1, t2, t3)
        }
        # Находим минимальное расстояние
        name1, name2, min_dist = find_min_distance(points)
        print(f"\nМинимальное расстояние: {min_dist:.4f}")
        print(f"Между точками: {name1} и {name2}")
    except ValueError:
        print("Ошибка: введите числовые значения.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
if __name__ == "__main__":
    main()