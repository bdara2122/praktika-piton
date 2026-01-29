# ПРАКТИЧЕСКАЯ 5
# ЗАДАНИЕ 1

text = input("Введите текст: ")
count = 0

for word in text.split():
    if word.lower().startswith('е'):
        count += 1
print(count)


# ЗАДАНИЕ 2

text = input("Введите строку: ")
old_char = ':'
new_char = '%'
# Заменяем и получаем новую строку
new_text = text.replace(old_char, new_char)
# Количество замен = разница длин (или можно просто посчитать вхождения)
count = text.count(old_char)
print("Изменённая строка:", new_text)
print("Количество замен:", count)

# ЗАДАНИЕ 3

text = input("Введите строку: ")
removed_count = text.count('.')
new_text = text.replace('.', '')
print("Изменённая строка:", new_text)
print("Количество удалённых точек:", removed_count)

# ЗАДАНИЕ 4

text = input("Введите строку: ")
# Заменяем 'а' и 'А' на 'о'
new_text = text.replace('а', 'о').replace('А', 'о')
# Количество замен = разница в количестве букв 'а'/'А' между исходной и новой строкой
count_replaced = text.count('а') + text.count('А')
# Общее количество символов в исходной строке
total_chars = len(text)
print("Изменённая строка:", new_text)
print("Количество замен:", count_replaced)
print("Общее количество символов:", total_chars)

# ЗАДАНИЕ 5

text = input("Введите строку: ")
result = text.lower()
print("Результат:", result)

# ЗАДАНИЕ 6

text = input("Введите строку: ")
# Считаем количество удаляемых букв
count_removed = text.count('а') + text.count('А')
# Удаляем все 'а' и 'А'
new_text = text.replace('а', '').replace('А', '')
print("Изменённая строка:", new_text)
print("Количество удалённых букв 'а'/'А':", count_removed)

# ЗАДАНИЕ 7

text = input("Введите строку: ")
n = len(text)
half = n // 2  # Целая часть от n/2 (для нечётных n)
# Берём первую половину строки, заменяем 'п' и 'П' на '*'
first_half_replaced = text[:half].replace('п', '*').replace('П', '*')
# Соединяем с оставшейся частью строки
result = first_half_replaced + text[half:]
print("Результат:", result)

# ЗАДАНИЕ 8

text = input("Введите строку (должна заканчиваться точкой): ")
# Удаляем точку в конце (если есть), затем разбиваем на слова
words = text.rstrip('.').split()
word_count = len(words)
print("Количество слов:", word_count)

# ЗАДАНИЕ 9

text = input("Введите текст: ")
word = input("Какое слово искать: ")
count = text.count(word)
print(f"Слово '{word}' встречается {count} раз(а)")

# ЗАДАНИЕ 10

text = input("Введите предложение на английском: ")
result = text.title()
print("Результат:", result)

# ЗАДАНИЕ 11

text = input("Введите строку: ")
# 1. Находим самую длинную последовательность букв «н»
max_length = 0
current_length = 0
for char in text:
    if char == 'н':
        current_length += 1
        if current_length > max_length:
            max_length = current_length
    else:
        current_length = 0
print(f"Самая длинная последовательность букв «н»: {max_length} символов")
# 2. Заменяем все восклицательные знаки на точки
transformed_text = text.replace('!', '.')
print("Преобразованная строка (восклицательные знаки → точки):", transformed_text)

# ЗАДАНИЕ 12

text = input("Введите строку: ")
words = text.split()
result = []
for word in words:
    if word.endswith('я'):  # или: word[-1] == 'я'
        result.append(word)
print("Слова, оканчивающиеся на «я»:", result)

# ЗАДАНИЕ 13

text = input("Введите строку: ")
start = text.find('(')
end = text.find(')')
if start != -1 and end != -1 and start < end:
    result = text[start + 1:end]
    print("Символы внутри скобок:", result)
else:
    print("Скобки не найдены или расположены неверно.")

# ЗАДАНИЕ 14

text = input("Введите строку: ")
words = text.split()
result = []
for word in words:
    if word.startswith('а') or word.endswith('я'):
        result.append(word)
print("Слова, начинающиеся на «а» или заканчивающиеся на «я»:", result)

# ЗАДАНИЕ 15

text = input("Введите строку: ")
count = text.count('т')
print(f"Количество букв «т»: {count}")