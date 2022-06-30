'''
#1. 다음 내용을 참고해서 백신접종 프로그램을 만들어보자
'''
#9세 이하 또는 65세 이상이면 출생연도 끝자리에 따른 접종
#그렇지않으면 하반기 일정 확인
'''

my_age = int(input('나의 입력: '))

if 19 < my_age < 65:
    print('하반기 일정 확인하세요')
else:
    y_end = int(input('출생 연도 끝자리 입력: '))
    
    if y_end == 0 or y_end == 5:
        print('금요일 접종 가능!!')
    elif y_end == 1 or y_end == 6:
        print('월요일 접종 가능!!')
    elif y_end == 2 or y_end == 7:
        print('화요일 접종 가능!!')
    elif y_end == 3 or y_end == 8:
        print('수요일 접종 가능!!')
    elif y_end == 4 or y_end == 9:
        print('목요일 접종 가능!!')
'''

#2. 길이(mm)를 입력하면 inch로 환산하는 프로그램을 만들어보자(1mm = 0.039inch)
by_inch = 0.039
lenth = int(input('길이(mm) 입력: '))

le_to_in = lenth * by_inch

print('{}mm -> {}inch'.format(lenth,le_to_in))