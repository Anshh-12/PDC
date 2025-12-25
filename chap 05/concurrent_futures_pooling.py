import concurrent.futures
import time
import do_something

items_to_process = list(range(1, 12))

def process_item(val):
    results = []
    do_something.do_something(val, results)
    status = results[-1] if results else "Empty"
    print(f'Processed {val} | Last entry: {status}')

if __name__ == '__main__':
    # 1. Standard Loop
    t0 = time.perf_counter()
    for x in items_to_process:
        process_item(x)
    print(f'Sequential total: {time.perf_counter() - t0:.3f}s')

    # 2. Multithreading
    t1 = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as threads:
        threads.map(process_item, items_to_process)
    print(f'Thread Pool total: {time.perf_counter() - t1:.3f}s')

    # 3. Multiprocessing
    t2 = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as procs:
        procs.map(process_item, items_to_process)
    print(f'Process Pool total: {time.perf_counter() - t2:.3f}s')