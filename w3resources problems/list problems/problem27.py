# 27. Write a Python program to find
# the second-smallest number in a list.

# list_of_fruits = ["Water Melon", "Pears", "Avocado", "Jackfruit", "Pomegranate"]
#
# list_of_numbers = [100, 34, 399, 10283, 3, 4, 10, -204, 10]
# sorted_list = sorted(list_of_numbers)
#
# print((sorted_list[1]))

num_of_inputs = int(input("How many elements will be in the list?\n\t\t"))

input_list = []
for each_input in range(1, num_of_inputs+1):
    num = int(input(f"The no.{each_input} element in the list: "))
    input_list.append(num)

unique_numbers = set(input_list)
sorted_list = sorted(unique_numbers)

print(f'Your list contains {num_of_inputs} '
      f'unique numbers and the list is {unique_numbers}')

# sorted_list = set(sorted(input_list))

print(f"The largest number in the given list is: {sorted_list[1]}")

