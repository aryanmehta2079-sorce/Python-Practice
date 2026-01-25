# <---------Global Keyword---------->

# def myfunc():
#   global x
#   x = 300
# myfunc()
# print(x)

# x = 300
# def myfunc():
#   global x
#   x = 200
# myfunc()
# print(x)


# <---------Nonlocal Keyword---------->


def myfunc():
  x = 300
  def fun():
     nonlocal x
     x = 200
  fun()
  return x
print(myfunc())
