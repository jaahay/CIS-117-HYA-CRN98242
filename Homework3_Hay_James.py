# Homework 3
# Author: James Hay
# Date: 2025/08/28

# Problem Statement
# Write a program that:
# Asks the user to enter a highway number (1–999).
# If the number is between 1 and 99:
# Print whether it goes north/south or east/west.
# If the number is between 100 and 999:
# Print that it’s an auxiliary highway and which primary highway it serves.
# Also state the direction of the primary highway it serves.
# If the number is 0 or above 999, print "Invalid highway number." 

highway_number = int(input("Enter a highway number: "))
if highway_number <= 0 or highway_number >= 1000:
    print("Invalid highway number.")
else:
    print("Interstate", highway_number, end='')
    if highway_number // 100 > 0 and highway_number // 100 < 10:
        print(" is an auxiliary highway serving I-", end='')
        print(highway_number % 100, end='')
        print(", which", end='')
    print(" runs east-west." if highway_number % 2 == 0 else " runs north-south.")
