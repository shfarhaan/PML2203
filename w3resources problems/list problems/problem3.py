# 3. Write a Python program to get the largest number from a list.

num_of_inputs = int(input("How many elements will be in the list?\n\t\t"))

input_list = []
for each_input in range(1, num_of_inputs+1):
    num = int(input(f"The no.{each_input} element in the list: "))
    input_list.append(num)

print(f'Your list contains {num_of_inputs} '
      f'number of elements and the list is {input_list}')

sorted_list = sorted(input_list)

print(f"The largest number in the given list is: {sorted_list[-1]}")
