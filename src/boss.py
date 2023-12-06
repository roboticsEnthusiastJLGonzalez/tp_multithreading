#!/usr/bin/env python3

import manager


class Boss(manager.QueueClient):
    """
    Puts work in a queue
    """

    def __init__(self):
        super().__init__()

    def put_in_queue(self, item):
        self.client.task_queue.put(item)


if __name__ == "__main__":
    boss = Boss()
    boss.put_in_queue("hello")
