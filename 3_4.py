#1. 상수도 요금 계산기를 만들어보자
kind = int(input('업종 선택 : 1.가정용\t2.대중탕용\t3.공업용\t'))

if kind == 1:
    used = int(input('사용량 입력 : '))
    charge = 540 * used
elif kind == 2:
    used = int(input('사용량 입력 : '))
    if used > 300:
        charge = 2400 * used
    elif used > 50 :
        charge = 1920 * used
    else:
        charge = 820 * used
elif kind == 3:
    used = int(input('사용량 입력 : '))
    if used > 500 :
        charge = 470 * used
    else:
        charge = 240 * used


print('='*30)
print('상수도 요금표')
print('-'*30)
print('사용량\t\t:\t\t요금')
print('{}\t\t\t:\t\t{}원'.format(used, format(charge, ',')))
print('='*30)