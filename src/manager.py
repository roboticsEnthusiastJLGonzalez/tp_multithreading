#!/usr/bin/env python3

from multiprocessing import Queue, managers


class QueueManager(managers.BaseManager):
    """
    Holds and manages queues for tasks and results
    """

    def __init__(self):
        self.task_queue = Queue()
        self.result_queue = Queue()


class QueueClient:
    """
    Puts or gets item from a QueueManager's queue
    """

    def __init__(self):
        pass


if __name__ == "__main__":
    pass
