# Wrapping Sockets with Generators

In this step, we're going to learn how to use generators to wrap socket operations. This is a really important concept, especially when it comes to asynchronous programming. Asynchronous programming allows your program to handle multiple tasks at once without waiting for one task to finish before starting another. Using generators to wrap socket operations can make your code more efficient and easier to manage.

## Understanding the Problem

The `server.py` file contains a simple network server implementation using generators. Let's take a look at the current code. This code is the foundation of our server, and understanding it is crucial before we make any changes.

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

In this code, we use the `yield` keyword. The `yield` keyword is used in Python to create generators. A generator is a special type of iterator that allows you to pause and resume a function's execution. Here, `yield` is used to indicate when the server is ready to receive a connection or when a client handler is ready to receive or send data. However, the manual `yield` statements expose the internal workings of the event loop to the user. This means that the user has to know how the event loop works, which can make the code harder to understand and maintain.

## Creating a GenSocket Class

Let's create a `GenSocket` class to wrap socket operations with generators. This will make our code cleaner and more readable. By encapsulating the socket operations in a class, we can hide the details of the event loop from the user and focus on the high-level logic of the server.

1. Open the `server.py` file in the editor:

```bash
cd /home/labex/project
```

This command changes the current directory to the project directory where the `server.py` file is located. Once you're in the correct directory, you can open the file in your preferred text editor.

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

This `GenSocket` class acts as a wrapper for socket operations. The `__init__` method initializes the class with a socket object. The `accept`, `recv`, and `send` methods perform the corresponding socket operations and use `yield` to indicate when the operation is ready. The `__getattr__` method allows the class to forward any other attributes to the underlying socket object.

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

Notice how the explicit `yield 'recv', sock` and `yield 'send', client` statements have been replaced with cleaner `yield from` expressions. The `yield from` keyword is used to delegate the execution to another generator. This makes the code more readable and hides the details of the event loop from the user. Now, the code looks more like normal function calls, and the user doesn't have to worry about the internal workings of the event loop.

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

This code is more readable and maintainable. The `GenSocket` class encapsulates the yielding logic, allowing the server code to focus on the high-level flow rather than the details of the event loop. The `run_server` function starts the server on port 25000 and handles the `KeyboardInterrupt` exception, which allows the user to stop the server by pressing `Ctrl+C`.

## Understanding the Benefits

The `yield from` approach provides several benefits:

1. **Cleaner code**: The socket operations look more like normal function calls. This makes the code easier to read and understand, especially for beginners.
2. **Abstraction**: The details of the event loop are hidden from the user. The user doesn't have to know how the event loop works to use the server code.
3. **Readability**: The code better expresses what it's doing rather than how it's doing it. This makes the code more self-explanatory and easier to maintain.
4. **Maintainability**: Changes to the event loop won't require changes to the server code. This means that if you need to modify the event loop in the future, you can do so without affecting the server code.

This pattern is a stepping stone to modern async/await syntax, which we'll explore in the next step. The async/await syntax is a more advanced and cleaner way to write asynchronous code in Python, and understanding the `yield from` pattern will help you transition to it more easily.
