# Wrapping Sockets with Generators

In this step, you will learn how to use generators to wrap socket operations. This pattern is particularly useful for asynchronous programming.

## Understanding the Problem

The `server.py` file contains a simple network server implementation using generators. Let's examine the current code:

```python
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
```

This code uses `yield` to indicate when the server is ready to receive a connection or when a client handler is ready to receive or send data. This approach works, but the manual `yield` statements expose the internal workings of the event loop to the user.

## Creating a GenSocket Class

Let's create a `GenSocket` class to wrap socket operations with generators, making the code cleaner and more readable:

1. Open the `server.py` file in the editor:

```bash
cd /home/labex/project
```

2. Add the following `GenSocket` class at the end of the file, before any existing functions:

```python
class GenSocket:
    """
    A generator-based wrapper for socket operations.
    """
    def __init__(self, sock):
        self.sock = sock

    def accept(self):
        """Accept a connection and return a new GenSocket"""
        yield 'recv', self.sock
        client, addr = self.sock.accept()
        return GenSocket(client), addr

    def recv(self, maxsize):
        """Receive data from the socket"""
        yield 'recv', self.sock
        return self.sock.recv(maxsize)

    def send(self, data):
        """Send data to the socket"""
        yield 'send', self.sock
        return self.sock.send(data)

    def __getattr__(self, name):
        """Forward any other attributes to the underlying socket"""
        return getattr(self.sock, name)
```

3. Now, modify the `tcp_server` and `echo_handler` functions to use the `GenSocket` class:

```python
def tcp_server(address, handler):
    sock = GenSocket(socket(AF_INET, SOCK_STREAM))
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = yield from sock.accept()
        tasks.append(handler(client, addr))

def echo_handler(client, address):
    print('Connection from', address)
    while True:
        data = yield from client.recv(1000)
        if not data:
            break
        yield from client.send(b'GOT:' + data)
    print('Connection closed')
    client.close()
```

Notice how the explicit `yield 'recv', sock` and `yield 'send', client` statements have been replaced with cleaner `yield from` expressions. This makes the code more readable and hides the details of the event loop from the user.

4. Let's add a simple test function to demonstrate how our server would be used:

```python
def run_server():
    """Start the server on port 25000"""
    tasks.append(tcp_server(('localhost', 25000), echo_handler))
    try:
        event_loop()
    except KeyboardInterrupt:
        print("Server stopped")

if __name__ == '__main__':
    print("Starting echo server on port 25000...")
    print("Press Ctrl+C to stop")
    run_server()
```

This code is more readable and maintainable. The `GenSocket` class encapsulates the yielding logic, allowing the server code to focus on the high-level flow rather than the details of the event loop.

## Understanding the Benefits

The `yield from` approach provides several benefits:

1. **Cleaner code**: The socket operations look more like normal function calls.
2. **Abstraction**: The details of the event loop are hidden from the user.
3. **Readability**: The code better expresses what it's doing rather than how it's doing it.
4. **Maintainability**: Changes to the event loop won't require changes to the server code.

This pattern is a stepping stone to modern async/await syntax, which we'll explore in the next step.
