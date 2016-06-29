#!/user/bin/python3
#^.^ coding=utf-8 ^.^#
from HelloWorld import cute_split_line

# 1. open
# 2. StringIO BytesIO
# 3. os model
# 4. pickling


#************ open ************#
try:
    with open(r"/home/python/readme.md", 'rb') as readme:
        readme = readme.read()
except FileNotFoundError:
    print()
except PermissionError:
    print()
finally:
    pass

cute_split_line()

#************ StringIO BytesIO ************#

from io import StringIO, BytesIO

str_io = StringIO()
str_io.write('StringIO')
print("str_io:", str_io.getvalue())

bytes_io = BytesIO()
bytes_io.write('BytesIO'.encode())
print("bytes_io:", bytes_io.getvalue())

cute_split_line()

#************ os model ************#

import os
import sys
print("os name:", os.name)
# print("os uname:", os.uname())
print("os environ:", os.environ)
print("os environ OS:", os.environ.get('OS'))
print("pwd:", os.path.abspath('.'))
print("current file:", os.path.join(os.path.abspath('.'), sys.argv[0]))
print("split current file path:", os.path.split(os.path.join(os.path.abspath('.'), sys.argv[0])))
print("split current file suffix :", os.path.splitext(os.path.join(os.path.abspath('.'), sys.argv[0])))
# os.rename()
# os.remove()
# os.path.isdir()
# os.path.isfile()
# os.path.islink()
# os.path.ismount()
# os.path.exists()
# os.listdir()

cute_split_line()

#************ pickling ************#
##xml, json, bson also ok

user_dict = dict.fromkeys(range(10), "Peg")
import pickle
print("user_dict pickle:", pickle.dumps(user_dict))
print("user_dict pickle decode:", pickle.loads(pickle.dumps(user_dict)))
import json
print("user_dict json:", json.dumps(user_dict))
print("user_dict json decode:", json.loads(json.dumps(user_dict)))
import bson
import xml