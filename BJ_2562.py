
int_array=[]  #정수 배열 선언
for i in range(0,9):  #9개의 수까지 입력을 받고
    int_array.append(int(input()))

max_value= max(int_array)   #최대값 선택
index= int_array.index(max_value)  #최대값의 인덱스 저장

print(max_value)   #출력  단 몇 번째 수인지므로 인덱스 +1
print(index+1)