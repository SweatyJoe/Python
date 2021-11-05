# просто добавил func'ционал
def first():
    print('3.1')
    NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
    print('--' + NAT, '--' + NAT.replace('Fast', 'Gigabit'), sep='\n')


def second():
    MAC = 'AAAA:BBBB:CCCC'
    print('\n3.2')
    print('--' + MAC, '--' + MAC.replace(':', '.'), sep='\n')


def third():
    print('\n3.3')
    CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
    cse = CONFIG.strip(',').split(' ')[-1]
    print('--' + CONFIG, '--' + cse, sep='\n')


def forth():
    print('\n3.4')
    command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
    command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
    cm1 = set(command1.split(' ')[-1].split(','))
    cm2 = set(command2.split(' ')[-1].split(','))
    answ = list(cm1.intersection(cm2))
    print('--', answ, sep='')


def fifth():
    print('\n3.5')
    VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
    VLANS = sorted(set(VLANS))
    print('--', VLANS, sep='')


def sixth():
    print('\n3.6')
    ospf_route = 'OSPF 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
    keys = ('Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface')
    ospf_route = ospf_route.replace(',', '').replace('[', '').replace(']', '')
    out = ospf_route.split(' ')
    out.remove(out[3])  # удаляем слово "via"
    dictionary = dict(zip(keys, out))
    print(dictionary)


def seventh():
    print('\n3.7')
    MAC = '1111:2222:3333'
    out = MAC.split(':')
    print((bin(int(out[0])))[2:], (bin(int(out[1])))[2:], (bin(int(out[2])))[2:], sep=':')


def eight():  # без циклов тут кода много (хотя как и в прошлом нам известен размер ip
    print('\n3.8')
    IP = '192.168.3.1'
    a = IP.split('.')
    a = ['{:<10}'.format(i) for i in a]
    b = ['{:<010d}'.format(int(bin(int(i))[2:])) for i in a]
    print(' '.join(a))
    print(' '.join(b))


def nineth():
    print('\n3.9')
    num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
    word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
    a = num_list[::-1]
    b = word_list[::-1]
    print('10 in:', len(a) - a.index(10), ' ruby in:', len(b) - b.index('ruby'))
