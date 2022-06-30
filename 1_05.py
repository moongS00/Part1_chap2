#1.키오스크에서 사용하는 언어 선택 프로그램을 만들어보자
import datetime

lan = int(input('언어 선택(Choose your language): 1.한국어\t\t2.English'))
if lan == 1:
    print('1.샌드위치\t\t2.햄버거\t\t3.쥬스\t\t4.커피\t\t5.아이스크림')
elif lan == 2 :
    print('1.Sandwich\t\t2.Hamburger\t\t3.Juice\t\t4.Coffee\t\t5.Ice cream')

'''
if lan == 1:
    menu = '1.샌드위치\t\t2.햄버거\t\t3.쥬스\t\t4.커피\t\t5.아이스크림'
elif lan == 2 :
    menu = '1.Sandwich\t\t2.Hamburger\t\t3.Juice\t\t4.Coffee\t\t5.Ice cream'

print(menu)
'''

#2. 나의 나이가 100살 되는 해의 연도를 구하는 프로그램을 만들어보자
'''
age = input('나이 입력 : ')
n = 0
h = 0
flag = True

if age.isdigit():
    age= int(age)
    while flag:
        age += 1
        n += 1

        if age == 100:
            h = n
            flag = False
    h_year = 2022 + h
    print('{}년({}년후)에 100살!!'.format(h_year, n))
else:
    print('잘 못 입력했습니다.')
'''

today = datetime.datetime.today()

my_age = input('나이 입력 : ')
if my_age.isdigit():
    after_age = 100 - int(my_age)
    my_hun = today.year + after_age

    print('{}년({}년후)에 100살!!'.format(my_hun, after_age))

else:
    print('잘 못 입력했습니다.')