# <----------Without List Comprehension--------->

# list = ['aryan','shyam','gopal','radha']
# list1 = []
# for x in list:
#     list1.append(x)
# print(list1)

# <--------here let only word with letter h can present in list1 then-------->

# list = ['aryan','shyam','gopal','radha']
# list1 = []
# for x in list:
#     if 'h' in x:
#         list1.append(x)
# print(list1)


# <----------With list comprehension------------->

# list = ['aryan','shyam','gopal','radha']
# list1 = [x for x in list]
# print(list1)


# <--------here let only word with letter h can present in list1 then-------->

# list = ['aryan','shyam','gopal','radha']
# list1 = [x for x in list if 'h' in x]
# print(list1)


# <--------------condition----------->

# list = ['aryan','shyam','gopal','radha']
# list1 = [x for x in list if x!='aryan']
# print(list1)


#<-----------range----------->

# list = ['Narayan Narayan' for x in range(3)]
# print(list)


#  <-------Expression------->
# The expression is the current item in the iteration

# list = ['apple','ball','cat','dog']
# list1 = [x.upper() for x in list]
# print(list1)

#   <----------Expression------->

# list = ['apple','ball','cat','dog']
# list1 = [x.upper() if x!='apple' else 'Iphone' for x in list ]
# print(list1)