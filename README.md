python-automate
===============

A collection of code samples and explorations inspired by
"Automate the Boring Stuff" 
(by Al Sweigart - https://automatetheboringstuff.com/#toc)

- [python-automate](#python-automate)
  - [Chapter 1](#chapter-1)
    - [first_program.py](#first_programpy)
    - [calculator.py](#calculatorpy)
  - [Chapter 2](#chapter-2)
    - [calculator.py](#calculatorpy-1)
  - [Chapter 3](#chapter-3)
    - [calculator.py](#calculatorpy-2)

## Chapter 1
Chapter 1 gives us very basic tools to work with:
- operations
- data types
- string concatenation & replication
- variable naming & assignment
- the input() function to collect input
- the print() function to display output
- the str(), int() and float() functions to convert types
  
### [first_program.py](chapter_01/first_program.py) 

The expanded "Hello World" example from the text, which simulates a conversation
with the user and calculates some simple information about the user's name and age.
At this point, there's no validation of the user input, so it's easy for errors to
creep into the results when the user inputs unexpected data.

### [calculator.py](chapter_01/calculator.py) 

A _very_ simple demonstration combining input and operators to do math. 
Here, we have an opportunity to learn first-hand about [code duplication](https://en.wikipedia.org/wiki/Duplicate_code), and why it's generally a bad thing.

## Chapter 2
This chapter gives us flow control.  Now we can:
  - use booleans returned by comparison operators to determine if values meet specific conditions
  - use **if...elif...else** code blocks to execute specific pieces of code in response to comparison results
  - use **while...loop**, **break**, and **continue** to repeat code until conditions are met
  - use **for...range** loops to create predetermined or variable-control loops to repeat code 
  - **import** modules from outside of our code to gain use of their functions

### [calculator.py](chapter_02/calculator.py)

Now our simple calculator program gives the user some control over which of its predefined 
operator examples runs.  And we get to import the **operator** module so we can call
operators programmatically within our code

**Important** - This module depends on the curses package, which is included in unix-based distributions, but **not** in Windows distribution of python.  To avoid a dependency error running this module, install the [windows-curses](https://pypi.org/project/windows-curses/) package:
```
pip install windows-curses
```

## Chapter 3
This chapter gives us the power to write our own functions, start to wrap our heads around
local vs. global scope, introduces the concept of None to represent the lack of a value,
and handle errors that may occur in our code more elegantly

### [calculator.py](chapter_03/calculator.py)

Now we can refactor our code to eliminate some repetition by creating one dual-purpose function
that can either list out all the operators we can run, or calculate results using terms
we pre-define for each type of operator.

