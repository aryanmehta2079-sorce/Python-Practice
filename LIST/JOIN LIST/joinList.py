# <---------Join Two Lists-------->

# list1 = ['apple','ball','cat','dog']
# list2 = [1,2,3,4,5]
# list3 = list1+list2
# print(list3)

# <----------Append list1 into list2:---------->

# list1 = ['apple','ball','cat','dog']
# list2 = [1,2,3,4,5]
# for x in list1:
#     list2.append(x)
# print(list2)


# <----------extend list2---------->

list1 = ['apple','ball','cat','dog']
list2 = [1,2,3,4,5,5]
list2.extend(list1)
# print(list2)
print(list2.count(5))