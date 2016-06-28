#!/user/bin/python3
#^.^ coding=utf-8 ^.^#

from HelloWorld import cute_split_line
from functools import reduce
from random import randint
# 1. map
# 2. reduce
# 3. filter
# 4. sorted

FLAG = "_ID"

#********** map **********#

def Add_Flag(n):
    return "{}{}".format(FLAG, n)

result = map(Add_Flag, range(10))

print("result type:", type(result))
print("result:", list(result))

cute_split_line()

#********** reduce **********#

def multi(m, n):
    return m * n

result = reduce(multi, range(1,10))
print("result type:", type(result))
print("result:", result)

cute_split_line()

#********** filter **********#
def is_odd(n):
    return n%2

result = filter(is_odd, range(10))
print("result type:", type(result))
print("result:", list(result))

cute_split_line()

#********** sorted **********#
unorder_list = [randint(1, 100) for i in range(10)]
print("unorder list:", unorder_list)
print("ordered list:", sorted(unorder_list))
print("reverse ordered list:", sorted(unorder_list, reverse=True))
print("reverse ordered list:", sorted(unorder_list, key = str, reverse=True))