#'주문확인서'템플릿을 만들고, 변경되는 정보만 입력하면 '주문확인서'가 완성될 수 있도록 프로그램을 만들어 보자
import datetime

name = '홍길동'
item = '야구글러브'
code = 2568956
how = '신용카드'
cost = 110000
pay = 100000
point = 10000
today = datetime.datetime.today()
month = 6
pay_type = '무'

print('{} 고객님 안녕하세요.'.format(name))
print('{} 고객님 의 주문이 완료되었습니다..'.format(name))
print('다음은 주문건에 대한 상세 내역입니다.')
print('-'*25)
print('상품명 : {}'.format(item))
print('주문번호 : {}'.format(code))
print('결재방법 : {}'.format(how))
print('상품금액 : {} 원'.format(cost))
print('결재금액 : {} 원'.format(pay))
print('포인트 : {} P'.format(point))
print('결제일시 : {} '.format(today))
print('할부 : {} 개월'.format(month))
print('할부유형 : {}'.format(pay_type))
print('문의 : 02-1234-5678')
print('-'*25)
print('저희 사이트를 이용해 주셔서 감사합니다.')

