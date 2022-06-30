#1. 체중(g0과 신장(cm)을 입력하면 BMI지수가 출력되는 프로그램을 만들어보자 : isdigit() 함수
weight  = input('체중 입력(g) : ') 
height  = input('신장 입력(cm) : ')

if weight.isdigit():
    weight = int(weight) / 10

if height.isdigit():
    height = int(height) / 100

bmi = weight / (height * height)

print(f'체중 : {weight}kg')
print(f'신장 : {height}m')
print(f'BMI : {bmi}')

#2. num1 과 num2의 값을 서로 바꾸고 각각 출력해보자
num1 = 10
num2 = 20
print('num1: {}, num2: {}'.format(num1, num2))
print('num1: {}, num2: {}'.format(num2, num1))


#3. 중간, 기말고사 점수를 입력하면 총점과 평균이 출력되는 프로그램을 만들어보자
mid = input('중간 고사 점수: ')
final = input('기말 고사 점수: ')

if mid.isdigit() and final.isdigit():
    mid = int(mid)
    final = int(final)
    total = mid + final
    avg = total / 2
    print('총점 : {}, 평균 : {}'.format(total, avg))
else:
    print('잘 못 입력했습니다.')