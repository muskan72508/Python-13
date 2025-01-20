# import math


# print(math.floor(4.23))


# from math import sqrt,floor

# print(sqrt(4))
# print(floor(2.3))


# Not Recommended
# Beacuse we are importing all function from module

# from math import *

# print(sqrt(4))
# print(floor(2.3))


# Using as in import

import math as m

print(m.sqrt(4))


# To see all the function present in module

print(dir(m))


# Importing from other files

import importHelper

print(importHelper.welcome())