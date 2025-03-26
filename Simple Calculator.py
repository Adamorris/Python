while True: # sets the following loop to function while true
    try:
         a = float(input("First number: ")) # a = number of user input
         break # breaks the loop when a valid number is entered
    except ValueError: # if the input is not a number then ---
     print("Invalid - must be a number") # print invalid # Because the loop was never broken, it asks for the first number again. This will repeat until a valid number is entered
while True: # sets the following loop to function while true 
    try:
         b = float(input("Second number: ")) # a = number of user input
         break # breaks the loop when a valid number is entered
    except ValueError: # if the input is not a number then ---
     print("Invalid - must be a number") # print invalid # Because the loop was never broken, it asks for the first number again. This will repeat until a valid number is entered
Sum = a + b # sets "sum" to equal "a" + "b"
print("Sum: " +str(Sum)) # prints the word "sum:" and the sum created above as a string
