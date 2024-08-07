n = 4
for i in range(n):
    for j in range(i + 1):
        print("*",end=" ")
    print()
print("---------------")
for i in range(n,0,-1):
        print("  " * (n-i)+"* "*i)
print("---------------")
for i in range(1,n+1):
    for j in range(1,i):
        print(" ", end=" ")
    for k in range(1,n-i,1):
            print("* ",end=" ")
    print()






