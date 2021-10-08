# finding substring 
# we can use 4 methods for find substring

# Forwad direction
# 1. find()
# 2. index()

# Backward Direction 
# 1. rfind()
# 2. rindex()

#1. find() syntax: s.find(substring) return index
# Return index of first occurrence of the given string. If it is not 
# available the we will get -1

# s = "Vartika Sadaf"
# findString = "Sadaf"
# print(s.find("Sadaf"))

# find() can search total string. We can specify the bounding to search 
# s.find(subString,start,end) It will always search from start and end-1 index
# print(s.find("Sadaf",5,10)) # 

# index()
# index() is same as find() except if substring is not available then we will get 
# value error 

s = "I am a boy"
try:
    print(s.index("boy"))
except ValueError:
    print("Substring not found")
else:
    print("Substring found")


