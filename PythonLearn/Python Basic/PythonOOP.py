#!/user/bin/python3
#^.^ coding=utf-8 ^.^#
from HelloWorld import cute_split_line
# 1. class and object
# 2. inheritance and polymorphism
# 3. __slots__
# 4. @property
# 5. Enum
# 6. user-defined class
# 6. meta class


#*********** class and object ***********#
class Rabbit:
    doc = "a cute rabbit"
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return self.__name

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

num_1_rabbit = Rabbit("Luy", 3)

print("num_1_rabbit:", num_1_rabbit)
print("num_1_rabbit age:", num_1_rabbit._Rabbit__age)

cute_split_line()

#*********** inheritance and polymorphism ***********#

class ChinaRabbit(Rabbit):
    def __init__(self, name, age):
        super(ChinaRabbit, self).__init__(name, age)

#*********** __slots__ ***********#

#limit the dynamic attribution define
class Dog:
    __slots__ = ("name", "age")

cute_split_line()

#*********** @property ***********#

class Student:
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

s1 = Student()
s1.score = 99
print("Student Score: ", s1.score)

cute_split_line()

#*********** Enum ***********#
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

#*********** user-defined class ***********#

class Rain(object):
    def __index__(self):
        self.status = "Sleeping"

    def __str__(self):
        return "Rain baby is %s"%self.status

    def __getattr__(self, item):
        return None

    def __call__(self, *args, **kwargs):
        return "Hi, I am rain."

    def __eq__(self, other):
        return True

cute_split_line()

#*********** meta class ***********#

def say(self, word = "good night"):
    print(word)

Say = type("Say", (object,), dict(say=say))

s = Say()

print("Say said:", s.say())
print("Say type:", type(Say))
print("s type:", type(s))

cute_split_line()
