# 상품 가격과 지불 금액을 입력하면 거스름돈을 계산하는 프로그램을 만들어보자
#단, 거스름돈은 지폐와 동전의 개수를 최소로 하고, 1원단위를 절사한다.
m_50000 = 50000 ; m_10000 = 10000 ; m_5000 = 5000 ; m_1000 = 1000  #돈
m_500 = 500; m_100 = 100; m_50 = 50; m_10 = 10

m_50000_cnt = 0 ; m_10000_cnt = 0 ; m_5000_cnt = 0 ; m_1000_cnt = 0  #돈 개수
m_500_cnt = 0; m_100_cnt = 0; m_50_cnt = 0; m_10_cnt = 0

cost = int(input('상품 가격 입력: '))
pay = int(input('지불 금액: '))

if pay > cost:
    dif = pay - cost
    dif = (dif // 10) * 10  #1원단위 절사
    print('거스름돈 : {}(원단위절사)'.format(dif))

if dif > m_50000:
    m_50000_cnt = dif // m_50000
    dif %= m_50000

if dif > m_10000:
    m_10000_cnt = dif // m_10000
    dif %= m_10000

if dif > m_5000:
    m_5000_cnt = dif // m_5000
    dif %= m_5000

if dif > m_1000:
    m_1000_cnt = dif // m_1000
    dif %= m_1000

if dif > m_500:
    m_500_cnt = dif // m_500
    dif %= m_500

if dif > m_100:
    m_100_cnt = dif // m_100
    dif %= m_100

if dif > m_50:
    m_50_cnt = dif // m_50
    dif %= m_50

if dif > m_10:
    m_10_cnt = dif // m_10
    dif %= m_10

print('*'*30)
print('50,000 {}장'.format(m_50000_cnt))
print('10,000 {}장'.format(m_10000_cnt))
print('5,000 {}장'.format(m_5000_cnt))
print('1,000 {}장'.format(m_1000_cnt))
print('500 {}개'.format(m_500_cnt))
print('100 {}개'.format(m_100_cnt))
print('50 {}개'.format(m_50_cnt))
print('10 {}개'.format(m_10_cnt))
print('*'*30)
