# Prompth user to enter a number / test if even or odd

input = input("Please enter an integer: ")
# should add an exception to catch type error
number = int(input)

if number % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")
