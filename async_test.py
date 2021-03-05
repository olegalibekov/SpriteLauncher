import asyncio

# async def factorial(name, number):
#     f = 1
#     for i in range(2, number + 1):
#         print(f"Task {name}: Compute factorial({i})...")
#         await asyncio.sleep(1)
#         f *= i
#     print(f"Task {name}: factorial({number}) = {f}")
#
#
# async def main():
#     # Schedule three calls *concurrently*:
#     await asyncio.gather(
#         factorial("A", 2),
#         factorial("B", 3),
#         factorial("C", 4),
#     )
#
#
# loop = asyncio.get_event_loop()
#
# result = loop.run_until_complete(main())

import asyncio


async def first():
    for i in range(0, 10):
        await asyncio.sleep(0.1)
        print(i)


async def second():
    for i in range(10, 20):
        await asyncio.sleep(0.1)
        print(i)


async def main():
    await asyncio.gather(first(), second())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
