#!/bin/bash

# Create the project directory structure
mkdir -p /home/labex/project
cd /home/labex/project

# Create the initial cofollow.py file
cat > cofollow.py << 'EOF'
# cofollow.py - Coroutine utility functions

def consumer(func):
    """
    Decorator that makes a coroutine function automatically advance to first yield
    """
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)  # Advance to first yield
        return cr
    return start

# Example coroutine
@consumer
def printer():
    while True:
        item = yield
        print('Got:', item)
EOF

# Create the server.py file
cat > server.py << 'EOF'
# server.py - Coroutine-based socket server

from socket import *
import select

# List to hold all active tasks
tasks = []

# Server implementation using generators
def tcp_server(address, handler):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        yield 'recv', sock
        client, addr = sock.accept()
        tasks.append(handler(client, addr))

def echo_handler(client, address):
    print('Connection from', address)
    while True:
        yield 'recv', client
        data = client.recv(1000)
        if not data:
            break
        yield 'send', client
        client.send(b'GOT:' + data)
    print('Connection closed')
    client.close()

# Event loop
def event_loop():
    while any(tasks):
        for task in list(tasks):
            try:
                op, target = next(task)
                if op == 'recv':
                    # Check if target is readable
                    r, w, e = select.select([target], [], [], 0)
                    if not r:
                        continue
                elif op == 'send':
                    # Check if target is writable
                    r, w, e = select.select([], [target], [], 0)
                    if not w:
                        continue
                else:
                    raise RuntimeError(f"Unknown operation: {op}")
                # Operation can be performed, reschedule the task
                tasks.append(task)
            except StopIteration:
                # Task is done
                pass
EOF

# Set up Python shell history
cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash
