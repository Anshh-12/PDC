import asyncio
import random
import do_something as worker

async def node_a(cutoff):
    print("[Node A Active]")
    loop = asyncio.get_running_loop()
    temp_list = []
    await loop.run_in_executor(None, worker.do_something, random.randint(100, 1000), temp_list)
    
    await asyncio.sleep(1)
    if loop.time() < cutoff:
        await node_b(cutoff)

async def node_b(cutoff):
    print("[Node B Active]")
    loop = asyncio.get_running_loop()
    temp_list = []
    await loop.run_in_executor(None, worker.do_something, random.randint(100, 1000), temp_list)
    
    await asyncio.sleep(1)
    if loop.time() < cutoff:
        await node_c(cutoff)

async def node_c(cutoff):
    print("[Node C Active]")
    loop = asyncio.get_running_loop()
    temp_list = []
    await loop.run_in_executor(None, worker.do_something, random.randint(100, 1000), temp_list)
    
    await asyncio.sleep(1)
    if loop.time() < cutoff:
        await node_a(cutoff)

async def start_loop():
    deadline = asyncio.get_running_loop().time() + 45
    await node_a(deadline)

if __name__ == "__main__":
    asyncio.run(start_loop())