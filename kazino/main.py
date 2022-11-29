

#
# import random
# """ namber = 1...36  X 2
#  попыток = 2
#  выйгрыш то 1 Х 1
#  0 Х 1 то (1 Х 1) Х 2
# """
#
#
# number = []
# #number.append('0')
#
# for i in range(1, 37):
#     number.append(str(i))
# print(number * 2)
#
# print(random.choice(number))

# all_number = [i for i in range(1, 37)]
# colors = ['Красный', 'Черный']
# ruletka = ['0:Зеленый']
# stavka = int(12)
# lucky = input('Поставьте на какое-то число и цвет (пример: 16:Красный) --> ')
# win = 0
#
# for i in all_number:
#     for j in colors:
#         ruletka.append(f'{i}:{j}')
# print(ruletka)