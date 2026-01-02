# Day 2 project: Tip Calculator
# Goal was to create a tip calculator that will calculate a total bill including tip and split it among a certain number of people.
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15%? "))
number_of_people = int(input("How many people to split the bill? "))
bill_after_tip = total_bill + (total_bill * tip / 100)
bill_per_person = bill_after_tip / number_of_people
print(f"Each person should pay: ${round(bill_per_person, 2)}")