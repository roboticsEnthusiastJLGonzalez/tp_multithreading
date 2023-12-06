#!/usr/bin/env python3

from multiprocessing import Queue, managers


class QueueManager(managers.BaseManager):
    """
    Holds and manages queues for tasks and results
    """

    def __init__(self, address, authkey):
        super().__init__(address=address, authkey=authkey)
        self.task_queue = Queue()
        self.result_queue = Queue()


class QueueClient:
    """
    Puts or gets item from a QueueManager's queue
    """

    def __init__(self, address, authkey):
        self.client = managers.BaseManager(address, authkey)
        self.client.connect()


if __name__ == "__main__":
    manager = QueueManager(address=("", 50000), authkey=b"id_key")
    server = manager.get_server()
    server.serve_forever()
