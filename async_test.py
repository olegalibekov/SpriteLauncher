import asyncio


async def first():
    await asyncio.sleep(1)
    return "1"


async def second():
    await asyncio.sleep(1)
    return "2"


async def main():
    async def one_iteration():
        result = await first()
        print(result)
        result2 = await second()
        print(result2)

    # coros = [one_iteration() for _ in range(2)]
    await asyncio.gather(one_iteration(), one_iteration())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
