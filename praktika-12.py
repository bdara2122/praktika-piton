# ПРАКТИЧЕСКАЯ 12
# БЛОК А 1

import math

def calculate_expression(x, n):
    """
    Вычисляет значение выражения x^n / n!
    
    Параметры:
        x (int): натуральное число (основание степени)
        n (int): натуральное число (показатель степени и аргумент факториала)
    
    Возвращает:
        float: результат вычисления x^n / n!
    """
    if x <= 0 or n <= 0:
        raise ValueError("x и n должны быть натуральными числами (больше 0).")
    
    
    # Вычисляем x в степени n
    power = x ** n
    
    # Вычисляем факториал n
    factorial = math.factorial(n)
    
    # Возвращаем результат деления
    return power / factorial

def main():
    try:
        # Ввод данных от пользователя
        x = int(input("Введите натуральное число x: "))
        n = int(input("Введите натуральное число n: "))
        
        
        # Вычисление результата
        result = calculate_expression(x, n)
        
        # Вывод результата
        print(f"Результат выражения {x}^{n} / {n}! = {result}")
        
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()

# БЛОК Б (4)

import math

def is_prime(n, divisor=2):
    """
    Рекурсивно проверяет, является ли n простым.
    
    Параметры:
        n (int) — проверяемое число (n > 1).
        divisor (int) — текущий делитель для проверки (по умолчанию 2).
    
    Выводит:
        "YES", если n простое; "NO", если составное.
    """
    # Базовый случай 1: нашли делитель — число составное
    if divisor * divisor > n:
        print("YES")
        return
    
    # Базовый случай 2: n делится на divisor — число составное
    if n % divisor == 0:
        print("NO")
        return
    
    # Рекурсивный вызов для следующего делителя
    is_prime(n, divisor + 1)



def main():
    try:
        n = int(input())
        if n <= 1:
            print("NO")  # По условию n > 1, но на всякий случай
        else:
            is_prime(n)
    except ValueError:
        print("Ошибка: введите целое число.")


if __name__ == "__main__":
    main()
