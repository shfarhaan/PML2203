# 14. Write a Python program to print
# the numbers of a specified list after
# removing even numbers from it.

inputs = int(input("Please enter how many elements "
                   "you want to insert in the list: \n\t\t"))

specified_list = []
for each_input in range(1, inputs + 1):
    num = int(input(f"The no.{each_input} in your specified list is: "))
    specified_list.append(num)
    if num % 2 == 0:
        specified_list.remove(num)

print(f"The specified list without any even numbers is: {specified_list}")
