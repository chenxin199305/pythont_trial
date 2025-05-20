import time
import threading
import math


def cpu_intensive_task(duration_sec: float, thread_id: int):
    """
    CPU密集型任务，计算平方根多次
    """
    start_time = time.time()
    iterations = 0

    while time.time() - start_time < duration_sec:
        # 执行一些计算密集型操作
        math.sqrt(iterations ** 2 + 1)
        iterations += 1

    print(f"Thread {thread_id} completed {iterations:,} iterations in {duration_sec} seconds")


if __name__ == "__main__":
    # 测试持续时间(秒)
    test_duration = 5

    # 单线程测试
    print("Running single-threaded test...")
    start_time = time.time()
    cpu_intensive_task(test_duration, 1)
    single_thread_time = time.time() - start_time
    print(f"Single-threaded execution time: {single_thread_time:.2f} seconds\n")

    # 多线程测试
    print("Running multi-threaded test...")
    start_time = time.time()

    # 创建并启动线程
    threads = []
    for i in range(1, 5):  # 四个线程
        t = threading.Thread(target=cpu_intensive_task, args=(test_duration, i))
        threads.append(t)
        t.start()

    # 等待所有线程完成
    for t in threads:
        t.join()

    multi_thread_time = time.time() - start_time
    print(f"Multi-threaded execution time: {multi_thread_time:.2f} seconds")

    # 性能比较
    if multi_thread_time < single_thread_time * 0.8:  # 允许一些开销
        print("\nSignificant speedup detected - likely running without GIL!")
    else:
        print("\nLittle speedup detected - likely running with GIL limitation.")
