# Напишите программу, где исходный список содержит положительные и отрицательные числа.
# Требуется положительные поместить в один список, а отрицательные - в другой.

list_ = [-6, -5, -4, -3, 1, 2, 3, 4, 5, -6, 7, 8, 9, -1, -2, -3, -4, -5, 4, 5, 6, 7, -6, -7, -8, -9]

positive = []
negative = []

for i in list_:
    if i > 0:
        positive.append(i)
    elif i < 0:
        negative.append(i)
    else:
        print('TypeError')

print(f"общий список: {list_}")
print(f"положительные: {positive}")
print(f"отрицательные: {negative}")

