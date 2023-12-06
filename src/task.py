#!/usr/bin/env python3
from time import perf_counter

import numpy as np


class Task:
    def __init__(self, indentifier: int, size: int):
        self.indentifier = indentifier
        self.size = size
        self.a = np.random.rand(size, size)
        self.b = np.random.rand(
            size,
        )
        self.x = np.zeros((size,))
        self.time = 0.0

    def work(self) -> float:
        time_start = perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        time_end = perf_counter()
        self.time = time_end - time_start
        return self.time


if __name__ == "__main__":
    ma_tache = Task(0, 3)
    print(ma_tache.work())
