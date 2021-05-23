# Task 2
import random

names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt',
         'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt',
         'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt',
         'fhjhafhdfa.txt']

ran_file = random.choice(names)
print(ran_file)
f = open(ran_file, 'w')


def func(names):
    for ran_file in names:
        try:
            with open (ran_file, 'r') as a:
                print('Hey')
            f = open(ran_file, 'w')
            f.write('Ulukbek')
            f.close()
        except FileNotFoundError:
            print("Такого файла не существует!")


func(names)
