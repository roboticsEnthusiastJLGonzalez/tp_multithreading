# TP MULTITHREADING

## Goal of this TP
Introduce us to the use of multithreding. We have several tasks to perform and we want to distribute the calculation between different threads. 

We use a Python part to run the QueueManager, a boss that creates tasks and puts them in the queue, and minions that take a task from the queue and carry it out.

A proxy is used to retrieve a json file describing a pending task.

C++ code can formulate HTTP requests to retrieve a task in Json format from the queue of the QueueManager and execute it.

We compare the performance of python and c++ for task calculation.

## Run the python scripts
When in the repo `tp_multithreading/`, go in `src/`. Then, run the queue manager
```
python3 manager.py 
``` 
Then in a new terminal, run the proxy.
```
python3 proxy.py
```
You can now add tasks to the queue when calling a boss (in a new terminal) : 
```
python3 boss.py
```
When you call minions, they will do all the tasks in the queue:
```
python3 minion.py
```

## Run the C++ programm
This programm will send an http request and wait for its response. If a task is posted in the queue, the the C++ programm will take it from the queue and compute it.
When in the repo `tp_multithreading/` first build the project (in release mode) using:
```
cmake -B build-rel -S . -DCMAKE_BUILD_TYPE=Release
```
Then:
```
cmake --build build-rel/
```
Now you can run the executable:
```
./build-rel/low_level 
```
