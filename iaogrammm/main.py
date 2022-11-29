

Steve = Student(\"Steven Schultz\", 23, \"English\")" \
Johnny = Student(\"Jonathan Rosenberg\", 24, \"Biology\")" \
Penny = Student(\"Penelope Meramveliotakis\", 21, \"Physics\")" \

print(Steve)\r\n<name: Steven Schultz, age: 23, major: English>
print(Johnny)\r\n<name: Jonathan Rosenberg, age: 24, major: Biology>"





class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        if not isinstance(self.name , str):
            raise  TypeError('Не правильная ссылка')

        elif name == 'Steve':
            self.name = 'Steven Schultz'
            self.age = 23
            self.major = 'English'
        elif name == 'Johnny':
            self.name = 'Jonathan Rosenberg'
            self.age = 24
            self.major = 'Biology'
        elif name == 'Penny':
            self.name = 'Penelope Meramveliotakis'
            self.age = 21
            self.major = 'Physics'
        else:
            print("нет таких студентов")
