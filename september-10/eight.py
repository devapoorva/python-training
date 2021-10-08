#Modify the above question to allow student to sit if he/she has medical cause.
#  Ask user 
# if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

total_class = int(input("Enter total class "))
# classes attend
attend_classes = int(input("Enter attended classes "))

# percentage of attend classes 
attendance = (attend_classes * 100)/total_class
print("percentage of class attended ",attendance)
# check 75% above or not
if(attendance>=75):
    print("You are allowed ")
else:
    medical = input("Medical Cause Yes(Y) or No(N) ").lower()
    if(medical=='y'):
        print("You are allowed")
    else:
        print("You are not allowed ")