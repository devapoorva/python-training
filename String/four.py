# inbuilt function 
# len() - we can len() to find the number of characters present in the string 
# s = input("Enter a string ")
# print("length of the string is {}".format(len(s)))

# WAP to input a string and print their character using while loop
# forwad direction 
# Backward direction 

s = input("Enter a string ") # abcd -1 to -4
n = len(s)
i = 0
print("Forwad Direction ")
while i < n:
    print(s[i],end="  ")
    i+=1
print("\nBackward Direction ")
i = -1
while i >= -n:
    print(s[i],end="  ")
    i-=1
