# PROBLEM 1
print("---PROBLEM 1---")
# Declare a variable that gets the user's name
userName = input("Enter your name here: ")
# Print out a message welcoming the user
print(f"Hello {userName}!")



# PROBLEM 2
print("\n---PROBLEM 2---")
# Ask the user for their age, but you have to make sure you make it is an integer.
# Otherwise, it will attempt to add a string containing a number to an integer
userAge = int(input("How old are you? "))
# Print out how old they will be in five years.
print(userAge + 5)



# PROBLEM 3
print("\n---PROBLEM 3---")
# Ask the user for a number to add to their age. Set it to an integer.
ageAdd = int(input("How many years do you want to add? "))
# You have to convert userAge back to a string to properly concatenate.
print(f"In {ageAdd} years, you will be " + str(userAge + ageAdd))



# PROBLEM 4
print("\n---PROBLEM 4---")
# Ask the user how many hours they worked in a week and how much they get paid hourly
hoursWorked = float(input("Enter the number of hours worked on an average week: "))
hourlyWage = float(input("Enter your hourly wage, without the $: "))



# PROBLEM 5
print("\n---PROBLEM 5---")
# Calculate the weekly pay
weeklyPay = (hoursWorked * hourlyWage)
# Print out the weekly pay and annual pay with two decimal places.
print("Your gross pay this week is " + str(format(weeklyPay, ".2f")) +
      "\nYour estimated annual gross pay will be $" + str(format(weeklyPay * 50, ".2f")))