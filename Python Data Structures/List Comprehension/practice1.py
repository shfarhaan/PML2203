# a = [1, 3, 5, 7, 9, 11]
#
# # We want a list [2, 6, 10, 14, 18, 22]
# # that has the doubled value of elements in list a.
#
# # USING REGULAR FOR LOOP
# b = []
#
# for each_element in a:
#     b.append(each_element*2)
#
# print(b)
#
# # USING LIST COMPREHENSION
# c = [each_element * 2 for each_element in a]
#
# print(c)

# # USING REGULAR FOR LOOP
# ele = []
#
# for each_element in range(1,7):
#     ele.append(each_element ** 2)
#
# print(ele)
#
# # USING LIST COMPREHENSION
# ele2 = [each_elem ** 2 for each_elem in range(1,7)]
#
# print(ele2)

# [36, 25, 16, 9, 4, 1]

rev_lis = []
for el in range(6, 0, -1):
    rev_lis.append(el ** 2)

print(rev_lis)

rev_lis2 = [el1 ** 2 for el1 in range(6, 0, -1)]

print(rev_lis2)




