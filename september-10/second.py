#A company decided to give bonus of 5% to employee if his/her year of service is 
# more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary = float(input("Enter Employee Salary ")) # $50.5
year_of_service = int(input("Enter year of service "))
total_bonus = 0
if year_of_service>5:
    # give bonus
    total_bonus = (salary * 5)/100
    salary+= total_bonus

print("Net Bonus is ",total_bonus)
print("Total Salary is ",salary)