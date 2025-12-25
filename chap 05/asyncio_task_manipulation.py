import asyncio
import do_something

async def run_factorial(n):
    total = 1
    for i in range(2, n + 1):
        print(f'Async Process: Factorial step {i}')
        await asyncio.sleep(0.5)
        total *= i
    print(f'Async Process - Factorial result for {n}: {total}')

async def run_fibonacci(n):
    prev, curr = 0, 1
    for i in range(n):
        print(f'Async Process: Fibonacci index {i}')
        await asyncio.sleep(0.5)
        prev, curr = curr, prev + curr
    print(f'Async Process - Fibonacci final: {prev}')

async def run_binomial(n, k):
    val = 1
    for i in range(1, k + 1):
        val = val * (n - i + 1) / i
        print(f'Async Process: Binomial calculation {i}')
        await asyncio.sleep(0.5)
    print(f'Async Process - Binomial({n}, {k}): {val}')

async def main():
    shared_list = []
    
    # Bundle tasks together
    async_tasks = [
        asyncio.create_task(run_factorial(8)),
        asyncio.create_task(run_fibonacci(8)),
        asyncio.create_task(run_binomial(15, 5)),
        # Offload the math-heavy module to a thread
        asyncio.create_task(
            asyncio.to_thread(do_something.do_something, 5, shared_list)
        )
    ]
    
    await asyncio.gather(*async_tasks)
    print("Execution complete. Worker output:", shared_list)

if __name__ == "__main__":
    asyncio.run(main())