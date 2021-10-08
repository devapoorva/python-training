# WAP to merge character of 2 strings into a single string by 
# taking character alternative 
s1 = input("Enter first string ") # Apoorv
s2 = input("Enter second string ") # Vardhman
s3 = ""
i,j = 0,0

while i<len(s1) or j<len(s2):
    if i < len(s1):
        s3 = s3+ s1[i]
        i+=1
    if j<len(s2):
        s3 = s3 + s2[j]
        j+=1
print(s3)



