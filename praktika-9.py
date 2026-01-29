# ПРАКТИЧЕСКАЯ 9

with open('WWOD', 'r') as f:
    n, m = map(int, f.readline().split())
    matrix = [list(map(int, f.readline().split())) for _ in range(n)]

sums = [sum(row) for row in matrix]
max_i = sums.index(max(sums))
min_i = sums.index(min(sums))

with open('WWOD', 'w') as f:
    for row in matrix:
        f.write(' '.join(map(str, row)) + '\n')
    f.write('Строка с наибольшей суммой: ' + ' '.join(map(str, matrix[max_i])) + '\n')
    f.write('Ее сумма: ' + str(sums[max_i]) + '\n')
    f.write('Строка с наименьшей суммой: ' + ' '.join(map(str, matrix[min_i])) + '\n')
    f.write('Ее сумма: ' + str(sums[min_i]))