# 국어, 영어, 수학 점수 입력 후 총점, 평균, 최고점수과목, 최저점수 과목
# 그리고 최고 점수와 처저 점수의 차이를 각각 출력해보자

kor_score = int(input('국어 점수 입력 : '))
eng_score = int(input('영어 점수 입력 : '))
mat_score = int(input('수학 점수 입력 : '))

total = kor_score + eng_score + mat_score
avg = total / 3

max_score = kor_score
max_sub = '국어'

if eng_score > max_score:
    max_score = eng_score
    max_sub = '영어'

if mat_score > max_score:
    max_score = mat_score
    max_sub = '수학'

min_score = kor_score
min_sub = '국어'

if eng_score < min_score:
    min_score = eng_score
    min_sub = '영어'

if mat_score < min_score:
    min_score = mat_score
    min_sub = '수학'

dif_score = max_score - min_score

print('총점: {}'.format(total))
print('평균: %.2f' %avg)
print('*'*30)

print('최고 점수 과목(점수): {}({})'.format(max_sub, max_score))
print('최저 점수 과목(점수): {}({})'.format(min_sub, min_score))
print('최고, 최저 점수 차이: {}'.format(dif_score))
print('*'*30)