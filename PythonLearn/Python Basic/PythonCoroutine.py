#!/user/bin/python3
#^.^ coding=utf-8 ^.^#
from HelloWorld import cute_split_line


# 1. coroutine
# 2. asyncio
# 3. async/await
# 4. aiohttp

#*************** coroutine ***************#
'''
def customer():
    r= ''
    while True:
        n = yield r
        if not n:
            return
        print('[Customer] Consuming %s...'%n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[Producer] Producing %s...'%n)
        r = c.send(n)
        print('[Producer] Consuming return: %s'%r)
    c.close()

c =customer()
produce(c)

'''
cute_split_line()

#*************** asyncio ***************#
import asyncio
import threading
'''
@asyncio.coroutine
def hello():
    print("Hello World.(%s)"%threading.current_thread())
    r = yield from asyncio.sleep(0.1)
    # print("r:", r)
    print("Hello again.(%s)"%threading.current_thread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello(),]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''
cute_split_line()
'''
@asyncio.coroutine
def wget(host):
    print('wget %s...'%host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n'%host
    writer.write(header.encode())
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header> %s'%(host, line.decode().rstrip()))

    writer.close()

loop = asyncio.get_event_loop()
urls = ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']
tasks = [wget(host) for host in urls]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''
cute_split_line()

#*************** async/await ***************#
# for 3.5 or upper
'''
async def wget(host):
    print('wget %s...'%host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n'%host
    writer.write(header.encode())
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header> %s'%(host, line.decode().rstrip()))

    writer.close()

loop = asyncio.get_event_loop()
urls = ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']
tasks = [wget(host) for host in urls]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''
cute_split_line()
#*************** aiohttp ***************#

import asyncio
from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    text = '<h1>Index</h1>'.encode()
    return web.Response(body=text)

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>Hello, %s!<h1>'%request.match_info['name']
    return web.Response(body=text.encode())

async def init(loop):
    app = web.Application(loop= loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}',hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server Started at http://127.0.0.1:8000')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()