# ПРАКТИЧЕСКАЯ 4
# ЗАДАНИЕ 1

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
for i in range(A, B + 1):
    print(i)

# ЗАДАНИЕ 2

A = int(input("Введите A: "))
B = int(input("Введите B: "))
if A < B:
    # Возрастающий порядок: от A до B (включительно)
    for i in range(A, B + 1):
        print(i)
else:
    # Убывающий порядок: от A до B (включительно)
    for i in range(A, B - 1, -1):
        print(i)

# ЗАДАНИЕ 3

A = int(input("Введите A (большее число): "))
B = int(input("Введите B (меньшее число): "))
for i in range(A, B - 1, -1):  # от A до B включительно, шаг −1
    if i % 2 == 1:  # нечётное: остаток от деления на 2 равен 1
        print(i)

# ЗАДАНИЕ 4

try:
    n = int(input("Сколько чисел? "))
    total = 0
    for _ in range(n):
        total += int(input("Число: "))
    print("Сумма:", total)
except ValueError:
    print("Ошибка: введите целые числа!")

# ЗАДАНИЕ 5

n = int(input("Введите n: "))
total = 0
for i in range(1, n + 1):
    total += i ** 3
print(total)

# ЗАДАНИЕ 6

n = int(input("Введите n: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i
print(factorial)

# ЗАДАНИЕ 7

n = int(input("Введите n: "))
total_sum = 0      # Общая сумма факториалов
current_fact = 1  # Текущий факториал (начинаем с 0! = 1)
for i in range(1, n + 1):
    current_fact *= i      # Вычисляем i! = (i-1)! * i
    total_sum += current_fact  # Добавляем i! к общей сумме

print(total_sum)

# ЗАДАНИЕ 8

n = int(input("Введите n (≤ 9): "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()  # переход на новую строку после каждой ступеньки

# ЗАДАНИЕ 9

n = int(input("Введите N (количество чисел Фибоначчи): "))
if n <= 0:
    print(0)
elif n == 1:
    print(1)
else:
    a, b = 1, 1  # Первые два числа Фибоначчи
    total_sum = a + b  # Сумма первых двух

    for _ in range(2, n):
        next_fib = a + b
        total_sum += next_fib
        a, b = b, next_fib  # Сдвигаем пару для следующего шага
    print(total_sum)

# ЗАДАНИЕ 10

try:
    n = int(input("Введите N (количество чисел для суммы): "))
    k = int(input("Введите K (номер первого числа в ряду): "))
    if n <= 0 or k < 1:
        print(0)
    else:
        # Начальные числа Фибоначчи
        a, b = 1, 1  # F₁ = 1, F₂ = 1
        total_sum = 0
        count = 0  # счётчик чисел, которые мы «проходим»
        while count < k + n - 1:
            count += 1

            # Если достигли K-го числа или дальше — начинаем суммировать
            if count >= k:
                total_sum += a

            # Переходим к следующему числу Фибоначчи
            a, b = b, a + b

        print(total_sum)
except ValueError:
    print("Ошибка: введите целые числа!")

