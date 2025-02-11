# PROBLEMS 1 - 3

print("---Problems 1 - 3---")

# Tell the user to input a number and another number to decrement by
x = int(input("Enter a number: "))
decrement = int(input("Enter a number to decrease by: "))

while x > 0:
    # Inform the user if the current number is even or odd
    if x % 2 == 0:
        print(f"{x} is even!")
    else:
        print(f"{x} is odd!")

    # Decrement x by the number specified by the user
    x -= decrement

# Once x <= 0, print "Blastoff!"
print("Blastoff!")



# PROBLEM 4
print("\n---Problem 4---")

# Tell the user to enter a word
userWord = input("Enter a word: ")
# Initialize a counter
wordcount = 0

# While true (keep running this until it reaches a break)
while True:
    # Tell the user how many characters are in their word
    print(f"{userWord} has {len(userWord)} characters")

    # If the word entered is less than 5 characters, break the loop
    if len(userWord) < 5:
        print("Goodbye")
        break

    # Increment wordcount
    wordcount += 1
    # If 5 words have been entered, break the loop
    if wordcount == 5:
        print("Surely you have something better to do...")
        break

    # Tell the user to enter another word
    userWord = input("Enter another word: ")



# PROBLEM 5
print("\n---Problem 5---")

# Initialize a counter
y = 10

# While it is less than 100, print it in decimal, binary, and hexadecimal, then increment it.
while y <= 100:
    print(y, bin(y), hex(y))

    y += 1



# PROBLEM 6
print("\n---Problem 6---")

def stars_iteration(count):
    """
    Get a number from the user and print out that many stars, decrementing and repeating each line
    by iterating through the count

    :param count: (int) The initial amount of stars to print
    :return: (str) Several lines of stars that decrement as they go down
    """
    while count > 0:
        print("*" * count)
        count -= 1

def stars_recursion(count):
    """
    Get a number from the user and print out that many stars, decrementing and repeating each line
    by calling the function within itself

    :param count: (int) The initial amount of stars to print
    :return: (str) Several lines of stars that decrement as they go down
    """
    if count <= 0:
        return

    print("*" * count)
    stars_recursion(count - 1)

# Tell the user to enter a number, then input it into each of the functions
starcount = int(input("Enter a number: "))
stars_iteration(starcount)
stars_recursion(starcount)



# PROBLEM 7
print("\n---Problem 7---")

def digit_sum(num):
    """
    Calculate the sum of a number's digits until it gets down to one digit

    :param num: (int) The initial number
    :return: (int) A sum of all the digits of that number
    """
    # if the number is 0, return 0. Otherwise, mod it by 10 to get the last digit (193 / 10 == 19 + remainder 3)
    # Then add it to the result of this function without that last digit.
    # Remove it with floor division (193 / 10 = 19.3, drop the decimal to get 19)
    if num == 0:
        return 0
    return (num % 10) + digit_sum(num // 10)

# Tell the user to enter a number and run it through digit_sum
print(digit_sum(int(input("Enter a number: "))))


def is_palindrome(word):
    """
    Check if a word is a palindrome and inform the user

    :param word: (str) Any string the user enters
    :return: (bool) A true or false statement
    """
    # if the word is 1 or fewer characters, return true
    if len(word) <= 1:
        return True
    # if the first character and the last character are not the same, return false
    if word[0] != word[-1]:
        return False

    # Run the function again, but with a substring that doesn't include the first or last characters of the original
    return is_palindrome(word[1:-1])


# Tell the user to enter a word. Make it case-insensitive
initialWord = input("Enter a word: ").lower()

# Inform the user whether their word is a palindrome or not.
if is_palindrome(initialWord):
    print(f"{initialWord} is a palindrome!")
else:
    print(f"{initialWord} is not a palindrome")
