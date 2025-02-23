# PROBLEM 1

print("---Problem 1---")

# Tell the user to enter two numbers
lowNum = int(input("Enter a number to start at: "))
highNum = int(input("Enter a number to end with: "))

# Create an empty string to hold the even numbers and a variable that we will iterate
evenNums = ""
tempNum = lowNum

# Check each number between the two user specified numbers
# If they are even, concatenate them to the evenNums string
# Iterate tempNum
while tempNum <= highNum:
    if tempNum % 2 == 0:
        evenNums += str(tempNum) + " "
    tempNum += 1

# Inform the user of the data retrieved
print(f"The even numbers between {lowNum} and {highNum} are: {evenNums}")



# PROBLEM 2
print("\n---Problem 2---")

# Tell the user to enter a positive integer
posInt = int(input("Enter a positive integer: "))

# Create an empty string and reset tempNum as an iterable variable
factors = ""
tempNum = 1

# Check each number between 1 and the user's number and see if it factors evenly.
# If it does, add it to the string.
while tempNum <= posInt:
    if posInt % tempNum == 0:
        factors += str(tempNum) + " "
    tempNum += 1

# Inform the user of the factors of their entered number
print(f"The factors of {posInt} are: {factors}")



# PROBLEM 3
print("\n---Problem 3---")

# Make an array containing all the letters of the alphabet
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# Tell the user to enter their name
userName = input("Enter your name: ").lower()
# Initialize a total
letterVal = 0

# For each letter in their name, check its numeric position in the alphabet array and add it to the total
for letter in userName:
    i = 0
    while letter != alphabet[i]:
        i += 1
    letterVal += i

# Inform the user
print(f"The value of the numeric positions of the letters in your name is {letterVal}")



# PROBLEM 4
print("\n---Problem 4---")

# Tell the user to enter a number
squaresInt = int(input("Enter a positive integer: "))


def squares(integer):
    """
    Take in a positive int and list the squares of each of the numbers <= it

    :param integer: (int) Any positive integer
    :return: (str) A list of squared numbers
    """

    # Once integer gets to 0, stop recurring
    if integer == 0:
        return
    else:
        # Preform the same function, but decrement integer
        squares(integer - 1)
        # Print each integer squared (after recursion so it produces an ascending list
        print (integer * integer)

# Call the function with the number the user entered
squares(squaresInt)


# PROBLEM 5
print("\n---Problem 5---")

def teepee_sort(numList):
    """
    Take in a list of integers and sort them, largest in the middle,
     evens descending on the right and odds ascending on the left

    :param numList: (array) A list of integers
    :return: (array) the same list sorted in a new way
    """

    # First check if numList is empty so it doesn't break
    if not numList:
        return []

    # Sort numList in ascending order and take out the last one (the largest number)
    numList.sort()
    largest = numList.pop()

    # split the remaining numbers into evens and odds.
    # Doing it this way creates a new array that adds a copy of the number
    # for each number in the list as long as it is even (or odd in the second one)
    evens = [num for num in numList if num % 2 == 0]
    odds = [num for num in numList if num % 2 != 0]

    # sort the evens in descending order and the odds in ascending order
    evens.sort(reverse=True)
    odds.sort()

    # Print out a new list containing each of the sublists
    return print(odds + [largest] + evens)

# Test the function with random numbers
teepee_sort([12, 43, 22, 34, 2, 21, 3, 33, 81])



# PROBLEM 6
print("\n---Problem 6---")

def permutations(digits):
    """
    take in a number that contains each digit 1-9 only once and
    output the next permutation (the next lowest arrangement of the digits)

    :param digits: (int) a number containing each digit 1-9 once and only once
    :return: (int) the next permutation of the digits
    """

    # Turn the number into a list so we can swap stuff around
    digits = list(digits)
    n = len(digits)

    if digits == sorted(digits, reverse = True):
        return "This is the largest permutation"

    def find_pivot(index):
        """
        Find the first decreasing set from the right

        :param index: (int) the index of a number in the digits array
        :return: (int) the index of a number that is smaller than the one checked before
        """

        # If the digit left of the digit we are checking is smaller, then return that index
        if digits[index - 1] < digits[index]:
            return index - 1
        # Otherwise go again, but one to the left
        return find_pivot(index - 1)

    # Find the pivot, starting with the last index
    pivot = find_pivot(n - 1)


    def find_swap(index):
        """
        Find the smallest digit larger than the pivot to swap with

        :param index: (int) the index of a number in the digits array
        :return: (int) the index of the smallest digit larger than the pivot
        """

        # Starting from the right, if the value is more than the pivot's value, get that index
        if digits[index] > digits[pivot]:
            return index
        # Otherwise check the next one
        return find_swap(index - 1)

    to_swap = find_swap(n - 1)

    # Swap the pivot with the toSwap
    digits[pivot], digits[to_swap] = digits[to_swap], digits[pivot]


    def reverse_end(start, end):
        """
        Reverse the necessary digits after the pivot to ensure we get the smallest permutation

        :param start: (int) the index right after the pivot
        :param end: (int) the last index
        :return: an altered section of the digits after the pivot
        """
        # if the start is less than the end, swap them and repeat the function with the next pair in
        if start < end:
            digits[start], digits[end] = digits[end], digits[start]
            reverse_end(start + 1, end - 1)

    # Call the function
    reverse_end(pivot + 1, n - 1)

    # Stick all the numbers in the list back together into a string
    return "".join(digits)

# Test the function
print(permutations("123456789"))