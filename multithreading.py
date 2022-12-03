import time
import threading

# def my_function():
#     print("printing from thread")
#
#
#
# if __name__ == "__main__":
#     thread = Thread(target=my_function)
#     thread.start()
#     thread.join()


def my_function():
    print("printing from thread")


# Python program to explain the
# use of join() method in Thread class




def thread_1(i):
    time.sleep(0)
    print('Value by Thread 1:', i)


def thread_2(i):
    time.sleep(0)
    print('Value by Thread 2:', i)


def thread_3(i):
    print('Value by Thread 3:', i)


# Creating three sample threads
thread1 = threading.Thread(target=thread_1, args=(1,))
thread2 = threading.Thread(target=thread_2, args=(2,))
thread3 = threading.Thread(target=thread_3, args=(3,))

# Running three thread object
thread1.start()

thread2.start()
thread2.join()
thread3.start()
thread3.join()
thread1.join()

print()
# Creating another 3 threads
# thread4 = threading.Thread(target=thread_1, args=(1,))
# thread5 = threading.Thread(target=thread_2, args=(2,))
# thread6 = threading.Thread(target=thread_3, args=(3,))
#
# thread4.start()
# thread5.start()
# thread6.start()
# thread4.join()
# thread5.join()
# thread6.join()


# if __name__ == "__main__":
#     threads = [threading.Thread(target=my_function) for _ in range(10)]
#     for thread in threads:
#         thread.start()
#
#     for thread in threads:
#         thread.join()