import random

name_1 = 'John'
name_2 = 'Jack'  # computer
a = 0
b = 0
print('How many pencils would you like to use:')


class ZeroPencil(Exception):
    pass


class ToManyPencil(Exception):
    pass


class ComeOnGuy(Exception):
    pass


def is_pencil_zero(count_pencil):
    a = 0
    try:
        if count_pencil == 0:
            raise ZeroPencil
        elif count_pencil < 0:
            raise ValueError
    except ZeroPencil:
        print('The number of pencils should be positive')
    else:
        a = 1
    return a


def pencil_on_the_table(count_pencil):
    c = 0
    while c == 0:
        try:
            num = int(input())
            if num > 3 or num <= 0:
                raise ToManyPencil
            elif num > count_pencil:
                raise ComeOnGuy
        except ToManyPencil:
            print("Possible values: '1', '2' or '3'")
        except ComeOnGuy:
            print('Too many pencils were taken')
        except ValueError:
            print("Possible values: '1', '2' or '3'")
        else:
            c = 1
    return num


while a == 0:
    cnt_p = input()
    try:
        cnt_p = int(cnt_p)
        a = is_pencil_zero(cnt_p)
    except ValueError:
        print('The number of pencils should be numeric')

print(f'Who will be the first ({name_1}, {name_2}):')


def whose_move(names_of_person):
    b = 0
    if names_of_person != name_1 and names_of_person != name_2:  # John and Jack
        print(f'Choose between {name_1} and {name_2}')
    elif names_of_person == name_1:  # John
        b = 2
    elif names_of_person == name_2:  # Jack = computer
        b = 3
    return b


while b == 0:
    name = input()
    b = whose_move(name)
c = 0
while cnt_p > 0:
    print('|' * cnt_p)
    if b % 2 == 0:  # John
        print(f"{name_1}'s turn:")
        num = pencil_on_the_table(cnt_p)
        cnt_p -= num
        b += 1
    elif b % 2 == 1:  # Jack
        print(f"{name_2}'s turn:")
        if cnt_p % 4 == 0:
            num = 3
            print(num)
        elif cnt_p % 4 == 3:
            num = 2
            print(num)
        elif cnt_p % 4 == 2:
            num = 1
            print(num)
        elif cnt_p == 2:  # da
            num = 1
            print(num)
        elif cnt_p == 1:  # da
            num = 1
            print(num)
        else:
            num = random.randint(1, 3)
            print(num)
        cnt_p -= num
        b += 1
    elif cnt_p == 0:
        break

if b % 2 == 0:
    print(name_1, 'won!')
elif b % 2 == 1:
    print(name_2, 'won!')

