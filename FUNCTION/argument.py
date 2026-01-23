# <---------Parameters vs Arguments---------->

# def fun(name): # name is the parameter
#     print("Hello " + name)
# fun("Narayan")  # Narayan is the argument


# <---------Parameters vs Arguments---------->

# def fun(first,last):
#     print(first+ " " + last)

# fun('Hello','Narayan')


# <---------Default Parameter Values---------->

# def fun(first,last = 'Narayan'):
#     print(first+" "+last)

# fun('Hello','Mata')



# <---------Mixing Positional and Keyword Arguments---------->

# def fun(animal,name,age):
#     print("I have a",animal, "whose name is",name,"and he is",age,"years old")
# fun('dog','seru',5)
# fun(name='seru',animal='dog',age=5)


# <---------Sending a list as an argument:---------->

# def fun(fruits):
#     for x in fruits:
#         print(x)

# fruit = ['apple','banana','cherry']
# fun(fruit)


# <---------Sending a dictionary as an argument:---------->


# def fun(fruits):
#     for x,y in fruits.items():
#         print(x+": "+y)


# def fun(fruits):
#     for x in fruits:
#         print(x+": "+fruits[x])
#         print(x,": ",fruits[x])


# fruit = {'apple':'green','banana':'yellow','cherry':'red'}
# print(type(fruit))
# fun(fruit)


# <---------A function that returns a tuple:---------->

# def fun():
#     return (10,20)

# x,y = fun()
# print(x)
# print(y)


# <---------Positional-Only Arguments---------->

# def fun(first,/):
#     print(first)

# fun('Hello')
# fun(first = 'Hello') # through an error



# <---------Keyword-Only Arguments---------->

# def fun(*,first):
#     print(first)

# fun(first = 'Hello') 
# fun('Hello') # through an error


# <---------Combining Positional-Only and Keyword-Only---------->

def fun(a,b,/,*,c,d):
    return a+b+c+d

print(fun(3,4,1,2))