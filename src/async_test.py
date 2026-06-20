import asyncio
import time


async def fun_1(x: int):
    print("fun_1 before sleep")
    await asyncio.sleep(x)
    print("fun_1 after sleep")

async def fun_2(x: int = 3):
    print("fun_2 before sleep")
    await asyncio.sleep(x)
    print(f"fun_2 after sleep. result {x**x}")

async def main():
    task1 = asyncio.create_task(fun_1(5))
    task2 = asyncio.create_task(fun_2())
    await task1
    await task2


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    after_s = time.perf_counter() -s
    print(f"{after_s:0.2f} seconds")