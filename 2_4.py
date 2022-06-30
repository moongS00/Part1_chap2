#1. 고도가 60m 올라갈 때마다 기온이 0.8도 내려간다고 할 때, 고도를 입력하면 기온이 출력되는 프로그램을 만들어보자
# 지면온도 : 29도
base_temp = 29
step = 60
s_temp = 0.8

height = int(input('고도 입력: '))

c_temp = base_temp - s_temp * (height // step)

if height % step != 0:
    c_temp -= s_temp

print('지면 온도: {}'.format(base_temp))
print('고도 {}m의 기온: {}'.format(height, c_temp))

#2. 197개의 빵과 152개의 우유를 17명의 학생한테 동이랗게 나눠준다고 할 때,
#한명의 학생이 간게 되는 빵과 우유의 개수를 구하고 남는 빵과 우유의 개수를 출력해라

bread = 197
milk = 152
std = 17

print('한생 한명이 갖게되는 빵 개수 : {}'.format(bread // std))
print('한생 한명이 갖게되는 우유 개수 : {}'.format(milk // std))

print('남는 빵 개수: {}'.format(bread % std))
print('남는 우유 개수: {}'.format(milk % std))