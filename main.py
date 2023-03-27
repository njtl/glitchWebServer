import asyncio
import random
import logging
from aiohttp import web

# Define color codes for logging messages
GREEN = '\033[32m'
RED = '\033[31m'
ORANGE = '\033[33m'
RESET = '\033[0m'


async def handle():
    if random.random() < 0.05:
        # 5% chance of 500 error
        logging.info(f'{RED}Not answering request{RESET}')
        return web.Response(status=500)
    elif random.random() < 0.05:
        # 5% chance of 404 error
        logging.info(f'{RED}Sending 404 as a response{RESET}')
        return web.Response(status=404)
    elif random.random() < 0.1:
        # 10% chance of delaying the response by 2 seconds
        logging.info(f'{ORANGE}Delaying response{RESET}')
        await asyncio.sleep(2)
    logging.info(f'{GREEN}Answering request{RESET}')
    return web.Response(text="200OK")


async def init_app():
    this_app = web.Application()
    this_app.router.add_route('*', '/{tail:.*}', handle)
    return this_app


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_app())
    web.run_app(app, port=8765)
