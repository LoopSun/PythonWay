#!/user/bin/python3
#^.^ coding=utf-8 ^.^#
from collections import OrderedDict

# 1. list
# 2. tuple
# 3. dict and ordered dict
# 4. set


#********* list *********#

list_sample = (element for element in range(101) if not element % 2)
list_sample_trans = list(list_sample)
print("list length:", len(list_sample_trans))
print("origin type:", type(list_sample))   # generator will reduce memory usage
print("transform type:", type(list_sample_trans))
print("list built-in functions")
list_funcs = [print("{}.{}()".format(" "*2,func)) for func in dir(list) if not func.startswith('_')]
print("*"*20)

#********* tuple *********#

tuple_sample = tuple(list_sample_trans)
print("tuple type:", type(tuple_sample))
print("tuple built-in functions")
tuple_funcs = [print("{}.{}()".format(" "*2,func)) for func in dir(tuple) if not func.startswith('_')]
try:
    tuple_sample[-1] = 0
except Exception as err:
    print("tuple[-1] = 0: ",err)
print("*"*20)

#********* dict *********#
keys = ("user{}".format(index) for index in range(100))
dict_sample = dict.fromkeys(keys, None)
print(dict_sample)
print("dict type:", type(dict_sample))
print("dict built-in functions")
dict_funcs = [print("{}.{}()".format(" "*2,func)) for func in dir(dict) if not func.startswith('_')]
print("*"*20)

    #********* ordered dict *********#
print("ordered dict built-in functions")
ordered_dict_funcs = [print("{}.{}()".format(" "*2,func)) for func in dir(OrderedDict) if not func.startswith('_')]
print("*"*20)

#********* set *********#

set_sample = {1,1,2,3,4,4,5}
print('set_sample:', set_sample)
print("set built-in functions")
set_funcs = [print("{}.{}()".format(" "*2,func)) for func in dir(set) if not func.startswith('_')]
print("*"*20)