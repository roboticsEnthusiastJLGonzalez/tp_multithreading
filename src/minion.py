#!/usr/bin/env python3

import manager


class Minion(manager.QueueClient):
    """
    Gets work from a queue
    """

    def __init__(self):
        super().__init__()

    def exec_task(self):
        while True:
            if self.task_queue.empty():
                print("I have nothing to do, manager!")
                break
            task = self.task_queue.get()
            exec_task_time = task.work()
            print(exec_task_time)
            self.result_queue.put(exec_task_time)


if __name__ == "__main__":
    minion = Minion()
    minion.exec_task()
