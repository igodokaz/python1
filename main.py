# day = "Mon,Tue,Wed,Thu"

# print(day)

# # Mutable Sequence

# days = ["Mon","Tue","Wed","Thu","Fri"]

# print(type(days)) # List
# print("Mon" in days)
# print("Man" in days)
# print(days[3])
# print(len(days))
# print(days)
# # https://docs.python.org/3/library/stdtypes.html#typesseq-mutable
# days.append("Sat")
# days.reverse()
# print(days)


# # Immutable Sequence

# days = ("Mon","Tue","Wed","Thu","Fri")
# print(type(days)) # Tuples

# nico = {
#     "name" : "nico",
#     "age" : 29,
#     "korean" : True,
#     "fav_food" : ["Kimchi", "Sashimi"]
# } # Dictionary

# print(type(nico))
# print(nico)
# nico["handsome"] = True
# print(nico)


# https://docs.python.org/3/library/functions.html # Built in Functions


# age = "18"
# print(type(age))
# n_age = int(age)
# print(type(n_age))
# print(n_age)

# Define Function

# def say_hello():
#     print("hello")
#     print("bye")

# say_hello()
# say_hello()
# say_hello()

# def say_hello(who): # Function Arguments
#     print("hello", who)

# say_hello("Nicolas")

# https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

# def plus(a, b):
#     print(a + b)

# def minus(a, b = 0):
#     print(a - b)

# plus(2,5)
# minus(2)

# def say_hello(name="anonymous"):
#     print("hello", name)

# say_hello()
# say_hello("nico")


# Returns

# def p_plus(a,b):
#     print(a+b)

# def r_plus(a,b):
#     return a+b

# p_result = p_plus(2,3)
# r_result = r_plus(2,3)

# print(p_result, r_result)

# Keyworded Arguments

# def say_hello(name, age):
#     # return f"hello {name} you are {age} years old"
#     return "hello " + name + " you are " + age + " years old"

# # hello = say_hello("nico", "12")
# hello = say_hello(age = "12", name ="nico")
# print(hello)

# def say_hello(name, age, are_from, fav_food):
#     return f"hello {name} you are {age}. you are from {are_from} you like {fav_food}"

# # hello = say_hello("nico", "12")
# hello = say_hello(name="nico", age="12",fav_food="kimchi",are_from="korea")
# print(hello)

# Conditional part one

# def plus(a,b):
#     if type(b) is int or type(b) is float:
#         return a+b
#     else:
#         return None

# print(plus(12, 1.2))

# def age_check(age):
#     print(f"you are {age}")
#     if age < 18:
#         print("you cant drink")
#     elif age == 18:
#         print("you are now to this!")
#     elif age > 20 and age < 25:
#         print("you are still kind of young")
#     else:
#         print("enjoy your drink")


# age_check(23)

# For loop

# for day in [1,2,3,4,5]:
#     print(day)

# days = ("Mon", "Tue", "Wed", "Thu", "Fri")

# for day in days: # day는 작업이 시작되면 생김
#     if day is "Wed":
#         break
#     else:
#         print(day)

# for letter in "nicolas":
#     print(letter)

# Moduls

# https://docs.python.org/3/library/math.html

# import math

# print(math.ceil(1.2))
# print(math.fabs(-1.2))

from math import ceil, fsum as sexy_sum

print(ceil(1.2))
print(sexy_sum([1,2,3,4,5,6,7]))

from calculator import plus, minus

print(plus(1,2), minus(1,2), True, "lalalal", True, "lalalal")
