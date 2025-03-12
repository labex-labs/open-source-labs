# Building a Network Server with Generators

Now let's extend our task scheduler concept to build something more practical: a simple network server that can handle multiple client connections concurrently using generators.

Create a new file called `server.py` in the `/home/labex/project` directory:

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

This enhanced scheduler is more complex, but follows the same basic principles as our earlier one. The main differences are:

1. Tasks can yield a reason ('recv' or 'send') and a resource (a socket)
2. Based on the yield reason, the task is moved to a different waiting area
3. The `select()` function is used to determine which sockets are ready for I/O
4. When a socket is ready, its associated task is moved back to the active queue

This allows our tasks to efficiently wait for network I/O without blocking.
