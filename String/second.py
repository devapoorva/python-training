s = "abcdefghijklmnopqrstuvwxyz"
a= s[1:6:2] # bdf
# print(a)
s[::1] # endIndex = len(s)
s[::-1] # endIndex = -(len(s)+1)
s[3:5:-1] # ""
s[5:2:-1] # 5 to 3
b = s[2:50:1] # 2 to 49
#s[9:0:0] # Value Error: slice step cannot be zero
b= s[0:-5:-2]  # ""
s[10:-1:-1] # ""
b = s[50:2:-1] # 50 to 3
print(b)

