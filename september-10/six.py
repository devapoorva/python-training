#Take input of age of 3 people by user and determine oldest and
#  youngest among them.

age1,age2,age3 = [int(x) for x in input("Enter three age ").split()]

if age1>age2 and age1>age3:
    print("Oldset age is ",age1)
    if age2 < age3:
        print("Youngest age is ",age2)
    else:
        print("Youngest age is ",age3)
elif age2>age3 and age2>age1:
    print("Oldest age is ",age2)
    if age1 < age3:
        print("Youngest age is ",age1)
    else:
        print("Youngest age is ",age3)
else:
    print("Oldest age is ",age3)
    if age1 <age2:
        print("Youngest age is ",age1)
    else:
        print("youngest age is ",age2)

