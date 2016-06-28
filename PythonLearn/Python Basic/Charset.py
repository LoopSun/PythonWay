#!/user/bin/python3
#^.^ coding=utf-8 ^.^#

# ASCII
# Unicode
# UTF-8


#ASCII is a subset of Unicode

print("'A' ASCII Code:", ord('A'))

print("34678 Unicode Char:", chr(34678))

# In Python3, if want to transmit string in network, need to transform string to bytes.
str_type = "abc"
bytes = b'abc'

print("str type:", type(str_type))
print("bytes type:", type(bytes))
print("encode type:", type('ABC'.encode()))  # default utf-8
print("decode type:", type('ABC'.encode().decode()))  # default utf-8