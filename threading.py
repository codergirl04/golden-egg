import threading
import time


# takes the number of the thread and sleeps for one second
def sleep_job(thread_num):
    print("Thread %s entering sleep_job" % thread_num)
    time.sleep(1)
    print("Thread %s exiting sleep_job" % thread_num)


# takes the number of the thread and prints "5"
def print_job(thread_num):
    print("Thread %s entering print_job" % thread_num)
    print("5")
    print("Thread %s exiting print_job" % thread_num)


class SleepThread(threading.Thread):
    def __init__(self, thread_num):
        super(SleepThread, self).__init__()
        self.thread_num = thread_num

    def run(self):
        print("Thread %s entering sleep_job" % self.thread_num)
        time.sleep(1)
        print("Thread %s exiting sleep_job" % self.thread_num)


class PrintThread(threading.Thread):
    def __init__(self, thread_num):
        super(PrintThread, self).__init__()
        self.thread_num = thread_num

    def run(self):
        print("Thread %s entering print_job" % self.thread_num)
        print("5")
        print("Thread %s exiting print_job" % self.thread_num)


if __name__ == "__main__":
    # try:
    #     # create a thread to run sleep_job
    #     thread_1 = threading.Thread(target=sleep_job, args="1")
    #     thread_1.start()
    #     # make sure thread 1 finishes first
    #     thread_1.join()
    #     # create a thread to run print_job
    #     thread_2 = threading.Thread(target=print_job, args="2")
    #     thread_2.start()
    # except:
    #     print("Error creating threads.")
    thread_1 = SleepThread("1")
    thread_1.start()
    thread_1.join()
    thread_2 = PrintThread("2")
    thread_2.start()




# output
# Thread 1 entering sleep_job
# Thread 1 exiting sleep_job
# Thread 2 entering print_job
# 5
# Thread 2 exiting print_job