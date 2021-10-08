# print() without argument
# print() with argument 
print("hello"+"World")
# if both are string then it will concatenate 
# if one argument is string and another one is other data type then get error
# if both arguments are number then print sum
print("hello","world")

# print() with variable numbers of argument
a,b,c = 10,20,30 
print("hello","world",a,b,c)

#print() with end attribute default value is \n - new line
print("hello ")
print("Warivo",end=" ")
print("infotech")

# print(string, variable list )
a,b,c = 10,20,30 
print("hello","world",a,b,c)

# print(formated string )
# formatted string
# %i - int 
# %d - int 
# %f - float 
# %s - string 

a = 10
b = 20
c = a + b
print("sum is %i " %c)

#print() with replacement operator {} 
print("Sum of {} and {} is {}".format(b,a,c))
print("Sum of {1} and {0} is {2}".format(b,a,c))

print("Sum of {a} and {b} is {sum}".format(a=a,b = b, sum= c))

