# GLOBAL VARIABLE

x = "awesome"

def myfunc():
    print("python is :" + x)

myfunc()


print("=======================================================")

a = "awesome"

def urfunc():
  a = "fantastic"
  print("Python is " + a)

urfunc()

print("Python is " + a)

print("=======================================================")


# GLOBAL KEYWORD

abc  = "awesome"

def wowfunc():
   global abc
   abc = "fantastic"

wowfunc()

print("Python is: " + abc)