# 1. Ask for an input from the user
# 2. Check if the number is a positive integer
# 3. Run a while loop while its an positive integer
# 4. Check if the input is bigger than the max
# 5. Break out of the loop and print the max number if the user typed in a negitive number

num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
# While loop that checks for the maximum number
while(num_int >= 0):
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))
print("The maximum is", max_int)    # Do not change this line