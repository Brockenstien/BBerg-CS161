# PROBLEM 1
print("---Problem 1---")

# Tell the user to enter two phrases, one in all caps
phraseInitial = input("Please enter a phrase: ")
phraseCaps = input("Enter that same phrase, but in all caps: ")

# If the initial phrase in all capitals is the same as the second one, print a statement
if phraseInitial.upper() == phraseCaps:
    print("I'M NOT SHOUTING, YOU'RE SHOUTING!")
else:
    print("oi")



# PROBLEM 2
print("\n---Problem 2---")

# Set two counters and a flag
vowelCount = 0
yVowel = 0
plural = True

# Ask the user for a new phrase
vowelPhrase = input("Please enter a new phrase: ")

# Count the number of unique vowels by checking if each on is in the string
if "a" in vowelPhrase:
    vowelCount += 1
if "e" in vowelPhrase:
    vowelCount += 1
if "i" in vowelPhrase:
    vowelCount += 1
if "o" in vowelPhrase:
    vowelCount += 1
if "u" in vowelPhrase:
    vowelCount += 1
if "y" in vowelPhrase:
    yVowel += vowelCount + 1

# If there is only one, swap the flag
if vowelCount == 1:
    plural = False

# Inform the user, change are to is if the plural flag is false
print(f"There {"are" if plural == True else "is"} {str(vowelCount)}"
      f" unique vowel{"s" if plural == True else ""} in \"{vowelPhrase}\"!")
# If there are any y's, tell the user
if yVowel != 0:
    print(f"If you include y, then you have {str(yVowel)}")



# PROBLEM 3
print("\n---Problem 3---")

# Tell the user to enter two words
word1 = input("Enter a word: ")
word2 = input("Enter a second word: ")

# If they are the same, tell the user. If they are different, tell the user which comes first alphabetically
if word1 == word2:
    print("Those are the same word!")
elif word1 < word2:
    print(word1 + " comes before " + word2)
else:
    print(word2 + " comes before " + word1)



# PROBLEM 4
print("\n---Problem 4---")

# Ask the user to enter their email twice
email = input("Enter your email address: ")
emailConf = input("Enter your email address again: ")

# While they aren't the same, inform the user and make them reenter their email
while email != emailConf:
    print("Inputs do not match!")

    email = input("\nEnter your email address: ")
    emailConf = input("Enter your email address again: ")

# Once they are the same inform the user
print("Success!")



# PROBLEM 5
print("\n---Problem 5---")

import time

def factorial_iter(num):
    """
    Find the factorial of the inputted number

    :param num: (int) any positive integer
    :return: (int) the factorial of that number
    """
    # For 0 and 1, the factorial is just 1
    if num == 0 or num == 1:
        return 1

    # Set a counter equal to the initial number
    i = num
    # While i > 1, reduce i by 1 and multiply num by i
    while i > 1:
        i -= 1
        num *= i

    # Return the final number
    return num


def factorial_recur(num):
    """
    Find the factorial of the inputted number

    :param num: (int) any positive integer
    :return: (int) the factorial of that number
    """
    # Factorial of 0 and 1 is just 1
    if num == 0 or num == 1:
        return 1
    # Otherwise multiply the number by the result of this function with num as 1 less
    return num * factorial_recur(num - 1)


def functiontime(function, argument):
    """
    Check how long a function takes in ns

    :param function: (func) Any function
    :param argument: (any) The argument placed in the function
    :return: the time taken in nanoseconds
    """
    # Start a stopwatch
    start = time.perf_counter_ns()

    # Inform the user of the result of their argument factorial
    print(f"{argument}! is equal to {function(argument)}")

    # Stop the stopwatch
    stop = time.perf_counter_ns()
    # Inform the user the name of the function and how long it took
    return print(f"{function.__name__} took {stop - start} ns\n")

# Make a set of numbers to test the functions on
toTest = {3, 10, 25}

# Test each one
for num in toTest:
    functiontime(factorial_iter, num)
    functiontime(factorial_recur, num)

# It appears that in general, recurring the function is faster than iterating it.
# This becomes more apparent as the number of repeats grows larger.
