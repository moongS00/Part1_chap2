#1. 사용자가 입력한 데이터의 길이를 출력하는 프로그램 만들기 : len() 함수
msg = input('메시지 입력 : ')
print('메시지 문자열 길이 : {}'.format(len(msg)))


#2. 다음 문장에서 '객체지향'문자열을 찾아 보자. : find() 함수
article = '파이썬(영어: Python)은 1991년 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어로,플랫폼에 독립적이며 인터프리터식, 객체지향적, 동적 타이핑 대화형 언어이다.'

str_idx = article.find('객체지향')
print('객체지향 문자열 위치 : {}'.format(str_idx)) #위치는 0부터 시작

#3. 사용자가 입력한 데이터를 모두 실수로 변경한 후 사각형, 삼각형의 넓이를 출력해보자.
width = float(input('가로 길이 입력 : '))
height = float(input('세로 길이 입력 : '))

sq = width * height
tr = width * height / 2

print('-'*10, 'Result', '-'*10)
print('삼각형 넓이 : %f' %tr)
print('사각형 넓이 : %f' %sq)
print('삼각형 넓이 : %.2f' %tr)
print('사각형 넓이 : %.2f' %sq)
print('-'*30)