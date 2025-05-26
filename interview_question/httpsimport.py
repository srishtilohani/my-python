import aiohttp
import asyncio

async def fetch_url(URL):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response.status

asyncio.run(fetch_url("https://example.com"))