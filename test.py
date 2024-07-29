import asyncio
import time


def hera(number):
    for i in range(10):
        time.sleep(1)
        print(f'{number} - {i}')



async def main():
    for i in range(5):
        hera(i)
        time.sleep(0.5)
    return 'hello'

asyncio.run(main())