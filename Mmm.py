def LoopInfo():
    print("\n--- INFORMATION ABOUT THE NESTED LOOP CODE ---")
    print("\nThis code prints a star pattern using three nested loops:")
    print("1. The first loop prints spaces")
    print("2. The second loop prints stars on the left side")
    print("3. The third loop prints stars on the right side")
    print("\nThe loops look like this:")
    print("for uma in range(1,11,1):")
    print("    for deez in range(10, uma, -1):")
    print("        print(' ', end=' ')")
    print("    for y in range(1, uma, 1):")
    print("        print('*', end=' ')")
    print("    for y in range(1, uma, 1):")
    print("        print('*', end=' ')")
    print("    print()")
    input("\nPress any key to go back...")


def LoopRun():
    print("\n--- RUNNING THE NESTED LOOP STAR PATTERN ---\n")

    for uma in range(1, 11, 1):
        for deez in range(10, uma, -1):
            print(" ", end=" ")
        for y in range(1, uma, 1):
            print("*", end=" ")
        for y in range(1, uma, 1):
            print("*", end=" ")
        print()

    input("\nPress any key to go back...")


def choice(LoopRun, LoopInfo):
    import os
    os.system('cls')  # Use 'clear' on Linux/Mac

    print("What do you wanna know?")
    print("1 --- INFORMATION ABOUT THE NESTED LOOP")
    print("2 --- RUN THE CODE")

    tachyon = input("Enter Your Choice: ")

    if tachyon == '1':
        LoopInfo()

    elif tachyon == '2':
        LoopRun()

    else:
        print("Invalid selection")
        input("Press any key to go back...")


# Start the program
choice(LoopRun, LoopInfo)


def ForLoopInfo():
    print("\n--- FULL INFORMATION ABOUT THIS FOR LOOP PATTERN ---")

    print("\nThis pattern uses TWO loops:")
    print("1. The OUTER loop controls how many lines (rows) are printed.")
    print("   -> It goes from 1 to 10, increasing each row.")
    print("2. The INNER loop prints stars based on the current row number.")
    print("   -> It starts at the current row value (uma)")
    print("   -> It prints stars until 10 is reached.\n")

    print("This means:")
    print("- The first line prints 9 stars")
    print("- The second line prints 8 stars")
    print("- The third line prints 7 stars")
    print("- And so on…")
    print("- The last line prints 0 stars (just a blank line)")

    print("\nHere is the exact code being used:")
    print("for uma in range(1, 11, 1):")
    print("    for deez in range(uma, 10, 1):")
    print("        print('*', end=' ')")
    print("    print()")

    print("\nThis creates a REVERSE triangle pattern that shrinks every line.")
    input("\nPress any key to go back...")


def ForLoopRun():
    print("\n--- RUNNING THE FOR LOOP STAR PATTERN ---\n")

    for uma in range(1, 11, 1):
        for deez in range(uma, 10, 1):
            print("*", end=" ")
        print()

    input("\nPress any key to go back...")


def choice(ForLoopRun, ForLoopInfo):
    import os
    os.system('cls')  # Use 'clear' if on Mac/Linux

    print("What do you wanna know?")
    print("1 --- INFORMATION ABOUT THIS FOR LOOP")
    print("2 --- RUN THE FOR LOOP CODE")

    tachyon = input("Enter Your Choice: ")

    if tachyon == '1':
        ForLoopInfo()

    elif tachyon == '2':
        ForLoopRun()

    else:
        print("\nInvalid selection")
        input("Press any key to go back...")


# Start program by calling the choice menu
choice(ForLoopRun, ForLoopInfo)
nested for loop

A nested for loop means a for loop inside another for loop.

The OUTER loop runs first and controls the number of times the INNER loop runs.

For every single one round of the outer loop,
the inner loop runs completely from start to finish.

This allows us to create patterns such as:
- Triangles
- Squares
- Pyramids
- Repeated shapes
- Grids or tables

Nested loops work like a clock:
- The outer loop is the hour hand (moves slower)
- The inner loop is the minute hand (moves faster)

Example structure:

for i in range(...):
    for j in range(...):
        # this runs MANY times

In this program, the nested for loop is used to print stars (*)
in a pattern that changes every row.


def ForLoopInfo():
    print("\n--- INFORMATION ABOUT FOR LOOPS ---")

    print("\nA for loop is a control structure that repeats code a specific number of times.")
    print("It goes through a sequence of numbers using the range() function.")
    print("\nrange(start, stop, step) tells the loop:")
    print("- Where to start")
    print("- Where to stop")
    print("- How much to increase by")

    print("\nExample:")
    print("for i in range(1, 6):")
    print("    print(i)")
    print("This prints: 1 2 3 4 5")

    print("\nFor loops are used for:")
    print("- Printing patterns")
    print("- Repeating actions")
    print("- Counting")
    print("- Iterating through lists")
    print("- Automating repetitive tasks")

    print("\nIn this program, the for loop controls how many stars are printed on each row.")

    input("\nPress any key to go back...")
