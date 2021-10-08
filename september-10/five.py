#A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

marks = int(input("Enter marks "))
grade = ""
if marks < 25:
    grade = "F"
elif marks>= 25 and marks<45:
    grade = "E"
elif marks>=45 and marks<50:
    grade = "D"
elif marks>=50 and marks<60:
    grade = "C"
elif marks>=60 and marks <80:
    grade = "B"
else:
    grade = "A"
print("Grade is ",grade)