#A shop will give discount of 10% if the cost of purchased quantity is 
# more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

quantity = int(input("enter quantity "))
total_cost = quantity * 100
discount = 0
if total_cost>1000:
    # give discount 
    discount = (total_cost * 10 )/100

# total_cost -= discount
grand_total = total_cost - discount
print("total cost ",total_cost)
print("total discount ",discount)
print("grand total cost ",grand_total)



