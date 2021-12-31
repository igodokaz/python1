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

def plus(a, b):
    print(a + b)

def minus(a, b = 0):
    print(a - b)

plus(2,5)
minus(2)

def say_hello(name="anonymous"):
    print("hello", name)

say_hello()
say_hello("nico")