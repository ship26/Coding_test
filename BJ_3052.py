
num_list =[]  #리스트 생성

for i in range(0,10):
    num_list.append((int(input())%42))  #10번반복, 42나머지 저장


set_list=set(num_list)  #고유값 set 생성

print(len(set_list)) #출력