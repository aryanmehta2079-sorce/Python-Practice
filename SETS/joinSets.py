# <--------Union--------->

# The union() method returns a new set with all items from both sets.

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

# You can use the | operator instead of the union() method, and you will get the same result.
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1 | set2
# print(set3)


# <--------Join Multiple Sets--------->

# Join multiple sets with the union() method:

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# # set5 = set1.union(set2,set3,set4)

# set5 = set1 | set2 | set3 | set4
# print(set5)




# <--------Update--------->

# The update() method inserts the items in set2 into set1:

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)


# <--------Intersection--------->

# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2)
set3 = set1 & set2
print(set3)



