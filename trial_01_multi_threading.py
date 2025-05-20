import time
import threading

if __name__ == "__main__":
    def thread1_function():
        # create a CPU high load task
        while True:
            print("Thread 1")


    def thread2_function():
        # create a CPU high load task
        while True:
            print("Thread 2")


    # Create threads
    thread1 = threading.Thread(target=thread1_function)
    thread2 = threading.Thread(target=thread2_function)

    # Start threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    print("Done!")
