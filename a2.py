num = int(input("Enter your number : "))
flag = True
for f in range(2 ,num):
    if(num % f ==0 ):
        flag = False
        break
if(flag==False):
    print(num, "is a compsite number")
else:
    print(num , "is a prime number")
