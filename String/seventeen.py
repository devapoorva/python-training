# case 2: formatting numbers 
# d -> decimal integer
# f -> floating numbers default precision is 6
# b -> binary format
# o -> octal format
# x -> Hexa decimal format (lower case)
# X -> Hexa decimal format (Upper case)

# a = 1234
# print("integer number is {} ".format(a))
# print("integer number is {:d} ".format(a))
# print("integer number is {:9d} ".format(a))
# print("integer number is {:09d} ".format(a)) 

# a = 123.45
# print("float number is {} ".format(a))
# print("float number is {:f} ".format(a))
# print("float number is {:9.3f} ".format(a)) #total position = 8 total precision 3
# print("float number is {:09.3f} ".format(a))
# print("float number is {:09.4f} ".format(a))
# a = 1234567890.1234
# print("float number is {:09.6f} ".format(a)) 

# Total position should be minimum 9
# after decimal point exactly x digit(xf) are allowed. if it is less then 0s
# will be placed in the last position 

# if total number is < 9 positions then 0 will be placed in MSBs 
# if total number is > 9 position then all integer digits will be consider 

# extra digits we can take only 0

a = 50
print("binary form {:b}".format(a))
print("Octal form {:o}".format(a))
a = 542
print("Hexa form lower {:x}".format(a))
print("Hexa form capital {:X}".format(a))