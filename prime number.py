i=2
j=0
flag=0
N=30
count=0


for i in range(2,10000000000,1):
        flag=1
        for j in range(2,(i//2)+1,1):
            if (i%j==0):
                flag=0
                break
        if (flag==1):
            print(i,end=" ")
            count += 1
        if count==N:
            break

