#1. 미세먼지 비상저감조치로 차량 운행제한 프로그램 만들기
'''
미세먼지 측정 수치가 150 이하 : 차량 5부제 실시
미세먼지 측정 수치가 150 초과 : 차량 2부제 실시
차량 2부제여도 영업용 차량은 5부제 실시
미세먼지 수치, 차량 종류, 차량 번호를 입력하면 운행 가능 여부 출력
'''
import datetime

today = datetime.datetime.today()
day = today.day
limit_dust = 150
dust = int(input('미세먼지 수치 입력: '))
my_car = int(input('차량 종류 선택: 1.승용차\t\t2.영업용차\t\t'))
car_num = int(input('차량 번호 입력: '))

print('*'*30)
print(today)
print('*'*30)

if dust > limit_dust and my_car == 1:
    if (day % 2) == (car_num % 2):
        print('차량 2부제 적용')
        print('차량 2부제로 금일 운행제한 대상 차량입니다.')
    else:
        print('금일 운행 가능합니다.')

if dust > limit_dust and my_car == 2:
    if (day % 5) == (car_num % 5):
        print('차량 5부제 적용')
        print('차량 5부제로 금일 운행제한 대상 차량입니다.')
    else:
        print('금일 운행 가능합니다.')

if dust <= limit_dust:
    if (day % 5) == (car_num % 5):
        print('차량 5부제 적용')
        print('차량 5부제로 금일 운행제한 대상 차량입니다.')
    else:
        print('금일 운행 가능합니다.')

print('*'*30)