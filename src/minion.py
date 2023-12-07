#!/usr/bin/env python3

import manager


class Minion(manager.QueueClient):
    """
    Gets work from a queue
    """

    def __init__(self):
        super().__init__()

    def get_from_queue(self):
        print(self.task_queue.empty())
        return self.client.task_queue.get()


if __name__ == "__main__":
    minion = Minion()
    minion.get_from_queue()
