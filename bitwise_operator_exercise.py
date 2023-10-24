# 1. convert 4999 to base 2 using python


# converting the decimal number 4999 to its binary representation using the built in bin() function.
# bin() function converts the decimal number 4999 to its binary representation, and the result is a string that starts with 0b.

number: int =4999
print(bin(number))

# 2. convert 2111 to base 2 using python

number: int =2111
print(bin(number))


# 3. what will be the value of 4999 & 2111
4999 & 2111

value_of = 4999 & 2111
value_of = bin(value_of)[2:].zfill(12)  # The [2:] is used to remove the '0b' prefix from the binary representation, and zfill(12) ensures the result is 12 characters long with leading zeros to the left.
print(value_of)


# 4. To find the decimal value of this binary representation, you can use the int() function in Python

value_of = int("000000000111", 2)
print(value_of)

# what will be the value of 4999 | 2111
value_of = 4999 | 2111
value_of = bin(value_of)[2:].zfill(12)
print(value_of)

# The result of the bitwise OR operation between 4999 and 2111 is 100111111111 in binary.

# To find the decimal value of this binary representation, you can use the int() function in Python

value_of = int("1101110111111", 2)
print(value_of)
