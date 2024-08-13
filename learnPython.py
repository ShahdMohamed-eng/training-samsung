# This function will print the average of 3 numbers

def average():
    # Prompt the user to enter three numbers
    numbers = input("Enter three numbers separated by spaces: ").split()

    # Convert the input strings to integers
    num1, num2, num3 = map(int, numbers)

    # Calculate and print the average
    print((num1 + num2 + num3) / 3)
# Call the average function
average()
