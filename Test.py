def loop_info():
    print("\n--- INFORMATION ABOUT LOOPS ---")
    print("Loops repeat actions many times automatically.")
    print("\nFOR LOOP → repeats a fixed number of times.")
    print("Example: for i in range(5): print(i)")
    print("\nWHILE LOOP → repeats while a condition is true.")
    print("Example: while x < 10: x += 1")

def loop_run():
    print("\n--- LOOP EXAMPLES ---")

    print("\nFOR LOOP: counting 1 to 5")
    for i in range(1, 6):
        print(i)

    print("\nWHILE LOOP: counting down from 5")
    x = 5
    while x > 0:
        print(x)
        x -= 1
