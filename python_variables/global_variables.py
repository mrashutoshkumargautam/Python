# Example of using global variables in Python

# Part 1: Using a Global Variable
x = "awesome"

def myfunc():
    # Uses the global variable 'x'
    print("Python is :" + x)

myfunc()

print("=======================================================")

# Part 2: Shadowing a Global Variable Locally
a = "awesome"

def urfunc():
    # Local variable 'a' shadows the global 'a' within this function
    a = "fantastic"
    print("Python is " + a)

urfunc()

# Global 'a' remains unchanged outside the function
print("Python is " + a)

print("=======================================================")

# Part 3: Using the 'global' Keyword to Modify a Global Variable
abc = "awesome"

def wowfunc():
    global abc
    # Modify the global variable 'abc' within this function
    abc = "fantastic"

wowfunc()

# The global variable 'abc' is now changed to 'fantastic'
print("Python is: " + abc)
