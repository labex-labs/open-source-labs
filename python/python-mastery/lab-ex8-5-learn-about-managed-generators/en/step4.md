# Building a Network Server with Generators

In this section, we'll take the concept of a task scheduler we've learned and expand it to create something more practical: a simple network server. This server can handle multiple client connections at the same time using generators. Generators are a powerful Python feature that allows functions to pause and resume their execution, which is very useful for handling multiple tasks without blocking.

First, you need to create a new file named `server.py` in the `/home/labex/project` directory. This file will contain the code for our network server.

```python
# server.py

from socket import *
from select import select
from collections import deque

# Task system
tasks = deque()
recv_wait = {}   # Map: socket -> task (for tasks waiting to receive)
send_wait = {}   # Map: socket -> task (for tasks waiting to send)

def run():
    while any([tasks, recv_wait, send_wait]):
        # If no active tasks, wait for I/O
        while not tasks:
            # Wait for any socket to become ready for I/O
            can_recv, can_send, _ = select(recv_wait, send_wait, [])

            # Add tasks waiting on readable sockets back to active queue
            for s in can_recv:
                tasks.append(recv_wait.pop(s))

            # Add tasks waiting on writable sockets back to active queue
            for s in can_send:
                tasks.append(send_wait.pop(s))

        # Get next task to run
        task = tasks.popleft()

        try:
            # Resume the task
            reason, resource = task.send(None)

            # Handle different yield reasons
            if reason == 'recv':
                # Task is waiting to receive data
                recv_wait[resource] = task
            elif reason == 'send':
                # Task is waiting to send data
                send_wait[resource] = task
            else:
                raise RuntimeError('Unknown yield reason %r' % reason)

        except StopIteration:
            print('Task done')
```

This improved scheduler is a bit more complicated than the previous one, but it follows the same fundamental ideas. Let's break down the main differences:

1. Tasks can yield a reason ('recv' or 'send') and a resource (a socket). This means that a task can tell the scheduler that it's waiting to either receive or send data on a specific socket.
2. Depending on the yield reason, the task is moved to a different waiting area. If a task is waiting to receive data, it goes to the `recv_wait` dictionary. If it's waiting to send data, it goes to the `send_wait` dictionary.
3. The `select()` function is used to figure out which sockets are ready for I/O operations. This function checks the sockets in the `recv_wait` and `send_wait` dictionaries and returns the ones that are ready to either receive or send data.
4. When a socket is ready, the associated task is moved back to the active queue. This allows the task to continue its execution and perform the I/O operation it was waiting for.

By using these techniques, our tasks can efficiently wait for network I/O without blocking the execution of other tasks. This makes our network server more responsive and able to handle multiple client connections concurrently.
