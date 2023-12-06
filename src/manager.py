#!/usr/bin/env python3

from multiprocessing import Queue, managers

address = ("", 50000)
authkey = b"id_key"


class QueueManager(managers.BaseManager):
    """
    Holds and manages queues for tasks and results
    """

    def __init__(self, address, authkey):
        super().__init__(address=address, authkey=authkey)
        self.task_queue = Queue()
        self.result_queue = Queue()

        self.register("get_task_queue", callable=lambda: self.task_queue)
        self.register("get_result_queue", callable=lambda: self.result_queue)


class QueueClient:
    """
    Puts or gets item from a QueueManager's queue
    """

    def __init__(self):
        QueueManager.register("get_task_queue")
        QueueManager.register("get_result_queue")
        self.client = QueueManager(address, authkey)
        self.client.connect()


if __name__ == "__main__":
    manager = QueueManager(address, authkey)
    server = manager.get_server()
    server.serve_forever()
