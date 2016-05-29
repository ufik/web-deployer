#!/usr/bin/env python

import asyncio
import websockets
import time

async def hello(websocket, path):
    hash = await websocket.recv()

    file = open('/tmp/deploy-{}.log'.format(hash), 'r')

    fileString = file.read()
    print(fileString)
    await websocket.send(fileString)

    if '#EOF#' not in fileString:
        while 1:
            where = file.tell()
            line = file.readline()
            if not line:
                time.sleep(1)
                file.seek(where)
            else:
                if '#EOF#' in line:
                    break

                print(line)
                await websocket.send(line)

start_server = websockets.serve(hello, '0.0.0.0', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
