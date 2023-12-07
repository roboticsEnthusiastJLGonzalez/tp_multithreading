#!/usr/bin/env python3

from multiprocessing import Queue
from multiprocessing.managers import BaseManager

address = ("localhost", 50000)
authkey = b"key"


class QueueManager(BaseManager):
    """
    Holds and manages queues for tasks and results
    """

    def __init__(self, address, authkey):
        super().__init__(address=address, authkey=authkey)

        self.task_queue = Queue()
        self.result_queue = Queue()

        self.register("get_task_queue", callable=lambda: self.task_queue)
        self.register("get_result_queue", callable=lambda: self.result_queue)

    def run(self):
        print("manager running")
        server = self.get_server()
        server.serve_forever()

    def get_task_queue(self):
        return self.task_queue

    def get_result_queue(self):
        return self.result_queue


class QueueClient:
    """
    Puts or gets item from a QueueManager's queue
    """

    task_queue = Queue()
    result_queue = Queue()

    def __init__(self):
        QueueManager.register("get_task_queue")
        QueueManager.register("get_result_queue")
        self.client = QueueManager(address, authkey)
        self.client.connect()
        self.task_queue = self.client.get_task_queue()
        self.result_queue = self.client.get_result_queue()


if __name__ == "__main__":
    manager = QueueManager(address, authkey)
    manager.run()
