A=int(input())   #A,B,C 입력
B=int(input())
C=int(input())

num_list = [0,0,0,0,0,0,0,0,0,0]   #배열을 이용해서 0~9까지 카운팅
result = str(A*B*C)   #ABC 곱함

for i in range(len(result)):  #조건문을 이용해서 배열의 인덱스를 숫자 카운팅으로 사용
    num=int(result[i])
    if num==0:
        num_list[0]+=1
    elif num==1:
        num_list[1]+=1
    elif num==2:
        num_list[2]+=1
    elif num==3:
        num_list[3]+=1
    elif num==4:
        num_list[4]+=1
    elif num==5:
        num_list[5]+=1
    elif num==6:
        num_list[6]+=1
    elif num==7:
        num_list[7]+=1
    elif num==8:
        num_list[8]+=1
    elif num==9:
        num_list[9]+=1

for i in range(0,10):  #출력
    print(num_list[i])
