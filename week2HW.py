# PRACTICE 1
print("---PRACTICE 1---")
# Declare x as an integer.
x = 31
# Print the value of x, x in binary, and x in hexadecimal.
print(x, bin(x), hex(x))



# PRACTICE 2
print("\n---PRACTICE 2---")
# Set x to a float
x = 1.825
# Print the value of x, x in binary, and x in hexadecimal.
## print(x, bin(x), hex(x))
print("TYPE ERROR")
# This will give a Type Error.
# The functions bin() and hex() are both designed for integer values, and we put a floating-point value through them.

# Set x back to an integer
x = 18



# PRACTICE 3
print("\n---PRACTICE 3---")
# Declare y as a value in binary
y = 0b1011
# Declare z as a value in hexadecimal
z = 0xA3
# Print them. They come out as numbers in base 10
print(y, z)



# PRACTICE 4
print("\n---PRACTICE 4---")
# Each number can still be added, even though they are in different forms
w = x + y + z
print ('the sum is ' , w)




# COMPRESSION
print("\n---COMPRESSION---")
# Declare variables containing values pertaining to the formula for calculating compression.
origSize = 300
dictSize = 50
compSize = 100

# calculate the compression percent and store the values.
totalSize = dictSize + compSize
compPercent = (1 - (totalSize/origSize)) * 100

# Print out all our data in an organized format using f-strings.
print(f"Compressed text size: {compSize} characters\n"
      f"     Dictionary size: {dictSize} characters\n"
      f"               Total: {totalSize} characters\n"
      f"  Original text size: {origSize} characters\n"
      f"         Compression: {compPercent:.2f}%")