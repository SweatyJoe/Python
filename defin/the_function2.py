def Fd1(str):
    str = str.split('.')
    i = int(str[0])
    zero, cap = 0, 0
    for iter in str:
        if int(iter) == 0:
            zero += 1
        elif int(iter) == 255:
            cap += 1
        else:
            break
    if zero == 4:
        print('unassigned')
    elif cap == 4:
        print('local broadcast')
    if 1 <= i <= 233:
        print('unicast')
    elif 224 <= i <= 239:
        print('multicast')
    else:
        print('unused')


def Fd1a(str):
    while True:
        pop = 0
        a = str.split('.')
        for i in a:
            if 0 <= i <= 255:
                pop += 1
            else:
                print('Incorrect IPv4 address: Число вне диапозона')
                return 0
        if pop != 4:
            print('Incorrect IPv4 address: Ошибка кличества')
            return 0
        else:
            print('всё ок, запуск сканирования...')
            Fd1(str)
        return 0


def Fd1b(str):
    while True:
        pop = 0
        a = str.split('.')
        for i in a:
            if 0 <= int(i) <= 255:
                pop += 1
            else:
                print('Incorrect IPv4 address: Число вне диапозона')
                break
        if pop != 4:
            print('Incorrect IPv4 address: Ошибка кличества')
        else:
            print('всё ок, запуск сканирования...')
            Fd1(str)
            return 0
        print('Введите ip-адресс заново: ')
        str = input()


def Fd2():
    mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
    print(mac)
    mac_cisco = []
    for mac_iter in mac:
        mac_cisco.append(mac_iter.replace(':', '.'))
    print(mac_cisco)