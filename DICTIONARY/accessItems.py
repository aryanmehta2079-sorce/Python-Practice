# <------Get the value of the "model" key:----->

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict['model'])

######------Using get()----->

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # print(thisdict.get('model'))
# print(thisdict.keys())
# print(thisdict.values())



# <------Keys and Values----->

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()
# print(x)
# print(type(x))

# y = car.values()
# print(y)
# print(type(y))

# car['brand'] = 'Tata'
# x = car.values()
# print(x)

# car['color'] = 'green'
# x = car.values()
# x = car.items() #gives all items present
# print(x)


# <------Check if Key Exists----->


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

if 'brand'in car:
    print(car['brand'])