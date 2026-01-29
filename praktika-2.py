# ПРАКТИЧЕСКАЯ 2
# ЗАДАНИЕ 1 ВАРИАНТ 1

import math
# Запрос значений переменных у пользователя
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
z = float(input("Введите значение z: "))
# Вычисление выражения
numerator = 2 * math.cos(x - 2/3)  # числитель дроби
denominator = 0.5 + math.sin(y) ** 2  # знаменатель дроби
fraction = numerator / denominator  # результат деления числителя на знаменатель
# Вычисление второй части выражения (в скобках)
z_squared = z ** 2
denominator_inner = 3 - z_squared / 5
bracket_part = 1 + z_squared / denominator_inner
# Итоговое значение s
s = fraction * bracket_part
# Вывод результата с двумя знаками после запятой
print(f"Результат вычисления s: {s:.2f}")

# ЗАДАНИЕ 2 ВАРИАНТ 7

import math
# Запрос значений переменных у пользователя
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
z = float(input("Введите значение z (например, 3.25e-4 для 3.25×10⁻⁴): "))
# Вычисляем отдельные части формулы
arctg_part = 5 * math.atan(x)  # 5 * arctg(x)
arccos_part = (1/4) * math.acos(x)  # (1/4) * arccos(x)
# Числитель дроби
numerator = x + 3 * abs(x - y) + x**2
# Знаменатель дроби
denominator = abs(x - y) * z + x**2
# Дробная часть выражения
fraction_part = numerator / denominator
# Итоговое значение s
s = arctg_part - arccos_part * fraction_part
# Вывод результата с двумя знаками после запятой
print(f"Результат вычисления s: {s:.2f}")