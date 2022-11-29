number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = 7

# def index(numbers, c):
#     das = []
#     for i in range(len(numbers)):
#         for j in numbers[i + 1: len(numbers)]:
#             if numbers[i] + j == c:
#                 print(numbers[i], j)
#                 das.append([numbers[i], j])
#                 break
#     print(das)
#
# index(number, c)


def two_sum(array, k):

    s = set()

    for n in array:
        if k-n in s:
            return k-n, n
        s.add(k-n)
    print(s)
    return ()

print(two_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))












# numbe = set(number)
#
# print(numbe)
#
# a = random.choices(numbe)
# b = numbe.pop()
# print(a, b)
# print(numbe)
# import random
# print(number)
#
# def index():
#     while True:
#         aiGuess = random.choice(number)
#         ajGuess = random.choice(number)
#         if aiGuess + ajGuess == 8:
#             print(aiGuess, ajGuess, 'uuuuuuuuuuuurrrrrrrrrrrraaaaaaaaaaaaaa')
#             number.pop(index(aiGuess))
#             number.pop(index(ajGuess))
#             print(number)
#         else:
#             pass
#
#
#
# index()
