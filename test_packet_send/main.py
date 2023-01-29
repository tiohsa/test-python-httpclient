import requests
import json
import aiohttp
import asyncio
import time

# GET先URL
url = "http://localhost:8000/item/"

# JSON形式のデータ
json_data = {
    "name": "val1"
}


async def get_request(session, no):
    response = await session.get(f'http://localhost:8000/?no={no}')
    content = await response.json()
    print(f"{time.strftime('%X')} - {response.status} {content}\n", end='')


async def post_request(session, no):
    item = {
        "name": no
    }
    response = await session.post(f'http://localhost:8000/item/?no={no}', json=item)
    content = await response.json()
    print(f"{time.strftime('%X')} - {response.status} {content}\n", end='')


async def main():
    tasks = []
    print(f"{time.strftime('%X')} - Start")
    async with aiohttp.ClientSession() as session:
        for n in range(300):
            # tasks.append(get_request(session, n+1))
            tasks.append(post_request(session, n+1))
        await asyncio.gather(*tasks)
    print(f"{time.strftime('%X')} - Finish")

asyncio.run(main())
