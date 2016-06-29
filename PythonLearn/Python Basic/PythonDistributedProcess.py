#!/user/bin/python3
#^.^ coding=utf-8 ^.^#
from HelloWorld import cute_split_line

# 1. process manager

from multiprocessing import Process, Pool
from multiprocessing.managers import BaseManager
import random, time, queue

#*************** process manager ***************#

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register("get_task_queue", callable = lambda:task_queue)
QueueManager.register("get_result_queue", callable = lambda:result_queue)

manager = QueueManager(address = ('', 7777), authkey = "123".encode())
manager.start()
task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    n = random.randint(0, 1000)
    print('Put task %d...'%n)
    task.input(n)

print('Try get result...')
for i in range(10):
    r = result.get(timeout = 10)
    print("Result: %s"%r)

manager.shutdown()
print('master exit.')

