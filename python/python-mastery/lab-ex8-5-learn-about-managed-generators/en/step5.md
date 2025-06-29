# Implementing an Echo Server

Now, we're going to add the implementation of an echo server to our `server.py` file. An echo server is a type of server that simply sends back whatever data it receives from a client. This is a great way to understand how servers handle incoming data and communicate with clients.

Add the following code at the end of the `server.py` file. This code will set up our echo server and handle client connections.

```python
# TCP Server implementation
def tcp_server(address, handler):
    # Create a TCP socket
    sock = socket(AF_INET, SOCK_STREAM)
    # Set the socket option to reuse the address
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # Bind the socket to the given address
    sock.bind(address)
    # Start listening for incoming connections, with a backlog of 5
    sock.listen(5)

    while True:
        # Yield to pause the function until a client connects
        yield 'recv', sock        # Wait for a client connection
        # Accept a client connection
        client, addr = sock.accept()
        # Add a new handler task for this client to the tasks list
        tasks.append(handler(client, addr))  # Start a handler task for this client

# Echo handler - echoes back whatever the client sends
def echo_handler(client, address):
    print('Connection from', address)

    while True:
        # Yield to pause the function until the client sends data
        yield 'recv', client      # Wait until client sends data
        # Receive up to 1000 bytes of data from the client
        data = client.recv(1000)

        if not data:              # Client closed connection
            break

        # Yield to pause the function until the client can receive data
        yield 'send', client      # Wait until client can receive data
        # Send the data back to the client with 'GOT:' prefix
        client.send(b'GOT:' + data)

    print('Connection closed')
    # Close the client connection
    client.close()

# Start the server
if __name__ == '__main__':
    # Add the tcp_server task to the tasks list
    tasks.append(tcp_server(('', 25000), echo_handler))
    # Start the scheduler
    run()
```

Let's understand this code step by step:

1. The `tcp_server` function:
   - First, it sets up a socket to listen for incoming connections. A socket is an endpoint for communication between two machines.
   - Then, it uses `yield 'recv', sock` to pause the function until a client connects. This is a key part of our asynchronous approach.
   - Finally, it creates a new handler task for each client connection. This allows the server to handle multiple clients concurrently.

2. The `echo_handler` function:
   - It yields `'recv', client` to wait for the client to send data. This pauses the function until data is available.
   - It yields `'send', client` to wait until it can send data back to the client. This ensures that the client is ready to receive the data.
   - It processes the client data until the connection is closed by the client.

3. When we run the server, it adds the `tcp_server` task to the queue and starts the scheduler. The scheduler is responsible for managing all the tasks and making sure they run asynchronously.

To test the server, run it in one terminal:

```bash
python3 /home/labex/project/server.py
```

You should see a message indicating the server is running. This means that the server is now listening for incoming connections.

Open another terminal and connect to the server using `nc` (netcat). Netcat is a simple utility that allows you to connect to a server and send data.

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

If you don't have `nc` installed, you can use Python's built-in `telnetlib`. Telnetlib is a library that allows you to connect to a server using the Telnet protocol.

```bash
python3 -c "import telnetlib; t = telnetlib.Telnet('localhost', 25000); t.interact()"
```

You can open multiple terminal windows and connect multiple clients simultaneously. The server will handle all connections concurrently, despite being single-threaded. This is thanks to our generator-based task scheduler, which allows the server to pause and resume tasks as needed.

## How It Works

This example demonstrates a powerful application of generators for async I/O:

1. The server yields when it would otherwise block waiting for I/O. This means that instead of waiting indefinitely for data, the server can pause and let other tasks run.
2. The scheduler moves it to a waiting area until the I/O is ready. This ensures that the server doesn't waste resources waiting for I/O.
3. Other tasks can run while waiting for I/O to complete. This allows the server to handle multiple tasks concurrently.
4. When I/O is ready, the task continues from where it left off. This is a key feature of asynchronous programming.

This pattern forms the foundation of modern asynchronous Python frameworks like `asyncio`, which was added to the Python standard library in Python 3.4.
