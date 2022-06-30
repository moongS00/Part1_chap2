#1. 버스 A, B, C의 운행정보가 다음과 같을 때, 2대 이상의 버스가 정차하는 시간대를 출력해보자
'''
버스 A, B 운행정보
-오전 6시 첫차: 오후 23시 운행 종류
-버스A: 15분 간격 운행
-버스B: 13분 간격 운행

버스C 운행 정보
-6시 20분 첫차: 오후 22시 운행 종류
-8분 간격 운행

(최소공배수의 개념 사용)
'''

bus_A = 15
bus_B = 13
bus_C = 8

total_min = 60 * 17 #총 운행시간(6시~23시)(17시간을 분으로 환산)
for i in range(total_min+1):
    if i < 20 or i > (total_min - 60):  #버스C가 운행하지 않는 6시~6시20분 & 22시~23시
        if i % bus_A == 0 and i % bus_B == 0:
            print('busA와 busB 동시 정차!!', end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t{} : {}'.format(hour, min))

    else:
        if i % bus_A == 0 and i % bus_B == 0:
            print('busA와 busB 동시 정차!!', end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t{} : {}'.format(hour, min))
        elif i % bus_A == 0 and i % bus_C == 0:
            print('busA와 busC 동시 정차!!', end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t{} : {}'.format(hour, min))

        elif i % bus_B == 0 and i % bus_C == 0:
            print('busB와 busC 동시 정차!!', end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t{} : {}'.format(hour, min))
