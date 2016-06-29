#!/user/bin/python3
#^.^ coding=utf-8 ^.^#
from HelloWorld import cute_split_line

# 1. threading
# 2. lock
# 3. ThreadLocal

#*************** threading ***************#

import threading
from threading import Thread
from time import sleep

'''
def loop():
    print("thread %s is running..."%threading.current_thread().name)
    n = 0
    while n <5:
        n = n + 1
        print('thread %s print num %s'%(threading.current_thread().name, n))
        sleep(0.1)
    print('thread %s ended.'%threading.current_thread().name)

print('thread %s is running...'%threading.current_thread().name)
t = Thread(target=loop, name="subthread")
t.start()
n = 0
while n < 5:
    n = n + 1
    print('thread %s print num %s' % (threading.current_thread().name, n))
    sleep(0.1)
t.join()
print('thread %s ended.'%threading.current_thread().name)
'''
cute_split_line()
#*************** lock ***************#
'''
# lock is a thing which nobody like
lock = threading.Lock()
balance = 0

def change_balance(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread():
    for i in range(1000000):
        lock.acquire()
        try:
            change_balance(i)
        finally:
            lock.release()

t1 = Thread(target=run_thread, name="t1")
t2 = Thread(target=run_thread, name="t2")

t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
'''
cute_split_line()
#*************** ThreadLocal ***************#

local_school = threading.local()

def process_student():
    std = local_school.student
    print("%s --- %s"%(threading.current_thread().name, std))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = Thread(target=process_thread, args=("Sun",), name="subThreadA")
t2 = Thread(target=process_thread, args=("Moon",), name="subThreadB")
t1.start()
t2.start()
t1.join()
t2.join()


