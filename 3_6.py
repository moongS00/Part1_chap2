'''
#1. pc에서 난수를 발생하면 사용자가 맞추는 게임을 만들어보자

pc가 난수(1~1000)를 발생하면 사용자가 숫자(정수)를 입력한다
사용자가 난수를 맞추면 게임이 종료딘다
만약 못맞추면 난수와 사용자 숫자의 크고 작음을 출력한 후 사용자에게 다시 기회를 준다
최종적으로 사용자가 시도한 횟수를 출력한다

import random
flag = True
ran_num = random.randint(1, 1000)
user = int(input('1에서 1000까지의 정수 입력: '))
n = 0

while flag:
    n += 1

    if user > ran_num :
        print('난수가 작다!')
        user = int(input('1에서 1000까지의 정수 입력: '))
    elif user < ran_num :
        print('난수가 크다!')
        user = int(input('1에서 1000까지의 정수 입력: '))
    elif user == ran_num :
        print('빙고!')
        flag = False

print('난수: {}, 시도 횟수: {}'.format(ran_num, n))

# 더 간단한 방법
while flag:
    n += 1
    user = int(input('1에서 1000까지의 정수 입력: '))

    if user == ran_num:
        print('빙고!')
        flag = False
    else:
        if user > ran_num:
            pass
        else:
            pass

'''

#2.실내온도를 입력하면 스카트에어컨 상태가 자동으로 설정되는 프로그램을 만들어보자
tem = int(input('실내온도 입력 : '))

if tem > 28:
    print('에어컨: 매우 강!!')
elif tem > 26:
    print('에어컨: 강!!')
elif tem > 24:
    print('에어컨: 중!!')
elif tem > 22:
    print('에어컨: 약!!')
elif tem > 18:
    print('에어컨: 매우 약!!')
else:
    print('에어컨: off!!')
