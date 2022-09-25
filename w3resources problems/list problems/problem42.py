# 42. Write a Python program to find
# missing and additional values in two lists.
#
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h

no_of_list = int(input("How many list do you want to check? "))

for i in range(1, no_of_list+1):
    elements_in_list = int(input("Enter number of Elements: "))
    list_of_elements = list(map(int, input("\nEnter the numbers : ").strip().split()))[:no_of_list]
    print("\n List of Items in the list")