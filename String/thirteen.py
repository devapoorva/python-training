# Changing case of a string 

# 1. upper() : To convert all character to upper case 
# 2. lower() : To convert all character to lower case 
# 3. swapcase() : convert all lower case to upper case and upper case to lower case 
# 4. title() : to convert all character to title case. i.e. first character 
# in every word should be upper case and all remaining character should 
# be in lower case
# 5. capitalize() : Only first character will be converted to upper case and 
# all remaining character can be converted to lower case

# camel case : ComputerGate 

s = "I am a boy"
print(s.upper()) # I AM A BOY
print(s.lower()) # i am a boy
print(s.swapcase()) #i AM A BOY
print(s.title()) # I Am A Boy
print(s.capitalize()) #I am a boy