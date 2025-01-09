# PROBLEM 1
# Declare string variables for the pet's type and name
pet_type = "dog"
pet_name = "Zoey"

# Use an f-string to input the variables straight into a print statement without concatenation.
print(f"I have a {pet_type} and her name is {pet_name}.")



# PROBLEM 2
# Declare variables requiring input from the user
user_name = input("Please enter your first name: ")
user_age = int(input("Please enter your age: "))
user_savings = int(input("Please enter your yearly savings: "))

# Declare variables that take inputted data and alter it
future_age = user_age + 10
future_savings = user_savings * 5
monthly_savings = user_savings // 12

# Print out statements on multiple lines containing all the variables
print(f"Hello {user_name}! You are currently {user_age} years old.\n"
      f"In 10 years, you will be {future_age} years old.\n"
      f"If you save ${user_savings} each year, in 5 years you will have saved ${future_savings}.\n"
      f"Your average monthly savings is ${monthly_savings:.2f}.")



# PROBLEM 3
# Import the calendar library
import calendar

# Declare a variable that gets the days from the month
# I used a random variable name to get the first day output so that I could just have the number of days
___, num_days = calendar.monthrange(2025, 1)

# calculate the number of hours, then minutes, then seconds
num_hours = num_days * 24
num_minutes = num_hours * 60
num_seconds = num_minutes * 60

# print out the number of seconds in January with an f-string
print(f"The number of seconds in January is {num_seconds}")



# PROBLEM 4
# ask the user how many eggs he has
# Also, my last teacher wanted me to just do the prints and inputs exactly as stated
# Can I do dumb inputs like this or is it just easier if I do it exactly? Thanks --Brock B
num_eggs = int(input("How many eggs do you have? I really need to know, man: "))

# Calculate the dozens of eggs and the leftover amount
dozens_eggs = num_eggs // 12
leftover_eggs = num_eggs % 12

# Inform the user how many dozens and leftovers there are
print(f"Thanks. That makes {dozens_eggs} dozen eggs with {leftover_eggs} left over!")
