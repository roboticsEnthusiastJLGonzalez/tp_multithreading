#!/usr/bin/env python3

import json
from time import perf_counter

import numpy as np


class Task:
    def __init__(self, identifier: int, size: int, a=None, b=None, x=None, time=None):
        self.identifier = identifier
        self.size = size
        if a is None:
            self.a = np.random.rand(size, size)
        else:
            self.a = a
        if b is None:
            self.b = np.random.rand(
                size,
            )
        else:
            self.b = b
        if x is None:
            self.x = np.zeros((size,))
        else:
            self.x = x
        if time is None:
            self.time = 0.0
        else:
            self.time = time

    def work(self) -> float:
        time_start = perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        time_end = perf_counter()
        self.time = time_end - time_start
        return self.time

    def to_json(self) -> str:
        class_info = {
            "size": self.size,
            "id": self.identifier,
            "a": self.a.tolist(),
            "b": self.b.tolist(),
            "x": self.x.tolist(),
            "time": self.time,
        }
        return json.dumps(class_info)

    @classmethod
    def from_json(cls, task_info_json: str) -> "Task":
        task_info = json.loads(task_info_json)
        return Task(
            task_info.get("id"),
            task_info.get("size"),
            task_info.get("a"),
            task_info.get("b"),
            task_info.get("x"),
            task_info.get("time"),
        )

    def __eq__(self, other_task: "Task") -> bool:
        if not isinstance(other_task, Task):
            return False
        elif self.identifier != other_task.identifier:
            return False
        elif self.size != other_task.size:
            return False
        elif not np.array_equal(self.a, other_task.a):
            print(self.a)
            print(other_task.a)
            return False
        elif not np.array_equal(self.b, other_task.b):
            return False
        elif not np.array_equal(self.x, other_task.x):
            return False
        else:
            return True


if __name__ == "__main__":
    ma_tache = Task(0, 3)
    # print(ma_tache.to_json())
    # print(ma_tache.work())
    json_tache = ma_tache.to_json()
    deuxieme_tache = Task.from_json(json_tache)
    # print(deuxieme_tache.work())
    # print(ma_tache.work())
    print(ma_tache == deuxieme_tache)
