#  <-------Sort List Alphanumerically--------->

# list = ["orange", "mango", "kiwi", "pineapple", "banana"]
# list.sort()
# print(list)


#  <-------Sort List numerically Ascending--------->
 
# list = [100, 50, 65, 82, 23]
# list.sort()
# print(list)

#  <-------Sort List Alphanumerically Descending--------->

# list = ["orange", "mango", "kiwi", "pineapple", "banana"]
# list.sort(reverse = True)
# print(list)


#  <-------Sort List numerically Ascending--------->
 
# list = [100, 50, 65, 82, 23]
# list.sort(reverse = True)
# print(list)


#   <-------Customize Sort Function---------->

# def fun(n):
#     return abs(n-50)

# list = [100, 50, 65, 82, 23]
# list.sort(key = fun)
# print(list)


#   <<----------Case sensitive Sort------------>

# list = ["orange", "Mango", "kiwi", "Pineapple", "banana"]
# list.sort()
# print(list) # first capital letters are printed in ascending then small letters




#   <<----------Case Insensitive Sort------------>

# list = ["orange", "Mango", "kiwi", "Pineapple", "banana"]
# list.sort(key = str.lower)
# print(list) 


#     <-----------Reverse Order--------->

list = ["orange", "Mango", "kiwi", "Pineapple", "banana"]
list.reverse()
print(list) 


