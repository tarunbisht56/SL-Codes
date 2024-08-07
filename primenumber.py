n = int(input("enter the no."))
flag = True
for i in range(2,n):
    if (n%i == 0):
        flag = False
        break

if(flag):
    print("Its a prime no.")
else:
    print("its not a prime no.")







