# accessing character by using slice operator 
# syntax : s[startIndex:endIndex:step]
# startIndex : where we have to consider slice (SubString)
# EndIndex : Where we have to terminate the slice at endIndex-1
# step : Increment value

s = input("enter string ") # My Name is Apoorv
#print(s[1:5:1]) # y Na
#print(s[1:5]) # y Na default step - 1
# print(s[1:len(s)]) # 
#print(s[::]) # startIndex -0 , end= len , step -1

# print(s[::-1])

# in backward direction end value is -1 then result is empty
# print(s[:-1:-1]) # 
# in forward direction end value is 0 then result is empty 

# In forward direction : 
# default value of start = 0
# default value of end = length of string 
# default value of step = 1

# In backward direction 
# default value of start = -1 
# default value of end = -(length of string +1)

print(s[-1:-6:-2]) # 



