#!/user/bin/python3
#^.^ coding=utf-8 ^.^#
from HelloWorld import cute_split_line

# 1. Process
# 2. Pool
# 3. subprocess
# 4. Queue Pipes Value Array

#************* Process *************#

import os
from multiprocessing import Process, Pool, Queue, Pipe
from time import sleep
def worker(name):
    print('Run child process %s (%s)'%(name, os.getpid()))
    # sleep(1)
'''
if __name__ == '__main__':
    print('Parent process %s start...'%(os.getpid()))
    p = Process(target=worker, args=('subprocess',))
    print('Child process start...')
    p.start()
    p.join()  #syn
    print("Child process end.")
'''
cute_split_line()

#************* Pool *************#
'''
if __name__ == '__main__':
    print('Parent process %s start...'%(os.getpid()))
    p = Pool(4)
    for i in range(5):
        p.apply_async(worker, args=(i,))
    print('Waiting for all subprocesses done....')
    p.close()
    p.join()  #syn
    print("All subprocesses done.")
'''
cute_split_line()

#************ subprocess ************#
cute_split_line()

#************ Queue Pipes ************#

def write_msg(q, p):
    print("Process(%s) prepares to write"%(os.getpid()))
    for var in (odd for odd in range(100) if odd % 2):
        print('Put %s to queue...'%(var))
        q.put(var)
        print('Put %s to pipe...' % (var))
        p.send(var)
        sleep(0.01)

def read_msg(q,p):
    print("Process(%s) prepares to read" % (os.getpid()))
    while True:
        var = q.get(True)
        print('Get %s from queue...'%(var))
        print('Get %s from pipe...' % (p.recv()))

if __name__ == "__main__":
    q = Queue()
    p_p, c_p = Pipe()
    pw = Process(target=write_msg, args=(q, c_p))
    pr = Process(target=read_msg, args=(q, p_p))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()