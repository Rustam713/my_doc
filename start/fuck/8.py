# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).


def season(number):

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    month = months[number-1]
    print(month)
    if month in 'January February December':
        print('winter')
    if month in 'March April May':
        print('spring')
    if month in 'June July August':
        print('summer')
    if month in 'September October November':
        print('autumn')


season(int(input('enter a number from 1 to 12: ')))
