# PROBLEM 1
from platform import processor

print("---PROBLEM 1---")

def avg(num1, num2, num3):
    """
    Input three numbers and return the average value.

        parameters:
            num1 (int): A decimal integer
            num2 (int): Another decimal integer
            num3 (int): A third decimal integer

        returns:
            (float): the average of the three numbers
        """
    return (num1 + num2 + num3)/3

# Invoke the avg function using different arguments
print (avg(7, 5, 9))
print (avg(6, 6, 7))



# PROBLEM 2
print("\n---PROBLEM 2---")
'''
# Invoke the avg function using different arguments, but this time before it is declared.
print (avg(7, 5, 9))
print (avg(6, 6, 7))
# Declare the avg function as we did before.
def avg(num1, num2, num3):
    return (num1 + num2 + num3)/3

# This will cause an error because python reads scripts from top to bottom,
# so you cannot call a function before it is declared.
'''
print("NameError")



# PROBLEM 3
print("\n---PROBLEM 3---")
'''
# Declare the avg function first
def avg(num1, num2, num3):
    return (num1 + num2 + num3)/3
# Invoke the avg function using different arguments, but also attempt to print a parameter.
print (avg(7, 5, 9))
print (avg(6, 6, 7))
print(num1)
# This will cause an error, as num1 is a parameter to a function, rather than a declared variable.
'''
print("NameError")



# PROBLEM 4
print("\n---PROBLEM 4---")

def dogToHumanYrs(years):
    """
    Calculate how old a dog is in human years and return the result

    :param years: (int) A decimal number

    :return: (str) A statement containing dog years in the
            argument and its equivalent in human years
    """
    result = 24 + (years - 2) * 4
    return f"{years} dog years is equivalent to about {result} human years."

# use a print statement to call the function
print(dogToHumanYrs(8))

# PROBLEM 5
print("\n---PROBLEM 5---")

def carVal(price, years, nationality):
    """
    Calculate the value of a car based on 3 parameters and return a statement.

    :param price: (int) The price that was originally paid for the car.
    :param years: (int) The amount of years passed.
    :param nationality: (int) The nationality of car.

    :return: (str) A statement containing the new value of the car based on its nationality.
    """
    if nationality.lower() == "german":
        value = format( price * (.95 ** years), ".2f")
        return f"The value of your {nationality} car will be ${value} after {years} years"
    elif nationality.lower() == "japanese":
        value = format( price * (.93 ** years), ".2f")
        return f"The value of your {nationality} car will be ${value} after {years} years"
    elif nationality.lower() == "italian":
        value = format( price * (1.05 ** years), ".2f")
        return f"The value of your {nationality} car will be ${value} after {years} years"

# Call the function using different arguments for the nationality to see the differences.
print(carVal(2500, 10, "German"))
print(carVal(2500, 10, "Japanese"))
print(carVal(2500, 10, "Italian"))



# PROBLEM 6
print("\n---PROBLEM 6---")

def dogAgeCalc(years):
    """
    Calculate how old a dog is in human years and return the result

    :param years: (int) The dog's age

    :return: (int) The dog's age in human years
    """
    result = 24 + (years - 2) * 4
    return result

# Ask the user for their dog's name and age
dogName = input("What is your dog's name? ")
dogAge = int(input("How old is your dog? "))
# Print a statement telling them how old their dog is in human years by invoking the function we just created.
print("Your " + dogName + " is " + str(dogAgeCalc(dogAge)) + " human years old.")



# PROBLEM 7
print("\n---PROBLEM 7---")

def icecreamCost(scoops):
    """
    Calculate the cost of the ice cream based on the number of scoops and return it.

    :param scoops: (int) The number of scoops
    :return: (str) A statement telling the customer how much their ice cream costs
    """
    price = format((scoops * 1.15) + 2.25, ".2f")
    return f"A {scoops}-scoop cone will cost ${price}"

# Call the icecreamCost function, but use an input as its argument. Print the result.
print(icecreamCost(int(input("How many scoops would you like? "))))