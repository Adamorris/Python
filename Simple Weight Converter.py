
weight = float(input("Weight: "))             # 2: 'weight' equals the float version(integer with a decimal) of the integer/decimal the user types into the terminal
unit = input("(K)g or (L)bs: ")               # 3: 'unit' equals either K or L depending on which the user inputs
if unit.upper() == "K":                       # 4: if the uppercase version of the input is K then ---
    converted = weight / 0.45                 # 5: 'converted' equals the input of line 2 divided by 0.45 (this converts Kgs into Lbs)
    print("Weight in Lbs: " + str(converted)) # 6: Prints out the string version of the answer of line 5
else:                                         # 7: if the uppercase version of the input of line 3 does not equal K ---
    converted = weight * 0.45                 # 8: 'converted' equals the input of line 2 multiplied by 0.45 (this converts Lbs into Kgs
    print("Weight in Kgs: " + str(converted)) # 9: Prints the string version of the answer to line 8
# an integer is a whole number
# a float is an integer with a decimal
# a string is a piece of text surrounded by "" e.g "height"
# a boolean is a statement, specifically the use of True or False
