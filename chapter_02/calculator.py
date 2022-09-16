from curses.ascii import isdigit
import operator, sys

# Data we need - (Dont worry about these next three lines, we'll learn about lists and tuples in Chapter 4) 
operators = [('1) Exponent', '**'), ('2) Modulus/remainder','%'), ('3) Integer division/floored quotient','//'), ('4) Division','/'), ('5) Multiplication','*'), ('6) Subtraction','-'), ('7) Addition','+')]
operator_functions = [operator.pow, operator.mod, operator.floordiv, operator.truediv, operator.mul, operator.sub, operator.add]
terms = [(2,3), (22,8), (22,8), (22,8), (3,5), (5,2), (2,2)]

# Loop through the list called "operators" and print the text in the first element of each tuple in the list  
for item in operators:
    print(item[0])

while True:
    # Get input from the user and assign it to the "index" variable - (Question: What type of data is stored in "index" at this moment?)
    index = input('Enter the number corresponding to the operator to run (press enter to run all operators, "q" to quit): ')

    if index == "q":
        sys.exit()

    if index.strip().isdigit():                                                  # Is the input a number? If it is, get the corresponding operator function and terms from the data and calculate the result
        while (int(index) < 1 or int(index) > len(operators)):                     # is the input number within the range of operator_functions provided?
            index = input(f'Please choose a number between 1 and {len(operators)}: ')
            
        index = int(index) - 1                                                   # A list index begins with 0, so we need to subtract one from the number provided by the user input to choose the right list item   
        operator_name = operators[index][0]
        operator_symbol = operators[index][1]
        first_term = terms[index][0]
        second_term = terms[index][1]
        result = operator_functions[index](first_term, second_term)          # Run the operator function for the terms provided
        print(f'{operator_name}: {first_term} {operator_symbol} {second_term} = {result}')
    else:                                                                        # Run all the operator functions against the terms provided
        for index in range(0, len(operators)):
            operator_name = operators[index][0]
            operator_symbol = operators[index][1]
            first_term = terms[index][0]
            second_term = terms[index][1]
            result = operator_functions[index](first_term, second_term)
            print(f'{operator_name}: {first_term} {operator_symbol} {second_term} = {result}')