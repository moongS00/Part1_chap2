#1. 성적을 입력하면 총점을 비롯한 각종 데이터가 출력되는 프로그램을 만들어보자
'''
과목별 점수를 입력하면 총점, 평균, 편차를 출력한다
평쥼은 다음과 같다
국어:85, 영어:82, 수학:89, 과학:75, 국사:94

각종 편차 데이터는 막대그래프로 시각화한다
'''
kor_score = int(input('국어 점수: ')); eng_score = int(input('영어 점수: '))
mat_score = int(input('수학 점수: ')); sci_score = int(input('과학 점수: '))
his_score = int(input('국사 점수: '))
total_score = kor_score + eng_score + mat_score + sci_score + his_score
avg_score = int(total_score / 5)

kor_avg = 85; eng_avg = 82; mat_avg = 89; sci_avg = 75; his_avg = 94
total_avg = kor_avg + eng_avg + mat_avg + sci_avg + his_avg
avg_avg = int(total_avg / 5)

kor_dif = kor_score - kor_avg
eng_dif = eng_score - eng_avg
mat_dif = mat_score - mat_avg
sci_dif = sci_score - sci_avg
his_dif = his_score - his_avg
total_dif = total_score - total_avg
avg_dif = avg_score - avg_avg

print('-'*70)
print('총점: {}({}), 평균: {}({})'.format(total_score,total_dif,avg_score,avg_dif))
print('국어: {}({}), 영어: {}({}), 수학: {}({}), 과학: {}({}), 역사: {}({})'.format(
    kor_score, kor_dif, eng_score,eng_dif,mat_score,mat_dif,sci_score,sci_dif,his_score,his_dif))
print('-'*70)

str = '+' if kor_dif > 0 else '-'
print('국어 편차: {}({})'.format(str*abs(kor_dif), kor_dif))

str = '+' if eng_dif > 0 else '-'
print('영어 편차: {}({})'.format(str*abs(eng_dif), eng_dif))

str = '+' if mat_dif > 0 else '-'
print('수학 편차: {}({})'.format(str*abs(mat_dif), mat_dif))

str = '+' if sci_dif > 0 else '-'
print('과학 편차: {}({})'.format(str*abs(sci_dif), sci_dif))

str = '+' if his_dif > 0 else '-'
print('역사 편차: {}({})'.format(str*abs(his_dif), his_dif))