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

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# # set3 = set1.intersection(set2)
# set3 = set1 & set2
# print(set3)


# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

# set1 = {"apple", "banana", "cherry"}
# set2 = {1,2,'apple'}

# set3 = set1.intersection(set2)

# print(set3)



# <--------Intersection Update--------->

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.intersection_update(set2)

# print(set1)


# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}

# set3 = set1.intersection(set2)

# print(set3)



# <--------Difference--------->

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)
# # set3 = set1.difference(set2)
# set3 = set1 - set2
# print(set3)
# # print(set1)



# <--------Symmetric Differences--------->

# Keep the items that are not present in both sets: keep means unique items of both sets 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# set3 = set1.symmetric_difference(set2)
# set1.symmetric_difference_update(set2)
set3 = set1 ^ set2
# print(set1)
print(set3)

