n = int(input("enter the no."))
n1 = 0
n2 = 1
if(n<=0):
    print(n1)
else:
    print(n1,n2,end=" ")
    for i in range(2,n):
        result = n1 + n2
        print(result,end=" ")
        n1=n2
        n2=result