#!/usr/bin/env python3

import manager
import task


class Boss(manager.QueueClient):
    """
    Puts work in a queue
    """

    def __init__(self):
        super().__init__()

    def put_in_queue(self, item):
        self.task_queue.put(item)


if __name__ == "__main__":
    boss = Boss()
    task_for_minion = task.Task(0, 3)
    boss.put_in_queue(task_for_minion)
