import input_handlers
import output_handlers
import time
import replit

########################################

# this is the main body of code for running the program


def run_loop(file_state: bool = True):
    testing_and_debugging_allowed = True  # disable this before sharing publicly
    # loop for command input
    user_input = ""
    accepted_input = ["EXIT", "FILE", "PERK", "MAGIC", "ALL", "TEST"]
    while user_input.upper() not in accepted_input:
        print_landing(file_state)
        user_input = input("Please input command: ")

    # valid user input is processed below this point
    # if invalid input will just cycle the above

    # changing whether print to console or file
    if user_input.upper() == "FILE":
        new_file_state = str(not file_state).upper()
        print(f"\nFile Output Mode has been set to {new_file_state}\n")
        reset_loop(not file_state)

        # exiting program
    elif user_input.upper() == "EXIT":
        replit.clear()

        # running all functions
    elif user_input.upper() == "ALL":
        [
            execute_function(i, file_state) for i in accepted_input
            if not i == "TEST"
        ]
        reset_loop(file_state, file_state)

        # this is for development usage only
    elif user_input.upper() == "TEST" and testing_and_debugging_allowed:
        #testing code placed here, subject to change
        #print(input_handlers.parse_magic())
        #input_handlers.parse_magic()
        pass

        # running any function
    else:
        execute_function(user_input.upper(), file_state)
        reset_loop(file_state, file_state)
        # input not acceptable for this is caught earlier
        # functions not implemented yet will do nothing


########################################

# this code handles executing functions from output_handlers.py, using functions from input_handlers.py to process raw text collected from EnaiSiaion's files on ModNexus.


def execute_function(function_input, file_state: bool = True):
    if function_input == "PERK":
        # print organised ordinator text dump data
        output_handlers.parser_printer(
            input_handlers.parse_ordinator(),
            "excel_formatted_output/perk_list_output.txt", file_state)
    elif function_input == "MAGIC":
        # print organised apocalypse and triumvirate text dump data
        output_handlers.parser_printer(
            input_handlers.parse_apocalypse(),
            "excel_formatted_output/spell_list_output.txt", file_state)
        #append triumvirate output
        output_handlers.parser_printer(
            input_handlers.parse_triumvirate(),
            "excel_formatted_output/spell_list_output.txt", file_state, False)


########################################

# this code resets the console


def reset_loop(file_state: bool = True, clear_console: bool = True):
    time.sleep(2)
    if clear_console:  # if printing to console we don't want to clear
        replit.clear()
    else:
        print("\n\n")
    run_loop(file_state)


########################################

# this code executes every time the loop executes, forming a text GUI
# default text-GUI on running loop


def print_landing(file_state: bool):
    print("\n\n#########################")
    print(
        "Accepted commands:\nEXIT << Exits program\nFILE << toggles print mode versus output to file mode\nPERK << executes perk (Ordinator) function\nMAGIC << executes magic (Apocalypse/Triumvirate) functions\nALL << execute all functions\n\n(File Output Mode currently set to {0})"
        .format(str(file_state).upper()))
    print("#########################\n")


########################################
# main body below, program starts here then falls into permanent loop
########################################

run_loop()
