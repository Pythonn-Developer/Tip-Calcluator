# Display the greeting
print("Welcome to Tip Calculator")

# Take input of total bill given by the restaurant
total_bill = float(input("What was the total bill? $. "))
# Take input of the % tip the group wants to give
tip_percent = int(input("What % tip would you like to give? "))
# Take input of the no of people in the group
total_people = int(input("How many people to split the bill? "))

# Depending on the tip %, just the tip money will be:
tip_money = (tip_percent * total_bill) / 100
# Adding that tip money to total bill will give you the final amout to be paid
total_money = total_bill + tip_money
# Divide the above total amount amongst the members of group
each_person_money = total_money / total_people

# Display the payment amount each person should pay 
final_amount = "{:.2f}".format(each_person_money)
print(f"Each person shound pay: ${final_amount}")
