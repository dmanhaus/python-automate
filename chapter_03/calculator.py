from curses.ascii import isdigit
import operator, sys

def calculate_term(index, print_list_of_terms=False):
    if index == 1:
        operator_name = '1) Exponent'
        operator_symbol = '**'
        operator_function = operator.pow
        first_term = 2
        second_term = 3
    elif index == 2:
        operator_name = '2) Modulus/remainder'
        operator_symbol = '%'
        operator_function = operator.mod
        first_term = 22
        second_term = 8
    elif index == 3:
        operator_name = '3) Integer division/floored quotient'
        operator_symbol = '//'
        operator_function = operator.floordiv
        first_term = 22
        second_term = 8        
    elif index == 4:
        operator_name = '4) Division'
        operator_symbol = '/'
        operator_function = operator.truediv
        first_term = 22
        second_term = 8              
    elif index == 5:
        operator_name = '5) Multiplication'
        operator_symbol = '*'
        operator_function = operator.mul
        first_term = 3
        second_term = 5
    elif index == 6:
        operator_name = '6) Subtraction'
        operator_symbol = '-'
        operator_function = operator.sub
        first_term = 5
        second_term = 2        
    elif index == 7:
        operator_name = '7) Addition'
        operator_symbol = '+'
        operator_function = operator.add
        first_term = 2
        second_term = 2        
    
    result = operator_function(first_term, second_term)          # Run the operator function for the terms provided
    if print_list_of_terms:
        print(operator_name)
    else:
        print(f'{operator_name}: {first_term} {operator_symbol} {second_term} = {result}')

# Loop through the list called "operators" and print the text in the first element of each tuple in the list  
for index in range(1,8):
    calculate_term(index, True)

while True:
    # Get input from the user and assign it to the "index" variable - (Question: What type of data is stored in "index" at this moment?)
    index = input('Enter the number corresponding to the operator to run (press enter to run all operators, "q" to quit): ')

    if index == "q":
        sys.exit()

    if index.strip().isdigit():                                                  # Is the input a number? If it is, get the corresponding operator function and terms from the data and calculate the result
        while (int(index) < 1 or int(index) > 7):                                # is the input number within the range of operator_functions provided?
            index = input(f'Please choose a number between 1 and 7: ')
            
        index = int(index)                                                   
        calculate_term(index)
    else:                                                                        # Run all the operator functions against the terms provided
        for index in range(1, 8):
            calculate_term(index)