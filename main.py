from defin.the_function import *
from defin.the_function2 import *


def lab1():
    print('Введите номер задания (1-9)')
    iter = int(input())
    if iter == 1:
        first()  # -1
    elif iter == 2:
        second()  # -2
    elif iter == 3:
        third()  # -3
    elif iter == 4:
        forth()  # -4
    elif iter == 5:
        fifth()  # -5
    elif iter == 6:
        sixth()  # -6
    elif iter == 7:
        seventh()  # -7
    elif iter == 8:
        eight()  # -8
    elif iter == 9:
        nineth()  # -9


def lab2():
    print('Введите номер задания (5.1 - 1, 5.1a - 2, 5.1b - 3, 2)')
    iter = int(input())
    if 1 <= iter <= 2:
        print('Введите ip-адрес формата "10.0.1.1" ')
        str = input()
        if iter == 1:
            Fd1(str)
        elif iter == 2:
            Fd1a(str)
        elif iter == 3:
            Fd1b(str)
    if iter == 3: Fd2()

#надо затестить первые задания 2 лабы
while True:
    print('Введите номер лабораторной, 5 - Выход')
    a = int(input())
    if 1 == a:
        lab1()
    elif 2 == a:
        lab2()
    elif 5 == a:
        print('Выход')
        break
