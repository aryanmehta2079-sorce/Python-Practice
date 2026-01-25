# <--------Basic Decorator-------->

# def changecase(func):
#   def rapper():
#      return func().upper()
#   return rapper
# @changecase
# def myfunction():
#   return "Hello Sally"
# print(myfunction())


# <--------Basic Decorator-------->

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# print(myfunction())



# <--------Multiple Decorator Calls-------->

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# @changecase
# def otherfunction():
#   return "I am speed!"

# print(myfunction())
# print(otherfunction())


# <--------Functions with arguments can also be decorated:-------->


# def changecase(func):
#   def myinner(x):
#     return func(x).upper()
#   return myinner

# @changecase
# def myfunction(nam):
#   return "Hello " + nam

# print(myfunction("Aryan"))



# <--------One decorator for upper case, and one for adding a greeting:-------->

def changecase(func):
    def rapper():
        return func().upper()
    return rapper

def greeting(func):
    def wrap():
        return "Hello "+func()+" Have a good day"
    return wrap

@changecase
@greeting
def my_function():
    return "Aryan"

print(my_function())





