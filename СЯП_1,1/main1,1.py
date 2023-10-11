import math
# Ввод начала диапазона с проверкой на целочисленный ввод
while True:
    try:
        begin = int(input("Введите начало диапазона: "))
        break
    except ValueError:
        print("Ошибка! Введите целое число.")

# Ввод конца диапазона с проверкой на целочисленный ввод
while True:
    try:
        end = int(input("Введите конец диапазона: "))
        break
    except ValueError:
        print("Ошибка! Введите целое число.")

if begin > end:
    begin, end = end, begin
for i in range(begin, end+1):
    is_prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime and i > 1:
        print(i)