# 42. Write a Python program to find
# missing and additional values in two lists.

# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h

elements_in_list1 = int(input("Enter number of Elements in List 1: "))
lis1 = list(map(str, input("\nEnter the numbers : ")
                .strip().split()))[:elements_in_list1]

elements_in_list2 = int(input("Enter number of Elements in List2: "))
lis2 = list(map(str, input("\nEnter the numbers : ")
                .strip().split()))[:elements_in_list2]

print(f"\nList of Items in the list 1 - {lis1}\n"
      f"and List of Items in the list 2 - {lis2}\n")

uniq_lis1 = set(lis1)
uniq_lis2 = set(lis2)

print(f"Missing values in second list: {uniq_lis1 - uniq_lis2}")
print(f"Additional values in second list: {uniq_lis2 - uniq_lis1}")

