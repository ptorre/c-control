#!/usr/bin/env python

import asyncio
import websockets
import json

async def navigate(uri):
    async with websockets.client.connect(uri) as websocket:
        await websocket.send(
            json.dumps(
                {
                    'id': 1,
                    'method': "Page.navigate",
                    'params': {'url': "file:///media/ghost-in-the-shell-tatikoma.jpg"},
                }
            )
        )
        print(await websocket.recv())

asyncio.get_event_loop().run_until_complete(
    navigate("ws://192.168.1.128:9222/devtools/page/706A2FB6220E5DF9ECD1C1DD3C2BCD97")
)
