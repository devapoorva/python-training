# spaces 
k = 3
# number of rows
for i in range(1,5): # 1 to 4
    # inner loop to handle spaces
    for j in range(k):
        print(end=" ")
    k = k-1

    for l in range(1,i+1): # i =1 l = 1 
        print("*",end=" ")
    print()

