import os

def Listinfo():
    print("\nThe List Function Allows us to store multiple items in a single variable.")
    print("\n-----> list() <----- is used to create a list.")
    print("\n--- INFORMATION ABOUT LIST FUNCTION ---")
    print("A list is a collection which is ordered and changeable. It allows duplicate members.")
    print("Example: months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul']")
    print("\nWe can use various list methods such as:")
    print("- reverse() to reverse the order of items.")
    print("- sort() to sort the list in ascending order.")
    print("Example:")
    print("months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul']")
    print("months.reverse() # Reverses the list.")
    print("months.sort() # Sorts the list alphabetically.")
    input("\nPress any key to go back")

def ListRun():
    print("\n--- Running Code Example for List Function ---")

    # List of months
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul']
    print("Original List:", months)

    # Reversing the list
    months.reverse()
    print("After Reversing:", months)

    # Converting a string into a list
    fullname = 'kurt dashiel pacaigue'
    newlist = list(fullname)  # Converts string into a list of characters
    print("List from String:", newlist)

    # Reversing the list of characters
    newlist.reverse()
    print("Reversed List of Characters:", newlist)

    # Sorting the list of characters
    newlist.sort()
    print("Sorted List of Characters:", newlist)

    input("\nPress any key to go back")

def choice(ListRun, Listinfo):
    os.system('cls')  # Clears the screen (on Windows)
    print("What do you want to know?")
    print("1 --- INFORMATION ABOUT LIST FUNCTION")
    print("2 --- RUN THE LIST CODE")
    
    tachyon = input("Enter Your Choice: ")

    if tachyon == '1':
        Listinfo()
    elif tachyon == '2':
        ListRun()
    else:
        print("Invalid selection")

# Running the program
choice(ListRun, Listinfo)

import os

def LoopInfo():
    print("\n--- INFORMATION ABOUT NESTED FOR LOOPS ---\n")
    print("A nested loop means a loop inside another loop.")
    print("The inner loop finishes all its iterations for every one iteration of the outer loop.\n")

    print("Example structure:")
    print("for i in range(5):")
    print("    for j in range(3):")
    print("        print(i, j)")
    print("\nYour code uses THREE nested loops to print a pyramid-like pattern.\n")

    print("Explanation of your code:")
    print("- The first loop increases uma from 1 to 10.")
    print("- The second loop prints spaces before the stars.")
    print("- The third and fourth loops print stars on each side, forming symmetry.")
    print("- print() creates a new line after each row.\n")

    input("Press any key to go back...")


def LoopRun():
    print("\n--- RUNNING NESTED FOR LOOP CODE ---\n")

    print("\t\t *", end="")   # Your first line

    for uma in range(1, 11, 1):

        # Prints spaces decreasing each row
        for deez in range(10, uma, -1):
            print(" ", end=" ")

        # Left side stars
        for y in range(1, uma, 1):
            print("*", end=" ")

        # Right side stars
        for z in range(1, uma, 1):
            print("*", end=" ")

        print()  # New line
    
    input("\nPress any key to go back...")


def choice(LoopRun, LoopInfo):
    os.system('cls')  # Windows clear screen
    print("What do you want to do?")
    print("1 --- INFORMATION ABOUT NESTED FOR LOOP")
    print("2 --- RUN THE NESTED LOOP CODE")

    tachyon = input("Enter Your Choice: ")

    if tachyon == '1':
        LoopInfo()
    elif tachyon == '2':
        LoopRun()
    else:
        print("Invalid selection")


# Run the program
choice(LoopRun, LoopInfo)


import os
import random

def WhileInfo():
    print("\n--- INFORMATION ABOUT WHILE TRUE LOOP ---\n")
    print("A while True loop runs forever until something stops it.")
    print("This 'something' is usually a BREAK statement.\n")

    print("Example:")
    print("while True:")
    print("    user = input('Enter something: ')")
    print("    if user == 'stop':")
    print("        break")
    print("\nIn your code:")
    print("- 'while c == True:' keeps looping until the player guesses the number.")
    print("- If the guess is correct, 'break' stops the loop.")
    print("- The loop counts how many tries the player used.\n")

    input("Press any key to go back...")


def WhileRun():
    print("\n--- RUNNING WHILE TRUE FUNCTION CODE ---\n")

    print("TRY YOUR LUCK")
    print("________________")

    a = random.randint(1, 10)
    b = 0
    c = True

    e = input("Enter Your Name--> ")

    while c == True:
        d = eval(input("Enter a number 1–10 ---> "))
        b += 1
        if d == a:
            print("Winner")
            break
        else:
            print("Choose Again")

    print(f"Hi {e}, Your Tries is {b}")

    input("\nPress any key to go back...")


def choice(WhileRun, WhileInfo):
    os.system('cls')
    print("What do you want to do?")
    print("1 --- INFORMATION ABOUT WHILE TRUE FUNCTION")
    print("2 --- RUN THE WHILE TRUE CODE")

    tachyon = input("Enter Your Choice: ")

    if tachyon == '1':
        WhileInfo()
    elif tachyon == '2':
        WhileRun()
    else:
        print("Invalid selection")


# Run the program
choice(WhileRun, WhileInfo)


import os

def DictionaryInfo():
    print("\n--- INFORMATION ABOUT DICTIONARIES ---\n")
    print("A dictionary in Python is a collection of data stored in KEY : VALUE pairs.")
    print("Unlike lists, dictionaries are unordered and you access items using keys instead of indices.")
    print("\nKey Points:")
    print("1. Dictionaries use curly braces {} to store items.")
    print("2. Each item is a pair: key : value.")
    print("3. Keys must be unique, but values can repeat.")
    print("4. You can change, add, or remove items in a dictionary.")
    print("5. Access values by using their key, not by position.")
    
    print("\nExample from your code:")
    print("TheD = {")
    print("   'SOLAR' : 'SOL',")
    print("   'DEFEATED' : 'CIRLCES',")
    print("   'RGB' : 'RB',")
    print("   'DR' : 'DREAM',")
    print("   'NM' : 'NIGHTMARE'")
    print("}")
    print("\nAccess a value using a key:")
    print("print(TheD['SOLAR'])  # Output: SOL")
    
    print("\nOther useful dictionary operations:")
    print("- Add new item: TheD['NEWKEY'] = 'NewValue'")
    print("- Change value: TheD['SOLAR'] = 'NEWVAL'")
    print("- Remove item: del TheD['DEFEATED']")
    print("- Check if key exists: 'SOLAR' in TheD  # returns True or False\n")
    
    input("Press any key to go back...")


def DictionaryRun():
    print("\n--- RUNNING CODE EXAMPLE FOR DICTIONARY ---\n")

    # List example
    TheList = ['RB', 'NM', 'DREAM', 'SOLAR', 'CIRCLES', 'BB', 'DONE']
    print("Example List:", TheList)
    print("Accessing the 6th item in the list (index 5):", TheList[5])  # BB

    # Dictionary example
    TheD = {
        'SOLAR' : 'SOL',
        'DEFEATED' : 'CIRLCES',
        'RGB' : 'RB',
        'DR' : 'DREAM',
        'NM' : 'NIGHTMARE'
    }
    print("\nDictionary Example:", TheD)
    print("Accessing the value of 'SOLAR':", TheD['SOLAR'])  # SOL

    input("\nPress any key to go back...")


def choice(DictionaryRun, DictionaryInfo):
    os.system('cls')  # Clears the screen
    print("What do you want to do?")
    print("1 --- INFORMATION ABOUT DICTIONARY FUNCTION")
    print("2 --- RUN THE DICTIONARY CODE")

    tachyon = input("Enter Your Choice: ")

    if tachyon == '1':
        DictionaryInfo()
    elif tachyon == '2':
        DictionaryRun()
    else:
        print("Invalid selection")


import os
# Assuming activity23_1.py exists in the same directory
from activity23_1 import GreetWithName, FunctionWithReturn, Greetperson, Factorial

def FunctionInfo():
    print("\n--- INFORMATION ABOUT FUNCTIONS IN PYTHON ---\n")
    print("In Python, functions are defined using the 'def' keyword.")
    print("Functions allow you to group code together and reuse it multiple times.\n")

    print("Key points about functions:")
    print("1. Use 'def function_name(parameters):' to define a function.")
    print("2. Functions can take inputs (parameters) and optionally return a value.")
    print("3. Call a function using its name and parentheses: function_name(args)")
    print("4. Using functions helps organize code and avoid repetition.\n")

    print("Example from your code:")
    print("def Function():")
    print("    print('umamusume')")
    print("    print('agnes tachyon')")
    print("    print('4 time world champion')")
    print("Function()  # calls the function\n")

    print("Other examples in your code:")
    print("- GreetWithName('lerbon')  # calls function with one parameter")
    print("- FunctionWithReturn(9)  # returns a value")
    print("- Factorial(6)  # returns factorial of 6\n")

    input("Press any key to go back...")


def FunctionRun():
    print("\n--- RUNNING FUNCTION EXAMPLES ---\n")

    # Your own defined function
    def Function():
        print("umamusume")
        print("agnes tachyon")
        print("4 time world champion")

    Function()  # call the function

    # Imported functions from activity23_1
    GreetWithName('lerbon')
    Greetperson('agnes', 'kyoto', '67')

    print(f"\nI want to get the summation of {FunctionWithReturn(9)}")
    print(f"I want to get the summation of {FunctionWithReturn(11) + 25}")
    print(f"I want to get the summation of {Factorial(6)}")

    input("\nPress any key to go back...")


def choice(FunctionRun, FunctionInfo):
    os.system('cls')
    print("What do you want to do?")
    print("1 --- INFORMATION ABOUT FUNCTIONS (def)")
    print("2 --- RUN THE FUNCTION CODE")

    tachyon = input("Enter Your Choice: ")

    if tachyon == '1':
        FunctionInfo()
    elif tachyon == '2':
        FunctionRun()
    else:
        print("Invalid selection")


# Run the program
choice(FunctionRun, FunctionInfo)
