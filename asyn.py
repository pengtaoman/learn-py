import asyncio

import random


async def print_number(number):
    await asyncio.sleep(random.random())
    print(number)

async def async_hello():
    print("hello, world!")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.gather(*[
            print_number(number)
            for number in range(20)
        ])
    )
    loop.close()