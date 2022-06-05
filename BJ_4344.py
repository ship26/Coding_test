C = int(input())

answer_list=[]

for i in range(0,C):
    num_list= list(map(int,input().split()))
    sum=0
    mean=0
    alpha=0
    for j in range(1,num_list[0]+1):
        sum +=num_list[j]

    mean= sum/num_list[0]

    for k in range(1,num_list[0]+1):
        if num_list[k] > mean:
            alpha +=1

    percent= (alpha/num_list[0])*100

    answer_list.append(percent)


for c in range(0,len(answer_list)):
    pop=answer_list[c]
    print(f"{pop:.3f}%")
