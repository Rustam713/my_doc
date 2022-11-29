# Напишите функцию которая принимает два аргумента (числа), умножает их друг на друга,
# и возвращает функцию, которая также берет два аргумента (числа),
# и возвращает результат умножения аргументов внешней функции плюс результат деления
# аргументов внутренней функции.
# Подсказка: (outer_arg1 * outer_arg2) + (inner_arg1 / inner_arg2)




def outer():
    outer_arg1 = int(input('ведите 1-мгож число: '))
    outer_arg2 = int(input('ведите 2-множ число: '))

    def inner():
        inner_arg1 = int(input('ведите делимое число: '))
        inner_arg2 = int(input('ведите делитель числа: '))

        sum_arg = print(outer_arg2 * outer_arg1 + (inner_arg1 / inner_arg2))

        return sum_arg

    inner()
outer()

