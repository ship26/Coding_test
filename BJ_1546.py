

N = int(input()) #과목의 개수

total=0 #변수 생성
score_list=list(map(int,input().split()))#  리스트 생성 , 리스트 추가

M= max(score_list) #최대값

for i in range(0,N):
    score_list[i] = (score_list[i]/M)*100  #리시트별 공식 적용


for i in range(0,N):
    total += score_list[i]


new_mean= total / N  #평균값구하기, 출력
print(new_mean)
