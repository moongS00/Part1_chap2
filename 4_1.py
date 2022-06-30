# 1부터 100까지 정수 중 십의자리와 일의자리에 대해 각각 홀/짝수를 구분하는 프로그램을 만들어보자
odd = '홀수'
even = '짝수'

for i in range(1, 101):
    if i < 10:
        if i % 2 == 0 :
            print('[{}]: {}'.format(i, even))
        else:
            print('[{}]: {}'.format(i, odd))
    else:
        ten = i // 10
        one = i % 10
        if (ten % 2 == 0) and (one  == 0):
            print('[{}] 십의자리: {}, 일의자리: 0'.format(i, even ))
        elif (ten % 2 == 0) and (one % 2 != 0):
            print('[{}] 십의자리: {}, 일의자리: {}'.format(i, even, odd))
        elif (ten % 2 != 0) and (one % 2 != 0):
            print('[{}] 십의자리: {}, 일의자리: {}'.format(i, odd, odd))
        elif (ten % 2 != 0) and (one % 2 == 0):
            print('[{}] 십의자리: {}, 일의자리: {}'.format(i, odd, even))
        elif (ten % 2 == 0) and (one % 2 == 0):
            print('[{}] 십의자리: {}, 일의자리: {}'.format(i, even, even))

'''
#쉬운 방법
num10 = i // 10
num1 = i % 10

res10 = ''
if num10 % 2 == 0:
    res10 = '짝수'
else:
    res10 = '홀수'

res1 = ''
if num1 != 0:
    if num1 % 2 == 0:
        res1 = '짝수'
    else:
        res1 = '홀수'
else:
    res1 = '0'
    
print('[{}] 십의자리: {}, 일의자리: {}'.format(i, res10, res1))
'''