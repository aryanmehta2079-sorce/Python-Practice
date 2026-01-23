# <---------Arbitrary Arguments - *args---------->

# If you do not know how many arguments will be passed into your function, add a * before the parameter name.
# This way, the function will receive a tuple of arguments and can access the items accordingly:

# def fun(*args):
#     for x in args:
#         print(x)

# fun(3,1,3,43,53,23,31,3,1,5,7)


# <---------Accessing individual arguments from *args:---------->

# def my_function(*args):
#   print("Type:", type(args))
#   print("First argument:", args[0])
#   print("Second argument:", args[1])
#   print("All arguments:", args)

# my_function("Ram", "Sita", "Hari")


# <---------Using *args with Regular Arguments---------->

# def fun(name,*names):
#     for x in names:
#         print(x)

# fun('Ram','Sita','Hari','Krishna','Shyam','Sundar','Radha') 



# <---------Finding the maximum value:---------->

def maximum(*num):
    if len(num)==0: return None
    else:
        max = num[0]
        for x in num:
            if x>max:
             max = x
        return max

print(maximum(1,6,2,5,2,7,8,98,3,1))

