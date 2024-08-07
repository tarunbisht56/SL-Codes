n = int(input("enter the no."))
sum = 0
while(n>0):
    unit_digit = n%10
    sum = sum + unit_digit
    n = n//10
print(sum)