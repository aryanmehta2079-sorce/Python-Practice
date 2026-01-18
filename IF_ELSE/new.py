#   <--------Python Conditions and If statements----->

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b




#   <--------If statement:----->

# a = 33
# b = 200
# if b > a:
#   print("b is greater than a")




#   <--------Indentation----->

# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

# a = 33
# b = 200
# if b > a:
# print("b is greater than a") # you will get an error



#   <--------Multiple Statements in If Block----->

# age = 20
# if age >= 18:
#   print("You are an adult")
#   print("You can vote")
#   print("You have full legal rights")


#   <--------Using Variables in Conditions----->

# is_Goal = True
# if is_Goal:
#   print("Yes")

# else:
#   print("No")



#   <--------The Else Keyword----->

# a = 1
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")



#   <--------Short Hand If ... Else----->

# a = 2
# b = 330
# print("A") if a > b else print("B")



#   <--------Multiple Conditions on One Line----->

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")