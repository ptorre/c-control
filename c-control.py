#!/usr/bin/env python

import asyncio
import websockets
import json
import argparse


async def navigate(ws, url):
    async with websockets.client.connect(ws) as websocket:
        await websocket.send(
            json.dumps(
                {
                    "id": 1,
                    "method": "Page.navigate",
                    "params": {
                        "url": url
                    },
                }
            )
        )
        print(await websocket.recv())


parser = argparse.ArgumentParser(description="Navigate through debug interface.")
parser.add_argument("ws", metavar="ws", type=str, help="Browser websocket address")
parser.add_argument("url", metavar="url", type=str, help="target url")

args = parser.parse_args()

asyncio.get_event_loop().run_until_complete(
    navigate(args.ws, args.url)
)
