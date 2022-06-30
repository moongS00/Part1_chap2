#1. 시, 분, 초를 입력하면 초로 환산하는 프로그램을 만들어보자

hou = int(input('시간 입력:'))
min = int(input('분 입력:'))
sec = int(input('초 입력:'))

print('{}초'.format(format(hou * 60 * 60 + min * 60 + sec, ',')))


#2. 금액, 이율, 거치기간을 입력하면 복리계산하는 복리계산기 프로그램을 만들어보자
mon = int(input('금액 입력: '))
rate = float(input('이율 입력: '))
term = int(input('기간 입력: '))
final_mon = mon

for i in range(term):
    final_mon = final_mon + (final_mon * rate / 100)

final_mon_fomat = format(int(final_mon), ',')

print('*'*30)
print('이율: {}%'.format(rate))
print('원금: {}원'.format(format(mon,',')))
print('{}년 후 금액: {}원'.format(term, final_mon_fomat))
print('*'*30)