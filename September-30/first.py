s = input("enter string ") # Apoorv -6
revString = ""
for x in range(-1,0-len(s)-1,-1): # -1 to -6 
    character = s[x]
    revString = revString + character
if s==revString:
    print("Palindrome ")
else:
    print("Not palindrome ")

