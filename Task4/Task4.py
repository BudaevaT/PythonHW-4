import random


def write_file(st):
    with open('result.txt', 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0,101)


def create_mn(k):
    my_list = [rnd() for i in range(k+1)]
    return my_list
    

def create_str(sp):
    my_list= sp[::-1]
    wr = ''
    if len(my_list) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(my_list)):
            if i != len(my_list) - 1 and my_list[i] != 0 and i != len(my_list) - 2:
                wr += f'{my_list[i]}x^{len(my_list)-i-1}'
                if my_list[i+1] != 0:
                    wr += ' + '
            elif i == len(my_list) - 2 and my_list[i] != 0:
                wr += f'{my_list[i]}x'
                if my_list[i+1] != 0:
                    wr += ' + '
            elif i == len(my_list) - 1 and my_list[i] != 0:
                wr += f'{my_list[i]} = 0'
            elif i == len(my_list) - 1 and my_list[i] == 0:
                wr += ' = 0'
    return wr

k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))