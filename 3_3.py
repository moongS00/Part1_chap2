import random
'''
#1. 난수를 이용해 홀/짝 게임을 만들어보자


com_num = random.randint(1,2)
user = int(input('홀/짝 선택: 1.홀\t2.짝'))

if com_num == 1 and user == 1:
    print('빙고!! 홀수!!')
elif com_num == 1 and   user == 2:
    print('실패!! 홀수!!')
elif com_num == 2 and   user == 2:
    print('빙고!! 짝수!!')
elif com_num == 2 and   user == 1:
    print('실패!! 짝수!!')
'''

#2. 난수를 이용해 가위바이보 게임을 만들어보자
com_number = random.randint(1,3)
user_number = int(input('가위, 바위, 보 선택: 1.가위\t2.바위\t3.보'))

if (com_number == 1 and user_number == 2) or \
        (com_number == 2 and user_number == 3) or \
        (com_number == 3 and user_number == 1):
    print('컴퓨터: 패, 유저: 승')
elif com_number == user_number:
    print('무승부')
else:
    print('컴퓨터: 승, 유저: 패')

print('컴퓨터: {}, 유저: {}'.format(com_number, user_number))