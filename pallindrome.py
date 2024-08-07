str = input("enter the word:")
n = len(str)
rev_str = ""
for i in range(n-1,-1,-1):
    rev_str = rev_str+str[i]
    print(rev_str)
if(rev_str==str):
    print("the word is a pallindrome")
else:
    print("the word is not a pallindrome")