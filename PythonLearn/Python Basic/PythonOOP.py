#!/user/bin/python3
#^.^ coding=utf-8 ^.^#
from HelloWorld import cute_split_line
# 1. class and object
# 2. inheritance and polymorphism
# 3. __slots__
# 4. @property


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
        return self.score

    @property.setter
    def score(self, score):
        self.score = score
