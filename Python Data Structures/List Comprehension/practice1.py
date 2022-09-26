a = [1, 3, 5, 7, 9, 11]

# We want a list [2, 6, 10, 14, 18, 22]
# that has the doubled value of elements in list a.

# USING REGULAR FOR LOOP
b = []

for each_element in a:
    b.append(each_element*2)

print(b)

# USING LIST COMPREHENSION
c = [each_element * 2 for each_element in a]

print(c)
#