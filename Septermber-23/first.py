# find digits 
number = int(input("Enter a number "))
reverse_number = 0
while number>0:
    # find last digit 
    last_digit = number %10
    #print(last_digit)
    # remove last digit 
    number = number//10
    # create number (reverse)
    #reverse_number = reverse_number+ (last_digit * (10**count))
    reverse_number = (reverse_number * 10) + last_digit 
    #print(reverse_number)
    #check prime number or not 
    
print("reverse number ",reverse_number)
