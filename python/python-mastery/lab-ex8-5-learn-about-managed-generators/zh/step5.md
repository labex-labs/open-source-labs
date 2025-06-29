# 实现一个回显服务器

现在，我们要在 `server.py` 文件中添加回显服务器的实现代码。回显服务器是一种简单地将从客户端接收到的任何数据原样返回的服务器。这是理解服务器如何处理传入数据并与客户端进行通信的绝佳方式。

在 `server.py` 文件的末尾添加以下代码。这段代码将设置我们的回显服务器并处理客户端连接。

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

让我们逐步理解这段代码：

1. `tcp_server` 函数：
   - 首先，它设置一个套接字来监听传入的连接。套接字是两台机器之间通信的端点。
   - 然后，它使用 `yield 'recv', sock` 暂停函数，直到有客户端连接。这是我们异步方法的关键部分。
   - 最后，它为每个客户端连接创建一个新的处理任务。这使得服务器能够并发处理多个客户端。

2. `echo_handler` 函数：
   - 它使用 `yield 'recv', client` 等待客户端发送数据。这会暂停函数，直到有数据可用。
   - 它使用 `yield 'send', client` 等待直到可以将数据发送回客户端。这确保客户端已准备好接收数据。
   - 它处理客户端数据，直到客户端关闭连接。

3. 当我们运行服务器时，它会将 `tcp_server` 任务添加到队列中并启动调度器。调度器负责管理所有任务，并确保它们异步运行。

要测试服务器，在一个终端中运行以下命令：

```bash
python3 /home/labex/project/server.py
```

你应该会看到一条消息，表明服务器正在运行。这意味着服务器现在正在监听传入的连接。

打开另一个终端，使用 `nc`（netcat）连接到服务器。Netcat 是一个简单的实用工具，允许你连接到服务器并发送数据。

```bash
nc localhost 25000
```

现在你可以输入消息，并看到它们以 "GOT:" 为前缀被原样返回：

```
Hello
GOT:Hello
World
GOT:World
```

如果你没有安装 `nc`，可以使用 Python 内置的 `telnetlib`。Telnetlib 是一个允许你使用 Telnet 协议连接到服务器的库。

```bash
python3 -c "import telnetlib; t = telnetlib.Telnet('localhost', 25000); t.interact()"
```

你可以打开多个终端窗口，同时连接多个客户端。尽管服务器是单线程的，但它可以并发处理所有连接。这要归功于我们基于生成器的任务调度器，它允许服务器根据需要暂停和恢复任务。

## 工作原理

这个示例展示了生成器在异步 I/O 中的强大应用：

1. 服务器在等待 I/O 时会产生（yield）。这意味着服务器不会无限期地等待数据，而是可以暂停并让其他任务运行。
2. 调度器将其移动到等待区域，直到 I/O 准备好。这确保服务器不会在等待 I/O 时浪费资源。
3. 在等待 I/O 完成时，其他任务可以运行。这使得服务器能够并发处理多个任务。
4. 当 I/O 准备好时，任务从暂停处继续执行。这是异步编程的一个关键特性。

这种模式构成了现代异步 Python 框架（如 `asyncio`）的基础，`asyncio` 在 Python 3.4 中被添加到 Python 标准库中。
