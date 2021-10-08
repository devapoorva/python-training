# WAP to display all position of substring in a given string 
# this is a dog. the dog is a pet animal. dog has four legs.

s = input("Enter string ")
sub = input("Enter substring ")
pos = -1
count = 0
while True:
    pos = s.find(sub,pos+1,len(s)) # 0 to 49 #10 11 to 49 #20 21 to 49 
    if pos==-1:
        break
    print("Found at position ",pos)
    count+=1
if count == 0:
    print("Not Found")

