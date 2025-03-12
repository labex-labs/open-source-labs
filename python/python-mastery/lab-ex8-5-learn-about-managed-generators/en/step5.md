# Implementing an Echo Server

Now let's add the echo server implementation to our `server.py` file. Add the following code at the end of the file:

```python
# TCP Server implementation
def tcp_server(address, handler):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)

    while True:
        yield 'recv', sock        # Wait for a client connection
        client, addr = sock.accept()
        tasks.append(handler(client, addr))  # Start a handler task for this client

# Echo handler - echoes back whatever the client sends
def echo_handler(client, address):
    print('Connection from', address)

    while True:
        yield 'recv', client      # Wait until client sends data
        data = client.recv(1000)

        if not data:              # Client closed connection
            break

        yield 'send', client      # Wait until client can receive data
        client.send(b'GOT:' + data)

    print('Connection closed')
    client.close()

# Start the server
if __name__ == '__main__':
    tasks.append(tcp_server(('', 25000), echo_handler))
    run()
```

Let's understand this code:

1. The `tcp_server` function:

   - Sets up a socket to listen for connections
   - Uses `yield 'recv', sock` to pause until a client connects
   - Creates a new handler task for each client connection

2. The `echo_handler` function:

   - Yields `'recv', client` to wait for client data
   - Yields `'send', client` to wait until it can send data back
   - Processes client data until the connection closes

3. When we run the server, it adds the `tcp_server` task to the queue and starts the scheduler

To test the server, run it in one terminal:

```bash
python3 /home/labex/project/server.py
```

You should see a message indicating the server is running.

Open another terminal and connect to the server using `nc` (netcat):

```bash
nc localhost 25000
```

Now you can type messages and see them echoed back with "GOT:" prefixed:

```
Hello
GOT:Hello
World
GOT:World
```

If you don't have `nc` installed, you can use Python's built-in `telnetlib`:

```bash
python3 -c "import telnetlib; t = telnetlib.Telnet('localhost', 25000); t.interact()"
```

You can open multiple terminal windows and connect multiple clients simultaneously. The server will handle all connections concurrently, despite being single-threaded, thanks to our generator-based task scheduler.

## How It Works

This example demonstrates a powerful application of generators for async I/O:

1. The server yields when it would otherwise block waiting for I/O
2. The scheduler moves it to a waiting area until the I/O is ready
3. Other tasks can run while waiting for I/O to complete
4. When I/O is ready, the task continues from where it left off

This pattern forms the foundation of modern asynchronous Python frameworks like `asyncio`, which was added to the Python standard library in Python 3.4.
