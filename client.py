#!/usr/bin/env python

import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://192.168.33.10:8765') as websocket:

        hash = input("Give me the path to file >: ")
        await websocket.send(hash)

        while 1:
            greeting = await websocket.recv()
            print(greeting)

try:
    asyncio.get_event_loop().run_until_complete(hello())
except:
    print('done')
