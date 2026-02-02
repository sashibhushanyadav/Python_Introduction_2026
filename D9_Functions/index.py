import next
# Built-in Functions
# Such as print(), input(), int() and so on.

# Module function
import math as m

r = 2
areaOfCircle = 2 * m.pi * r
print(m.sqrt(9))
print(areaOfCircle)


# Self-define function
def sum(a, b):
    return a + b

print(sum(4, 5))

# import function
print(next.function(4, 5))

# Recursion concept
def num(n):
    if n == 0:
        return 1
    else:
        return n * num(n-1)

print(num(5))