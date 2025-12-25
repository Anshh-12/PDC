# Performance Comparison: Concurrency Models in Python

This project analyzes the behavior of **Asyncio**, **Multithreading**, and **Multiprocessing** across different computational tasks.

---

## Analysis of Scripts

### 1. Task Management (`asyncio_task_manipulation.py`)
- Demonstrates cooperative multitasking.
- Confirms that `asyncio.sleep` allows other tasks to progress.
- CPU tasks are safely offloaded to threads using `to_thread`.

### 2. Execution Pools (`concurrent_futures_pooling.py`)
- **Comparison Results:**
    - *Sequential:* Baseline performance.
    - *Threads:* Good for I/O; limited by GIL for math.
    - *Processes:* Fastest for heavy computation, but has high startup costs.

### 3. Integrated Coroutines (`asyncio_and_futures.py`)
- Shows how `asyncio` acts as an orchestrator for both simple async functions and heavy calculations.

### 4. Recursive Chaining (`asyncio_coroutine.py` & `asyncio_event_loop.py`)
- Explores event loop persistence and recursive scheduling.
- Highlights the importance of termination conditions in async loops.

---

## Technical Summary

| Model | Primary Use Case | Parallelism |
| :--- | :--- | :--- |
| **Asyncio** | Web servers, I/O tasks | Cooperative (Single-core) |
| **Threading** | Waiting for responses/files | Shared Memory (GIL limited) |
| **Multi-processing** | Heavy math and data crunching | True Parallel (Multi-core) |

---