# Homework 2A
# Author: James Hay
# Date: 2025/08/21

print("Hello, my name is James")
print("\n")

my_id = 1340549
my_id_str = "G01340549"

print("my bare id is: " + str(my_id))
print("my padded id is: " + "{:08.0f}".format(my_id))
print("my raw id is: " + my_id_str)
print("\n")

print("my dollar amount is: " + "{:0.2f}".format(my_id))
print("my base-2 id is: " + "{0:b}".format(my_id))
print("my hex id is: " + "{0:x}".format(my_id))
print("\n")

my_id_len = len(str(my_id))
first_digit = my_id // 10 ** ( len(str(my_id)) - 1 )
last_digit = my_id % 10
print("the length of my id is: " + str(my_id_len))
print("the first digit of my id is: " + str(first_digit))
print("the last digit of my id is: " + str(last_digit))

print("the first and last digits of my id concatenated is: " + str(first_digit) + str(last_digit))