N= int(input())  #입력값받음

ox_list=[]  #리스트
for i in range(0,N):  #for문을 돌면서 리스트안에 리스트를 넣음
    temp = list(input().split())
    ox_list.append(temp)



for j in range(0,len(ox_list)):  #이중 포문을 돌면서 요소가 O면 값을카운트 아니면 값을 초기화 해서 전체합을 더함
    total=0
    temp=0

    for k in range(0,len(ox_list[j][0])):
    
        value=ox_list[j][0][k]  #2차원 리스트의 1차원리스트의 k번째요소
        if value=='O':
            temp += 1
            total +=temp
        elif value=='X':
            temp=0

    print(total)

