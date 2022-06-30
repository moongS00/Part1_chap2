#윤년 계산기를 만들어보자
'''
윤년 조건
- 연도가 4로 나누너 떨어지고, 100으로 나누어 떨어지지 않으면 윤년이다
- 또는 연도가 400으로 나누어떨어지면 윤년이다
'''

'''
user_year = int(input('연도 입력: '))
result = ''

if user_year % 4 == 0 and user_year % 100 != 0 :
    result = '윤년!!'
elif user_year % 400 == 0:
    result = '윤년!!'
else:
    result = '평년'

print('{}년: {}'.format(user_year, result))
'''
result = ''
for i in range(2021,2045):
    if i % 4 == 0 and i % 100 != 0:
        result = '윤년!!'
    elif i % 400 == 0:
        result = '윤년!!'
    else:
        result = '평년'

    print('{}년: {}'.format(i, result))
