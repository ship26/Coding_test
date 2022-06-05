N= int(input())

S=0
A= list(map(int,input().split()))
B= list(map(int,input().split()))

sorted_B = B.copy()
sorted_B.sort()

sorted_A = A.copy()
sorted_A.sort(reverse=True)

for i in range(N):
    S +=sorted_A[i]*sorted_B[i]

print(S)


