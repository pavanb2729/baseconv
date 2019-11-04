#!/usr/bin/python3

# baseconv.py
#
# Interactively converts hexadecimal, decimal and binary numbers 
# into each other.
#
# Usage:
#     baseconv.py
# This starts the interactive activity.
#
# Filter examples:
# * with a filter for decimal output only:
#     baseconv.py d
# * with a filter for hexadecimal and decimal output only:
#     baseconv.py hd
#
# Date: 2019-11-04
# Designer: Renato Montes
# Programmer: Renato Montes
#
# Copyright (c) 2019 Renato Montes
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#----------------------------------------------------------------------#
#------------------------------ PROGRAM -------------------------------#
#----------------------------------------------------------------------#

import random
import sys

#Program version.
VERSION = "1.0"

#Definition of accepted filter codes.
FILTER_CODES = {"b":{"base":2, "word":"binary", "func":lambda n:bin(n)[2:]},
               "o":{"base":8,  "word":"octal",  "func":lambda n:oct(n)[2:]},
               "d":{"base":10, "word":"decimal","func":lambda n:str(n)},
               "h":{"base":16, "word":"hexadecimal", "func":lambda n:hex(n)[2:]}}

#Default filter, shows all results.
ALL_CODES = FILTER_CODES.keys()

#Available commands to quit the program, as a tuple.
#The program can also be stopped with an EOF signal or a keyboard interrupt.
QUIT_COMMANDS = ("quit", "exit", "stop")

############################## FUNCTIONS ###############################

def interpret(input_line, bases):
    """Runs through a list of number strings.
    
    Args:
        input_line (str): user input containing numbers
        bases (set): bases to be shown"""
    for string in input_line.split():
        try:
            transform(string, bases)
        except ValueError:
            print("Entered number \"", string, "\" is invalid.", sep="")
        finally:
            print()

def transform(string, bases):
    """Displays a number string in other bases.

    Throws:
        ValueError: when a number cannot be converted

    Args:
        string (str): number to be converted
        bases (set): bases to be shown"""
    if string in QUIT_COMMANDS:
        sys.exit()
    #make a number without any suffix a decimal
    number = string if string[-1].isdigit() else string[:-1]
    number_code = 'd' if string[-1].isdigit() else string[-1]

    #convert numbers depending on suffix and the filter
    if number_code in ALL_CODES:
        number = int(number, FILTER_CODES[number_code]["base"])
        if len(bases) > 0:
            print(string)
        for base_code in bases:
            if base_code != number_code:
                print(FILTER_CODES[base_code]["word"].capitalize(), ": ",
                     FILTER_CODES[base_code]["func"](number), sep="")


def get_filter():
    """Validates and interprets the filter argument.

    Return:
        (set): filter codes to use, each as an str"""
    if len(sys.argv) == 1:
        return ALL_CODES
    elif len(sys.argv) == 2:
        shown = set()
        for letter in sys.argv[1]:
            if letter in ALL_CODES:
                shown.add(letter)
            else:
                print("Filter is invalid.")
                show_accepted_filter_codes()
                sys.exit()
        return shown
    else:
        print("Too many arguments.")
        print("Usage: baseconv.py [FILTER]")
        sys.exit()

def show_accepted_filter_codes():
    """Display a list of all accepted filter codes."""
    accepted = list(ALL_CODES)
    accepted.sort()
    print("Accepted filter codes:")
    for code in accepted:
        print(" ", code, "-", FILTER_CODES[code]["word"])
    if len(accepted) > 2: #if filter codes are not deleted
        choice = random.randrange(0, len(accepted))
        code1 = accepted.pop(choice)
        choice = random.randrange(0, len(accepted))
        code2 = accepted.pop(choice)
        print("Usage example:", sys.argv[0], code1 + code2)

def get_expanded_filter(arg):
    """Expands a filter into one string of full words.

    Args:
        arg (str): filter passed when calling the program,
                   used to retain the same code order

    Return:
        (str): expanded filter string

    Precondition:
        The parameter arg is a valid filter."""
    if len(arg) == 1:
        return FILTER_CODES[arg]["word"]

    words = []
    for letter in arg:
        words.append(FILTER_CODES[letter]["word"])

    expanded = FILTER_CODES[arg[0]]["word"]
    if len(arg) > 2:
        for letter in arg[1:-1]:
            expanded = ", ".join((expanded, FILTER_CODES[letter]["word"]))
    return " ".join((expanded, "and", FILTER_CODES[arg[-1]]["word"]))

def show_filter(arg):
    """Shows the filter used, if any is requested.

    Args:
        arg (str): filter passed when calling the program,
                   used to retain the same code order

    Precondition:
        The parameter arg is a valid filter."""
    if len(arg) < len(ALL_CODES):
        print("Using filter:", arg, "(only", end=" ")
        print(get_expanded_filter(arg), end="")
        print(")", end="\n\n")

def show_header():
    """Shows the header at the beginning of the program."""
    print("baseconv, version 1.")
    print("Copyright (c) 2019 Renato Montes, under Apache License 2.0.", end="\n\n")
    print("Enter numbers with a suffix, e.g. 2a98h 110101b 8916")
    print("for a hexadecimal, a binary and a decimal respectively.", end="\n\n")


def run(bases):
    """Runs the interactive converter.

    Args:
        bases (tuple): bases to be shown"""
    show_header()

    if len(bases) < len(ALL_CODES):
        show_filter(sys.argv[1]) #use sys.argv to retain original order

    while True:
        print("Enter a number:")
        try:
            line = input().strip()
        except EOFError:
            return
        if len(line) == 0:
            continue
        print()
        interpret(line, bases)   

############################# ENTRY POINT ##############################

if __name__ == '__main__':
    """Module entry point."""
    try:
        bases = get_filter()
        run(bases)
    except KeyboardInterrupt:
        print() #nicety for terminal line



