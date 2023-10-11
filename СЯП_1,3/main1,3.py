n = int(input("Введите количество чисел: "))
numbers = []
cubes = []

for i in range(n):
    num = int(input("Введите число: "))
    numbers.append(num)
    cubes.append(num ** 3)

sum_of_cubes = sum(cubes)
product_of_cubes = 1
for cube in cubes:
    product_of_cubes *= cube

reversed_list = list(reversed(cubes))

print("Список кубов чисел:", cubes)
print("Сумма кубов чисел:", sum_of_cubes)
print("Произведение кубов чисел:", product_of_cubes)
print("Список кубов чисел в обратном порядке:", reversed_list)