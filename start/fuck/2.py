# Банкомат
# Напишите код банкомата, который принимает цифру,
# выдает деньги с номиналом 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1.

def atm():
    cash = {
        'five_th' : int == 0,
        'two_th' : int == 0,
        'one_th' : int == 0,
        'five_hun' : int == 0,
        'two_hun' : int == 0,
        'one_hun' : int == 0,
        'fifty' : int == 0,
        'twenty' : int == 0,
        'ten' : int == 0,
        'five' : int == 0,
        'three' : int == 0,
        'one' : int == 0
    }


    number = int(input("ведите желаемую сумму: "))

    while True:

        if number >= 5000:
            number -= 5000
            cash['five_th'] += 1


        if number >= 2000:
            number -= 2000
            cash['two_th'] += 1


        if number >= 1000:
            number -= 1000
            cash['one_th'] += 1


        if number >= 500:
            number -= 500
            cash['five_hun'] += 1


        if number >= 200:
            number -= 200
            cash['two_hun'] += 1


        if number >= 100:
            number -= 100
            cash['one_hun'] += 1


        if number >= 50:
            number -= 50
            cash['fifty'] += 1


        if number >= 20:
            number -= 20
            cash['twenty'] += 1


        if number >= 10:
            number -= 10
            cash['ten'] += 1


        if number >= 5:
            number -= 5
            cash['five'] += 1


        if number >= 3:
            number -= 3
            cash['three'] += 1


        if number >= 1:
            number -= 1
            cash['one'] += 1


        else:
            break


    print(f"выдано наличными {cash}")

atm()
