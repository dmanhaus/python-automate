from curses.ascii import isdigit
import operator, sys

# Data we need - (Dont worry about these next three lines, we'll learn about lists and tuples in Chapter 4) 
operators = [('1) Exponent', '**'), ('2) Modulus/remainder','%'), ('3) Integer division/floored quotient','//'), ('4) Division','/'), ('5) Multiplication','*'), ('6) Subtraction','-'), ('7) Addition','+')]
operator_functions = [operator.pow, operator.mod, operator.floordiv, operator.truediv, operator.mul, operator.sub, operator.add]
terms = [(2,3), (22,8), (22,8), (22,8), (3,5), (5,2), (2,2)]

print('1) Exponent')
print('2) Modulus/remainder')
print('3) Integer division/floored quotient')
print('4) Division')
print('5) Multiplication')
print('6) Subtraction')
print('7) Addition')

while True:
    # Get input from the user and assign it to the "index" variable - (Question: What type of data is stored in "index" at this moment?)
    index = input('Enter the number corresponding to the operator to run (press "q" to quit): ')

    if index == "q":
        sys.exit()

    if index.strip().isdigit():                                                  # Is the input a number? If it is, get the corresponding operator function and terms from the data and calculate the result
        while (int(index) < 1 or int(index) > 7):                     # is the input number within the range of operator_functions provided?
            index = input(f'Please choose a number between 1 and 7: ')
            
        index = int(index)                                                   # A list index begins with 0, so we need to subtract one from the number provided by the user input to choose the right list item   
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
        
        result = operator_function(first_term, second_term)  
        print(f'{operator_name}: {first_term} {operator_symbol} {second_term} = {result}')