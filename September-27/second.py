# check prime number using break statement 
n = int(input("Enter a number ")) # 15 
count = 0
for i in range(2,n): # 2 to 14 
    if n % i == 0:
        count = count+1
        break
if count == 0:
    print("{} is a prime number ".format(n))
else:
    print("{} is not a prime number ".format(n))
    
    