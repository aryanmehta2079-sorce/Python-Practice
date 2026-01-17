#  <----------Dictionary Basics---------->

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# thisdict = {
#     'brand' :'Ford',
#     'model' : 'Mustang',
#     'year' : 1964
# }
# print(thisdict)


#  <----------Dictionary Items---------->

# Duplicate values will overwrite existing values:

# thisdict = {
#     'brand' :'Ford',
#     'model' : 'Mustang',
#     'year' : 1964,
#     "year": 2020
# }
# print(thisdict['year'])


#  <----------Dictionary Length---------->

# thisdict = {
#     'brand' :'Ford',
#     'model' : 'Mustang',
#     'year' : 1964, #this is not counted because of duplicate 
#     "year": 2020
# }
# print(len(thisdict))


#  <----------Dictionary Items - Data Types---------->

# The values in dictionary items can be of any data type:

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(type(thisdict))


#  <----------The dict() Constructor---------->

# thisdict = dict(name = 'Aryan', roll = 23053464, section = 'cse-26')
# # print(thisdict['section'])
# print('A') if 'cow' in thisdict else print('B') if 'dog' in thisdict else print('C')

