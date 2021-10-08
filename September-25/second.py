# input 2 * 2 matrix 
matrix = [] # [[12,15],[12,15]]
for x in range(2): # row
    rows = [] # [12,15]
    for y in range(2): # column 
        element = int(input("enter element [{}] [{}] ".format(x,y)))
        rows.append(element)
    matrix.append(rows)
print("*********-----Matrix-----***********")
for row in matrix:
    for element in row:
        print(element,end=" ")
    print()

