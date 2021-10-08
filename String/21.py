# print character at odd position and even position 
s = input("enter string ")
# print("Character at even position ",s[0::2])
# print("Character at odd position ",s[1::2])

i = 0 
print("characters at even position ")
while i < len(s):
    print(s[i],end=" ")
    i = i+2
print("\ncharacters at odd position ")
i = 1 
while i <len(s):
    print(s[i],end=" ")
    i = i+2