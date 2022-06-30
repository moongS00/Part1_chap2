#1. 톱니가 각각 n1개와 n2개의 톱니바퀴가 서로 맞물려 회전할 때,
# 회전을 시작한 후 처음 맞물린 톱니가 최초로 다시 만나게 될 때 까지의 톱니의 수와 각각의 바퀴 회전수를 출력해보자
# 단 n2는 n1보다 크다
'''
내 풀이

a = int(input('GearA 톱니수 입력: '))
b = int(input('GearB 톱니수 입력: '))
max = a*b

for i in range(1, max+1):
    print('gearA: {}, gearB: {}'.format(a * i, b * i))
    if i % a == 0 and i % b == 0:
        break

max = i

print('최초 만나는 톱니수(최소공배수): {}톱니'.format(max))
print('gearA 회전수: %d회전' %(max/a))
print('gearB 회전수: %d회전' %(max/b))
'''

a = int(input('GearA 톱니수 입력: '))
b = int(input('GearB 톱니수 입력: '))

gearA = 0
gearB = 0

least_num = 0
flag = True

while flag:
    if gearA != 0 :
        if gearA != least_num:  # 공배수에 도달하지 못함 -> 계속 회전해
            gearA += a
        else:
            flag = False    # 공배수에 도달함 -> 반복문 중지

    else:
        gearA += a   # 회전수가 0 -> 일단 돌아

    if gearB != 0 and gearB % a == 0: #더 큰 수로 공배수를 공배수 구함
        least_num = gearB
    else:
        gearB += b  #공배수 못구함 -> 계속 회전해

print('최초 만나는 톱니수(최소공배수): {}톱니'.format(least_num))
print('gearA 회전수: %d회전' %(least_num/a))
print('gearB 회전수: %d회전' %(least_num/b))