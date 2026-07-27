import asyncio
import time


async def run_task(name, seconds):
    print(f"{name} started")
    await asyncio.sleep(seconds)
    print(f"{name} finished")
    return f"{name} result"


async def run_sequential(tasks):
    results = []
    for name, seconds in tasks:
        result = await run_task(name, seconds)
        results.append(result)
    return results


async def run_concurrent(tasks):
    coroutines = [run_task(name, seconds) for name, seconds in tasks]
    results = await asyncio.gather(*coroutines)
    return results


async def main():
    tasks = [
        ("Downloading data", 3),
        ("Processing data", 2),
        ("Sending notification", 1),
        ("Saving results", 4),
    ]

    start = time.time()
    await run_sequential(tasks)
    sequential_time = time.time() - start

    print()

    start = time.time()
    await run_concurrent(tasks)
    concurrent_time = time.time() - start

    print()
    print(f"Sequential execution time: {sequential_time:.2f} seconds")
    print(f"Concurrent execution time: {concurrent_time:.2f} seconds")


asyncio.run(main())
