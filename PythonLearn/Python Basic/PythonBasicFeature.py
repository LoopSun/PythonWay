#!/user/bin/python3
#^.^ coding=utf-8 ^.^#
from HelloWorld import cute_split_line
# 1. slice
# 2. iter
# 3. list comprehensions
# 4. generator
# 5. iterator


#********** slice **********#

sample_list = list(range(10))
print("raw list:", sample_list)
print("sample_list[:5]:", sample_list[:5])
print("sample_list[2:5]:", sample_list[2:5])
print("sample_list[-1]:", sample_list[-1])
print("sample_list[-5:]:", sample_list[-5:])
print("sample_list[-5:-1]:", sample_list[-5:-1])
print("sample_list[1:10:2]:", sample_list[1:10:2])
print("sample_list[::-1]:", sample_list[::-1])

# tuple is same
cute_split_line()

#********** iter **********#

for index, value in enumerate(sample_list):
    print(index, value)

cute_split_line()

#********** list comprehensions **********#

coordinate = [(x, y, z) for x in range(5) for y in range(5) for z in range(5)]
print("coordinate type:", type(coordinate))
cute_split_line()

#********** generator **********#

coordinate = ((x, y, z) for x in range(5) for y in range(5) for z in range(5))
print("coordinate type:", type(coordinate))  # more grace


def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b
    return "..."

print("fib type:", type(fib))
f = fib(10)
print("f type:", type(f))
print("generator bulit-in function")
generator_funcs = [print("{}.{}()".format(" "*2,func)) for func in dir(f) if not func.startswith('_')]

cute_split_line()

#********** iterator & iterable **********#


# iterator: list comprehensions or include yield function
# iterable: could be call by for.