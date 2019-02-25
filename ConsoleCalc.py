# ==============================
# CONSOLE CALCULATOR APPLICATION
# ==============================
#
# Author: JMB Downing
# Last Modified: 2018-02-24
#
# =========================================
# Functions called by the main program loop
# =========================================
#
# Single value output displaying fractions specified so use fraction library 
# to handle division
import fractions as fra
#
# --------------------------------------------------------
# Print the instructions for how to use console calculator
def print_instructions():
    print("============")
    print("INSTRUCTIONS")
    print("============")
    print("")
    print("Console calculator performs basic arithmatical operations on integers.")
    print("")
    print("Usage:")
    print("Enter the first integer, a space, the desired mathematical operation (+-*/), ")
    print("a second space, then the second integer, and hit the ENTER key. Allowed mathematical ")
    print("operations are addition (+), subtraction (-), multiplication (*), and division (/).")
    print("Output will be a single integer in the case of addition, subtraction, or multiplication ")
    print("and will be a lowest common divisor fraction in the case of division.")
    print("")
    print("Prototype inputs:")
    print(" - Addition: a + b")
    print(" - Subtraction: a - b")
    print(" - Multiplication: a * b")
    print(" - Division: a / b")
    print("")
#
# --------------------------------------------------------------------------------------
# Take command line input from the user to choose a calculation or view the instructions
def user_input():
# get the input
    print("Enter desired computation.  Press ENTER to repeat instructions.")
    input_string = input("> ")
# determine if the user wants to do a calculation or wants to reprint the instructions
    if len(input_string) == 0:       # user wants instructions
        first_input = 0
        operator = "i"
        second_input = 0
    else:                          # user wants to do a calculation
        split_input = str.split(input_string)
        if len(split_input) == 3:  # well-formatted input
            operator = split_input[1]
            if operator not in ["+", "-", "*", "/"]: # make sure the operation is valid
                print("Invalid operation requested, please review the instructions")
                print("")
                operator = "i"
            try:                   # convert first user input to integer if possible
                first_input = int(split_input[0])
            except ValueError:
                print("First number is not an integer, please review the instructions.")
                print("")
                first_input = 0
                operator = "i"
            try:                    # convert second user input to integer if possible
                second_input = int(split_input[2])
            except ValueError:
                print("Second Number is not an integer, please review the instructions.")
                print("")
                second_input = 1
                operator = "i"
        else:                      # improperly formatted input
            print("Improperly formatted input, please review the instructions:")
            print("")
            first_input = 0
            second_input = 1
            operator = "i"
    return(first_input, operator, second_input)
#
# ---------------------------------------------------------------------------------------------
# Print the output of the arithmatic operation, tell user if there has been a calculation error
def print_result(final_value, error_type):
    if error_type == 0:          # no cacluation problems, print result
        print(">", final_value)
    elif error_type == 1:        # has been a mathematical error (e.g. div by 0)
        print("There has been a mathematical error, no result possible!")
    elif error_type == 2:        # user has requested instructions, nothing to do
        print("")
    else:
        print("Undentified error, please try again!")
#
# ---------------------
# Arithmetic operations
#
# Perform the addition operation
def calc_add(value1, value2):
    calc_value = value1 + value2
    err_code = 0
    return(calc_value, err_code)
#
# Perform the subtraction operation
def calc_subtract(value1, value2):
    calc_value = value1 - value2
    err_code = 0
    return(calc_value, err_code)
#
# Perform the multiplication operation
def calc_multiply(value1, value2):
    calc_value = value1 * value2
    err_code = 0
    return(calc_value, err_code)
#
# Perform the division opearation
def calc_divide(value1, value2):
    calc_value = 0
    if value2 == 0:
        print("Division by zero not mathematically possible!")
        err_code = 1
    else:
        calc_value = fra.Fraction(value1, value2)
        err_code = 0
    return(calc_value, err_code)
#
# -----------------------------------------------------
# User decides if they want to keep running the program
def choose_run_state():
    run_switch = True
    end_calc = input("Perform another cacluation? Enter Y for yes, N for no: ")
    if end_calc.lower() == "y":
        run_switch = True
    elif end_calc.lower () == "n":
        run_switch = False
        print("")
        print("Exiting Console Calculator")
        print("")
    else:
        print("Invalid option, will treat as yes")
    return(run_switch)
#
# ====================================================================
# Main routine that calls functions for input, computation, and output
# ====================================================================
#
# Welcome text
print("==================")
print("CONSOLE CALCULATOR")
print("==================")
print("")
print("Welcome to console calculator! This program performs addition, subtraction ")
print("multiplication, or division of integers.")
print("")
#
# Print instructions each time Console Calculator is opened
print_instructions()
#
# Keep the program running until user is done
run_calc = True
while run_calc:
#
# Get the numbers and desired operation from the user
    user_int1, user_op, user_int2 = user_input()
#
# Determine the opeation the user desires and perform the appropriate calcluation.  Also
# set an error code in case calcuation was unsuccesful
    calc_result = 0
    error_code = 0
    if user_op == "+":
        calc_result, error_code = calc_add(user_int1, user_int2)
    elif user_op == "-":
        calc_result, error_code = calc_subtract(user_int1, user_int2)
    elif user_op == "*":
        calc_result, error_code = calc_multiply(user_int1, user_int2)
    elif user_op == "/":
        calc_result, error_code = calc_divide(user_int1, user_int2)
    elif user_op == "i":
        print_instructions()
        error_code = 2
#
# Output the calculator results to the terminal screen
    print_result(calc_result, error_code)
#
# Determine whether to end program
    run_calc = choose_run_state()