
N= int(input())   #N개의 정수를 입력 받는다

int_array=list(map(int,input().split()))   #정수를 담을 리스트(배열) 생성

min_value = min(int_array)  #최대값 저장
max_value = max(int_array)  #최소값 저장

print(f"{min_value} {max_value}")  #최대 최소 출력




