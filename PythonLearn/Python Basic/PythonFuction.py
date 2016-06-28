#!/user/bin/python3
#^.^ coding=utf-8 ^.^#
from time import ctime
from functools import partial
# 1. function define
# 2. function arguments
# 3. recursive function
# 4. closure
# 5. lambda
# 6. decorator
# 7. Partial function


#************* function define *************#
def fib(limit):
    a, b = 0, 1
    while a < limit:
        print(a, end= ' ')
        a, b = b, a+b
    print()

fib(1000)

#************* function arguments *************#

def fib():
    limit = 1000
    a, b = 0, 1
    while a < limit:
        print(a, end= ' ')
        a, b = b, a+b

#fib()

def fib(end_flag ,limit = 1000):
    limit = 1000
    a, b = 0, 1
    while a < limit:
        print(a, end= end_flag)
        a, b = b, a+b

#fib('|')

def fib(*args):
    limit = args[0]
    flag = args[1]
    a, b = 0, 1
    while a < limit:
        print(a, end= end_flag)
        a, b = b, a+b
    return 0

#fib(1000, '|')

def fib(**kwargs):
    limit = kwargs['limit']
    flag = kwargs['flag']
    a, b = 0, 1
    while a < limit:
        print(a, end=end_flag)
        a, b = b, a + b
    return 0

#fib(limit = 1000, flag = '|')

def fib(name, *args,**kwargs):   #comfuse arguments, use it less.
    print(len(args))
    limit = kwargs['limit']
    flag = kwargs['flag']
    a, b = 0, 1
    while a < limit:
        print(a, end=end_flag)
        a, b = b, a + b
    return 0
print("*"*20)

#************* recursive function *************#
def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n-1)

print(factorial(5))


#***************** closure *****************#
def lazy_sum(*args):
    def sum_args():
        return sum(args)
    return sum_args

f = lazy_sum(1, 2, 3 ,4 ,5)
print("f:", f)
print("f type:", type(f))
print("result:", f())
print("*"*20)
#***************** lambda *****************#

# lambda x: x * x
# lambda x, y: x + y

#***************** decorator *****************#
def log(func):
    def wrapper(*args, **kwargs):
        print("called {}()".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

@log
def now_time():
    print(ctime())

# now_time() = log(wrapper(func))
now_time()
print("*"*20)

#***************** Partial function *****************#
int2 = partial(int, base = 2)
print("binary 10101011 to int:", int2("10101011"))