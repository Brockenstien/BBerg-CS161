# PROBLEM 1
print("---Problem 1---")

# Tell the user to enter a number
num = int(input("Enter a number: "))

# Check if it is divisible by 5, and print the result
if num % 5 == 0:
    print("This number is divisible by 5!")
else:
    print("This number is not divisible by 5")



# PROBLEM 2
print("\n---Problem 2---")

# Tell the user to enter a West Coast state
state = input("Enter a West Coast state: ")

# Using if/else, print the capital based on the state
if state == "Oregon":
    print("Salem")
elif state == "California":
    print("Sacramento")
elif state == "Washington":
    print("Olympia")
elif state == "Arizona":
    print("Phoenix")
elif state == "Nevada":
    print("Carson City")
elif state == "Hawaii":
    print("Honolulu")
elif state == "Alaska":
    print("Juneau")
else:
    print("That's not a West Coast State")

# Create a dictionary of West Coast states and their capitals
stateDict = {
    "Oregon": "Salem",
    "California": "Sacramento",
    "Washington": "Olympia",
    "Arizona": "Phoenix",
    "Nevada": "Carson City",
    "Hawaii": "Honolulu",
    "Alaska": "Juneau"
}

# Using the dictionary, print the capital based on the state
print(stateDict.get(state))

# Using match case, print the capital based on the state
match state:
    case "Oregon":
        print("Salem")
    case "California":
        print("Sacramento")
    case "Washington":
        print("Olympia")
    case "Arizona":
        print("Phoenix")
    case "Nevada":
        print("Carson City")
    case "Hawaii":
        print("Honolulu")
    case "Alaska":
        print("Juneau")
    case other:
        print("That's not a West Coast State")


# PROBLEM 3
print("\n---Problem 3---")

def pool_guest(age):
    """
    Get the age of the guest and return an admission price

    :param age: (int) The guest's age

    :return: (int) The admission price in dollars
    """
    # return a value based on the age argument
    if age < 2:
        return 0
    elif age < 12:
        return 3
    elif age < 61:
        return 6
    else:
        return 4

# Test the function
print(pool_guest(23))



# PROBLEM 4
print("\n---Problem 4---")

import requests

# Get the website using requests
cs160Site = requests.get("http://coccbobcat.com")

# Check if it is properly connected
if cs160Site.status_code == 200:

    # If it is, then get the text of the html
    html = cs160Site.text
    # Count how many times the substring "160" appears, and inform the user
    count = html.count("160")
    print(f"The substring '160' appears {count} times in the HTML of http://coccbobcat.com.")
else:
    # If it cant connect, inform the user
    print("Failed to retrieve http://coccbobcat.com")



# PROBLEM 5
print("\n---Problem 5---")

import psutil

# Get a list of all the running processes
processes = list(psutil.process_iter())

# Count the number of processes by checking the length of the list
numProcesses = len(processes)

# Print out that result
print(f"Number of running processes: {numProcesses}")
