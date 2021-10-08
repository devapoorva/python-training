# spliting of strings
# We can split the string a/c to specified separator by using split() method
# The default separator is space. retrun type - list

# input a sentence and print their words without using split()

# s = "Sadaf is a good girl"
# words = s.split()

# for word in words:
#     print(word)

# input a date print day month and year 
date = input("Enter date (dd-mm-yyyy) ")
l = date.split("-") # ['20','6','2021']
day = l[0]
month = l[1]
year = l[2]
print("Day in {} is {} ".format(date,day))
print("Month in {} is {} ".format(date,month))
print("Year in {} is {} ".format(date,year))

