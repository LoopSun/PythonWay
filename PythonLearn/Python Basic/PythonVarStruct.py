#!/user/bin/python3
#^.^ coding=utf-8 ^.^#

from sys import getsizeof

#************* int *************#

int_type = 1
print("int: {}".format(int_type))
# show int belong class
print('int type:', type(int_type))
# check object's class
print('isinstance int class:',isinstance(int_type, int))
# show dynamic to malloc
print('int length:', getsizeof(int_type))
int_type = 100000000000000000000000000000
print('int length:', getsizeof(int_type))
print('*'*20)
#************* float *************#
float_type = 12.21
print("float: {}".format(float_type))
# show int belong class
print('float type:', type(float_type))
# check object's class
print('isinstance float class:',isinstance(float_type, float))
# show dynamic to malloc
print('float length:', getsizeof(float_type))
float_type = 100000000000000000000000000000.2345
print('float length:', getsizeof(float_type))
print('*'*20)

#************* char & string  *************#
string_type = "X"
print("string: {}".format(string_type))
# show string belong class
print('string type:', type(string_type))
# check object's class
print('isinstance string class:',isinstance(string_type, str))
# show dynamic to malloc
print('string length:', getsizeof(string_type))
string_type = "A Rabbit is not an rabbit."
print('string length:', getsizeof(string_type))

print('string \\n length:', getsizeof('\n'))
print('*'*20)

#************* boolean *************#
bool_type = True      # or False
print("bool: {}".format(bool_type))
# show string belong class
print('bool type:', type(bool_type))
# check object's class
print('isinstance bool class:',isinstance(bool_type, bool))
# show dynamic to malloc
print('bool length:', getsizeof(bool_type))
bool_type = False
print('bool length:', getsizeof(bool_type))
print('*'*20)

#************* None *************#
None_type = None      # or False
print("None: {}".format(None_type))
# show string belong class
print('None type:', type(None_type))
# show dynamic to malloc
print('None length:', getsizeof(None_type))

#************* var *************#

