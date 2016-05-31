#!/usr/bin/env python

import asyncio
import websockets
import time

async def sendLog(websocket, path):
    filePath = await websocket.recv()

    file = open('{}'.format(filePath), 'r')

    fileString = file.read()
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

                await websocket.send(line)

start_server = websockets.serve(sendLog, '0.0.0.0', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
