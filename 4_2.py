#1부터 사용자가 입력한 정수까지의 합, 홀수의 합, 짝수의 합 그리고 팩토리얼을 출력하는 프로그램을 만들어보자
user_int = int(input('정수 입력 : '))
sum = 0
odd_sum = 0
even_sum = 0
fac = 1

for i in range(1, user_int+1):
    sum += i
    fac *= i
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print('합 결과: {}'.format(sum))
print('홀수 합 결과: {}'.format(odd_sum))
print('짝수 합 결과: {}'.format(even_sum))
print('팩토리얼 결과: {}'.format(format(fac, ',')))