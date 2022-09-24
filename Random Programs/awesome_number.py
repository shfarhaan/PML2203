# Write a python program that will take a number
# as an input and check whether the number is Awesome or not.
# If the number is Awesome, it prints True. Otherwise, False.

# Awesome number: a number where every digit is less than
# its immediate left digit is called an Awesome number. A single-digit number
# cannot be an awesome number (e.g. 5421 is an Awesome number.)


# def awesome_number(number):
input_number = input("Input a number of your choice to \n"
                     "check if the number is awesome or not... \n\t\t")

number_in_a_list = [int(index) for index in str(input_number)]

print(number_in_a_list)
print(number_in_a_list[-1])
print(number_in_a_list[0:-1])
for i in number_in_a_list:

    if list(number_in_a_list[:-1]) < number_in_a_list:
        print("Awesome Number")
    else:
        print("Not an Awesome Number!")
