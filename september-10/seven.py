#A student will not be allowed to sit in exam 
# if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

#total class 

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
    print("You are not allowed")
    
