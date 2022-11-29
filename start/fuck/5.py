# Дано dict_one = {'a':1, 'b':2, 'c':3}
# dict_two = {'d':4, 'e':5, 'f':6}
# dict_three = {'g':7, 'h':8, 'i':9}
# dict_four = {}
# С помощью цикла for необходимо собрать три первых словаря в словарь dict_four

# Подсказка: Для удобства итерации, первые три словаря можно записать в кортеж (dict_one, dict_two, dict_three

dict_one = {'a':1, 'b':2, 'c':3}
dict_two = {'d':4, 'e':5, 'f':6}
dict_three = {'g':7, 'h':8, 'i':9}
dict_four = {}

cotej = (dict_one, dict_two, dict_three)

for i in cotej:
    for key, values in i.items():
        dict_four.update({key: values})

print(dict_four)
