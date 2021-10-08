# Argument is list available in sys module
# the argument which are passing at the time of execution is called command line 
# arguments

# import sys - import complete module 
from sys import argv

# print(sys.argv)

print(argv[0])

a,b = argv[1],argv[2]
print(a+b)


