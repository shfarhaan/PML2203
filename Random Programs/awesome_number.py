# Write a python program that will take a number
# as an input and check whether the number is Awesome or not.
# If the number is Awesome, it prints True. Otherwise, False.

# Awesome number: a number where every digit is less than
# its immediate left digit is called an Awesome number. A single-digit number
# cannot be an awesome number (e.g. 5421 is an Awesome number.)

input_number = input("Input a number of your choice to \n"
                     "check if the number is awesome or not... \n\t\t")

num_list = [int(digit) for digit in input_number]

for i in num_list:
    if num_list[:-1] < num_list[0:]:
        i += 1
        print(i)


#
# print(type(num_list))


# number_in_a_list = [int(index) for index in str(input_number)]
# num_to_string =
#
#
# if check(number_in_a_list, ):
#     print("Awesome Number")
# else:
#     print("Not an Awesome Number")
