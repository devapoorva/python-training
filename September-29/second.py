s = input("Enter string ") #Nidhi
count =0
for i in s:
    print("Character is {} at positive index is {} and 
    negative index is {}".format(s[count],count,count-len(s)))
    count+=1
