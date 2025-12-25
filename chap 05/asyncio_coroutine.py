import asyncio
import random
from do_something import do_something

async def step_one(limit):
    print("--- Entering Step One ---")
    data = []
    engine = asyncio.get_running_loop()
    await engine.run_in_executor(None, do_something, random.randint(500, 2000), data)
    
    await asyncio.sleep(random.uniform(0.5, 1.5))
    if engine.time() < limit:
        await step_two(limit)
    else:
        print("Closing routine via Step One")

async def step_two(limit):
    print("--- Entering Step Two ---")
    data = []
    engine = asyncio.get_running_loop()
    await engine.run_in_executor(None, do_something, random.randint(500, 2000), data)
    
    await asyncio.sleep(random.uniform(0.5, 1.5))
    if engine.time() < limit:
        await step_three(limit)
    else:
        print("Closing routine via Step Two")

async def step_three(limit):
    print("--- Entering Step Three ---")
    data = []
    engine = asyncio.get_running_loop()
    await engine.run_in_executor(None, do_something, random.randint(500, 2000), data)
    
    await asyncio.sleep(random.uniform(0.5, 1.5))
    if engine.time() < limit:
        await step_one(limit)
    else:
        print("Closing routine via Step Three")

async def main():
    now = asyncio.get_running_loop().time()
    await step_one(now + 30) # Run for 30 seconds

if __name__ == "__main__":
    asyncio.run(main())