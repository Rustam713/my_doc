"""a) поля fullName, age, place(address)
б) метод talk(), в которых просто вывести на консоль сообщение -"Такой-то  Person говорит". Метод

move()  будет менять его адрес
в) Добавьте  конструктор  с тремя параметрами fullName, address, age = 18
г) Настроить  метод __str__  (Сделать отображение всех полей объекта)
"""


class Person():
    fullName = 'rustam'
    age = 19
    place = 'tagai-bei 79'

    def __init__(self, fullName='rustam', age=19, place='tagai-bei 79'):
        self.fullName = fullName
        self.age = age
        self.place = place

    def talk(self):
        print(f'{self.fullName} говорит что ему {self.age} лет, и живет он по адресу {self.place}')

    def move(self):
        self.place = 'depovskay 56'
        print(f'{self.fullName} говорит что ему {self.age} лет, и живет он по адресу {self.place}')

    def __str__(self):
        pass



rus = Person()
print(rus.talk())
print(rus.move())