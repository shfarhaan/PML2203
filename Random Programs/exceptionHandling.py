try:
    # Runs First
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))

    print("This is the Try Block before results..\n")
    results = numerator / denominator
    print("This is the Try Block after results...\n")
    print(results)

except ZeroDivisionError as obj:
    # Runs if exception occurs in try block
    # print("You can not Divide a number by Zero.")
    print("This is the ZeroDivisionError Block\n")
    print(obj)

except ValueError as obj:
    # Runs if exception occurs in try block
    # print("Please enter a value.")
    print("This is the ValueError Block\n")
    print(obj)
#
# else:
#     # Runs if try block *Succeeds*
#     print(results)
#     print("This is the else Block\n")

# finally:
#     # This code *always* run
#     pass
