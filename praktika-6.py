# ПРАКТИЧЕСКАЯ 6
# ВАРИАНТ 1(1)

# 1. Ввод размера массива
n = int(input("Введите количество элементов массива (N): "))
# 2. Создание и заполнение массива
array = []
for i in range(n):
    element = int(input(f"Введите элемент {i + 1}: "))
    array.append(element)
# 3. Нахождение максимального элемента
max_element = max(array)
# 4. Вывод массива в обратном порядке
reversed_array = array[::-1]  # срез с шагом -1
# 5. Вывод результатов
print("\nИсходный массив:", array)
print("Массив в обратном порядке:", reversed_array)
print("Максимальный элемент:", max_element)

# ВАРИАНТ 2(1)

# 1. Ввод размера массива
n = int(input("Введите количество элементов массива (N): "))
# 2. Создание и заполнение массива
array = []
for i in range(n):
    element = int(input(f"Введите элемент {i + 1}: "))
    array.append(element)
# 3. Нахождение минимального элемента и его индекса
min_element = array[0]      # предполагаем, что первый элемент — минимальный
min_index = 0              # индекс минимального элемента
for i in range(1, n):
    if array[i] < min_element:
        min_element = array[i]
        min_index = i
# 4. Вывод результатов
print("\nИсходный массив:", array)
print("Минимальный элемент:", min_element)
print("Индекс минимального элемента:", min_index)

# ВАРИАНТ 3(1)

# 1. Ввод размера массива
n = int(input("Введите количество элементов массива (n): "))
# 2. Создание и заполнение массива
D = []
for i in range(n):
    element = int(input(f"Введите элемент {i + 1}: "))
    D.append(element)
# 3. Вычисление суммы элементов с нечётными индексами
sum_odd_indices = 0
for i in range(1, n, 2):  # начинаем с 1, шаг 2 → 1, 3, 5, ...
    sum_odd_indices += D[i]
# 4. Вывод результатов
print("\nМассив D:", D)
print("Сумма элементов с нечётными индексами:", sum_odd_indices)

# ВАРИАНТ 4(1)

arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
max_value = max(arr)
max_index = arr.index(max_value)
print(f"Максимальный элемент: {max_value}")
print(f"Его индекс (порядковый номер): {max_index}")

# ВАРИАНТ 5(1)

# Ввод 10 чисел
print("Введите 10 целых чисел:")
arr = []
for i in range(10):
    num = int(input(f"Число {i+1}: "))
    arr.append(num)
# Поиск и вывод пар отрицательных чисел, стоящих рядом
print("Пары отрицательных чисел, стоящих рядом:")
found = False
for i in range(len(arr) - 1):
    if arr[i] < 0 and arr[i + 1] < 0:
        print(f"({arr[i]}, {arr[i + 1]})")
        found = True
if not found:
    print("Таких пар нет.")

# ВАРИАНТ 6(1)

# Ввод 10 чисел
print("Введите 10 целых чисел:")
arr = []
for i in range(10):
    num = int(input(f"Число {i+1}: "))
    arr.append(num)
# Находим максимальный элемент
max_element = arr[0]
for num in arr:
    if num > max_element:
        max_element = num
# Считаем элементы меньше и больше максимума
count_less = 0
count_greater = 0
for num in arr:
    if num < max_element:
        count_less += 1
    elif num > max_element:
        count_greater += 1
# Вывод результатов
print(f"\nМаксимальный элемент: {max_element}")
print(f"Количество элементов меньше максимального: {count_less}")
print(f"Количество элементов больше максимального: {count_greater}")

# ВАРИАНТ 7(1)

arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
sum_even = 0      # сумма элементов с чётными индексами
product_odd = 1   # произведение элементов с нечётными индексами
has_odd = False # флаг: были ли нечётные индексы
for i in range(len(arr)):
    if i % 2 == 0:           # чётный индекс (0, 2, 4, ...)
        sum_even += arr[i]
    else:                     # нечётный индекс (1, 3, 5, ...)
        product_odd *= arr[i]
        has_odd = True
# Если не было нечётных индексов, произведение считаем как 0 (или можно оставить 1)
if not has_odd:
    product_odd = 0
print(f"Сумма элементов с чётными номерами (индексами): {sum_even}")
print(f"Произведение элементов с нечётными номерами (индексами): {product_odd}")

# ВАРИАНТ 8(1)

# Ввод списка чисел
numbers = list(map(int, input("Введите числа через пробел: ").split()))
# Инициализация
sum_total = 0
product = 1
# Проход по элементам
for num in numbers:
    sum_total += num
    product *= num
# Вывод результатов
print(f"Сумма элементов: {sum_total}")
print(f"Произведение элементов: {product}")

# ВАРИАНТ 9(1)

# 1. Ввод размера массива
n = int(input("Введите количество элементов массива (N): "))
# 2. Ввод элементов массива с клавиатуры
arr = []
print("Введите элементы массива (вещественные числа):")
for i in range(n):
    element = float(input(f"Элемент {i + 1}: "))
    arr.append(element)
# 3. Поиск минимального по модулю элемента
min_abs_value = abs(arr[0])  # модуль первого элемента
min_abs_element = arr[0]   # сам элемент (сохраняем значение, а не только модуль)
for element in arr:
    if abs(element) < min_abs_value:
        min_abs_value = abs(element)
        min_abs_element = element
# 4. Вывод минимального по модулю элемента
print(f"\nМинимальный по модулю элемент: {min_abs_element} (модуль = {min_abs_value})")
# 5. Вывод массива в обратном порядке
print("Массив в обратном порядке:", arr[::-1])

# ВАРИАНТ 10(1)

lst = list(map(int, input("Введите элементы списка через пробел: ").split()))
# Считаем, сколько раз встречается каждый элемент
freq = {}
for item in lst:
    freq[item] = freq.get(item, 0) + 1
# Находим элементы, которые встречаются больше одного раза
duplicates = [key for key, value in freq.items() if value > 1]
if duplicates:
    print("Повторяющиеся элементы:", duplicates)
else:
    print("Повторяющихся элементов нет.")

# ВАРИАНТ 11(1)

lst = list(map(int, input("Введите элементы списка через пробел: ").split()))
# Отбираем чётные числа (делятся на 2 без остатка)
even_numbers = [x for x in lst if x % 2 == 0]
if even_numbers:
    max_even = max(even_numbers)
    print(f"Наибольший чётный элемент: {max_even}")
else:
    print("Чётных элементов нет.")

# ВАРИАНТ 12(1)

lst = list(map(int, input("Введите элементы списка через пробел: ").split()))
# Отбираем нечётные числа
odd_numbers = [x for x in lst if x % 2 != 0]
if odd_numbers:
    min_odd = min(odd_numbers)
    print(f"Наименьший нечётный элемент: {min_odd}")
else:
    print("Нечётных элементов нет.")

# ВАРИАНТ 13(1)

arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
# Словарь: ключ — значение элемента, значение — список индексов
indices = {}
for idx, value in enumerate(arr):
    if value not in indices:
        indices[value] = []
    indices[value].append(idx)
# Выводим только элементы, которые встречаются >1 раза
found_duplicates = False
for value, idx_list in indices.items():
    if len(idx_list) > 1:
        found_duplicates = True
        print(f"Элемент {value} встречается на позициях: {idx_list}")
if not found_duplicates:
    print("Одинаковых элементов нет.")

# ВАРИАНТ 14(1)

arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
if len(arr) == 0:
    print("Массив пуст!")
else:
    # Находим значения и их индексы
    max_val = max(arr)
    min_val = min(arr)
    max_idx = arr.index(max_val)
    min_idx = arr.index(min_val)

    # Меняем местами
    arr[max_idx], arr[min_idx] = arr[min_idx], arr[max_idx]
    print(f"Массив после замены: {arr}")

# ВАРИАНТ 15(1)

lst = list(map(int, input("Введите элементы списка через пробел: ").split()))
# Считаем, сколько раз встречается каждый элемент
freq = {}
for item in lst:
    freq[item] = freq.get(item, 0) + 1
# Находим элементы, которые встречаются больше одного раза
duplicates = [key for key, value in freq.items() if value > 1]
if duplicates:
    print("Повторяющиеся элементы:", duplicates)
else:
    print("Повторяющихся элементов нет.")