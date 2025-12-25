import asyncio
import sys
from do_something import do_something

async def sum_integers(limit: int):
    val = sum(range(limit + 1))
    await asyncio.sleep(2)
    return f"Sum Coroutine: Result = {val}"

async def calc_factorial(limit: int):
    res = 1
    for i in range(1, limit + 1):
        res *= i
    await asyncio.sleep(2)
    return f"Factorial Coroutine: Result = {res}"

async def compute_heavy(size: int):
    current_loop = asyncio.get_running_loop()
    buffer = []
    # Using executor to prevent blocking
    await current_loop.run_in_executor(None, do_something, size, buffer)
    final = buffer[-1] if buffer else "No Data"
    return f"CPU Coroutine: Processed {size} units. End value: {final}"

async def main(a, b, c):
    jobs = await asyncio.gather(
        sum_integers(a),
        calc_factorial(b),
        compute_heavy(c)
    )
    for report in jobs:
        print(report)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Required args: <sum_limit> <fact_limit> <cpu_size>")
        sys.exit(1)
    
    asyncio.run(main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))