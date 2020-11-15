import random

def Random(x):

    list = []
    for i in range(0, 6):
        val=random.randint(1, 20)
        if val % 2 == 0:
            print(f'liczba {val} jest podzielna przez 2')
        list.append(val)
    return list
list= Random(20)
print(list)


