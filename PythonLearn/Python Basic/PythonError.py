#!/user/bin/python3
#^.^ coding=utf-8 ^.^#
from HelloWorld import cute_split_line
import unittest
import doctest

# 1. try...except...finally
# 2. raise
# 3. assert
# 4. unittest
# 5. doctest

#********** try...except...finally **********#

try:
    from xml.etree import cElementTree as ET
except ImportError:
    from xml.etree import ElementTree as ET
finally:
    pass

cute_split_line()

#********** raise **********#

if 1 == 0:
    raise SystemError("It's impossible")
cute_split_line()
#********** assert **********#

m = 10
n = 0
try:
    assert n != 0, 'n is zero'
except AssertionError as err:
    print("Error information:", err)
cute_split_line()