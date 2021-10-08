# formatting the strings
# format string into meaningful output

# case 1: 
# basic formatting for default,positional and keyword argument 

name = "Sadaf"
salary = 50000
age = 22
print("{}'s salary is {} and her age is {} ".format(name,salary,age))

print("{1}'s salary is {0} and her age is {2} ".format(salary,name,age))

print("{x}'s salary is {y} and her age is {z}".format(z=age,y=salary,x=name))

