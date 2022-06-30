#1.
for i in range(1,6):
    print('*'*i)

#2.
for i in range(1,6):
    for j in range(6 - i - 1):
        print(' ', end='')
    for k in range(i):
        print('*', end='')
    print()

#3.
for i in range(5, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

#4.
for i in range(5, 0, -1):
    for j in range(5 - i):
        print(' ', end='')
    for k in range(i):
        print('*', end='')
    print()

#5.
for i in range(1, 10):
    if i < 5 :
        for j in range(i):
            print('*', end='')
    else:
        for j in range(10 -i):
            print('*', end='')
    print()

#6.
for i in range(1,6):
    for j in range(1,6):
        if i == j:
            print('*', end='')
        else:
            print(' ', end='')
    print()