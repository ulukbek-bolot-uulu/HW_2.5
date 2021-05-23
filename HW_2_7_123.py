
class Phone:
    def __init__(self, model, camera, cost):
        self.model = model
        self.camera = camera
        self.cost = cost

    def specification(self):
        return self.model, self.camera, self.cost


ph_1 = Phone('OnePlus', '100 Mpx', 1000)
ph_1.specification()
print(ph_1.specification())


# Task 2


class Monkey:
    max_age = 12
    loves_bananas = True

    def climb(self):
        print('I am climbing the tree')


monkey1 = Monkey()
print(monkey1.max_age, monkey1.loves_bananas)
monkey2 = Monkey()
print(monkey2.max_age, monkey2.loves_bananas)
monkey1.climb()
monkey2.climb()





# Task 3

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def calculate_age(self, year):
        self.year = year
        willbe = self.age + year
        print(f'Через {year} лет {p.name} будет {willbe} лет')

p = Person('John', 23, 'male')
p.calculate_age(int(input('Введите число: ')))





