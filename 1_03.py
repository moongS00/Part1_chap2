#1. 원의 반지름을 입력하면 원의 넓이와 둘레 길이를 출력하되, 아래와 같은 형식으로 출력해보자,
# 정수 / 소수점 한자리 / 소수점 셋째자리
dim = int(input('반지름(cm) 입력 : '))

long = 2 * dim * 3.14
area = dim * dim * 3.14

print('원의 넓이\t\t:\t%dcm' %area)
print('원 둘레이길이\t:\t%dcm' %long)

print('원의 넓이\t\t:\t%.1fcm' %area)
print('원 둘레이길이\t:\t%.1fcm' %long)

print('원의 넓이\t\t:\t%.3fcm' %area)
print('원 둘레이길이\t:\t%.3fcm' %long)

#2. 사용자로부터 입력받은 개인정보를 포맷문자열을 이용해서 출력해보자
# (단, 비밀번호와 주민번호 뒷자리는 별표로 처리하자)
name = input('이름 입력: ')
mail = input('메일 입력: ')
user_id = input('아이디 입력: ')
pw = input('비밀번호 입력: ')
user_num_head = input('주민번호 앞자리 입력: ')
user_num_tail = input('주민번호 뒷자리 입력: ')
add = input('주소 입력: ')

print('-'*30)
print('이름 : {}'.format(name)) #print(f'이름 : {name}')
print('메일 : {}'.format(mail))
print('아이디 : {}'.format(user_id))
print('비밀번호 : {}'.format('*'*len(pw)))
print('주민번호 : {} - {}{}'.format(user_num_head, user_num_tail[0], '*'*(len(user_num_tail)-1)))
print('주소 : {}'.format(add))
print('-'*30)

