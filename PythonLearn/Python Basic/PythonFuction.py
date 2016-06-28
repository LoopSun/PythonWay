#!/user/bin/python3
#^.^ coding=utf-8 ^.^#

# 1. function define
# 2. function arguments
# 3. recursive function


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