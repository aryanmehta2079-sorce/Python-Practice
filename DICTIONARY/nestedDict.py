# <-----Nested Dictionaries---->

# myfamily = {
#     'father' : {
#         'Occupation' : 'Farmer',
#         'Age' : 57
#     },
#     'mother' : {
#         'Occupation' :'Teacher',
#         'Age' : 55
#     },
#     'brother' : {
#         'Occupation' : 'Student',
#         'Age' : 20
#     }
# }
# for x,y in myfamily.items():
#     print(x,y)

# <-----Nested Dictionaries - three to one ---->


# father = {
#     'Occupation' : 'Farmer',
#     'Age' : 57
# }
# mother = {
#     'Occupation' :'Teacher',
#     'Age' : 55
# }
# brother = {
#     'Occupation' : 'Student',
#     'Age' : 20
# }

# myfamily = {
#     'child1' : father,
#     'child2' : mother,
#     'child3' : brother
# }

# for x,y in myfamily.items():
#     print(x,y)


# <-----Access Items in Nested Dictionaries------>

# myfamily = {
#     'father' : {
#         'Occupation' : 'Farmer',
#         'Age' : 57
#     },
#     'mother' : {
#         'Occupation' :'Teacher',
#         'Age' : 55
#     },
#     'brother' : {
#         'Occupation' : 'Student',
#         'Age' : 20
#     }
# }

# print(myfamily['father']['Occupation'])


# <-----Access Items in Nested Dictionaries------>

# myfamily = {
#     'father' : {
#         'Occupation' : 'Farmer',
#         'Age' : 57
#     },
#     'mother' : {
#         'Occupation' :'Teacher',
#         'Age' : 55
#     },
#     'brother' : {
#         'Occupation' : 'Student',
#         'Age' : 20
#     }
# }

# for x,obj in myfamily.items():
#     print(x)
#     for y in obj:
#         print(y+":"+obj[y])


# <-----Set default or access------>
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.setdefault("model", "Bronco")
# print(x)




