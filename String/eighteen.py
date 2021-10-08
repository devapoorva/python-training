# 1. reverse the string 
s = input("Enter string ")
# print(s[::-1])

# print(''.join(reversed(s)))

rev = ""
i = len(s) - 1 # 5
while i>=0: 
    last_char = s[i]
    i = i-1
    rev = rev+last_char
print(rev)

