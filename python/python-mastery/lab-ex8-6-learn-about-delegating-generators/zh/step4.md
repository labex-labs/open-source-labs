# 从生成器到 `async`/`await`

在这最后一步中，我们将探索 Python 中的 `yield from` 模式是如何演变成现代的 `async`/`await` 语法的。理解这一演变过程至关重要，因为它能帮助你看清生成器与异步编程之间的联系。异步编程允许你的程序在不等待每个任务完成的情况下处理多个任务，这在网络编程和其他 I/O 密集型操作中尤为有用。

## 生成器与 `async`/`await` 的联系

Python 3.5 引入的 `async`/`await` 语法是建立在生成器和 `yield from` 功能之上的。实际上，`async` 函数是使用生成器实现的。这意味着你所学的关于生成器的概念与 `async`/`await` 的工作原理直接相关。

要从使用生成器过渡到 `async`/`await` 语法，需要遵循以下步骤：

1. 使用 `types` 模块中的 `@coroutine` 装饰器。这个装饰器有助于将基于生成器的函数转换为可与 `async`/`await` 一起使用的形式。
2. 将使用 `yield from` 的函数转换为使用 `async` 和 `await`。这会使代码更易读，并更好地体现操作的异步性质。
3. 更新事件循环以处理原生协程。事件循环负责调度和运行异步任务。

## 更新 `GenSocket` 类

现在，让我们修改 `GenSocket` 类，使其能与 `@coroutine` 装饰器一起使用。这样，我们的类就可以在 `async`/`await` 上下文中使用了。

1. 在编辑器中打开 `server.py` 文件。你可以在终端中运行以下命令来实现：

```bash
cd /home/labex/project
```

2. 在 `server.py` 文件的顶部，添加对 `coroutine` 的导入。要使用 `@coroutine` 装饰器，这个导入是必需的。

```python
from types import coroutine
```

3. 更新 `GenSocket` 类以使用 `@coroutine` 装饰器。这个装饰器将我们基于生成器的方法转换为可等待的协程，这意味着它们可以与 `await` 关键字一起使用。

```python
class GenSocket:
    """
    A generator-based wrapper for socket operations
    that works with async/await.
    """
    def __init__(self, sock):
        self.sock = sock

    @coroutine
    def accept(self):
        """Accept a connection and return a new GenSocket"""
        yield 'recv', self.sock
        client, addr = self.sock.accept()
        return GenSocket(client), addr

    @coroutine
    def recv(self, maxsize):
        """Receive data from the socket"""
        yield 'recv', self.sock
        return self.sock.recv(maxsize)

    @coroutine
    def send(self, data):
        """Send data to the socket"""
        yield 'send', self.sock
        return self.sock.send(data)

    def __getattr__(self, name):
        """Forward any other attributes to the underlying socket"""
        return getattr(self.sock, name)
```

## 转换为 `async`/`await` 语法

接下来，让我们将服务器代码转换为使用 `async`/`await` 语法。这将使代码更易读，并清晰地体现操作的异步性质。

```python
async def tcp_server(address, handler):
    """
    An asynchronous TCP server using async/await.
    """
    sock = GenSocket(socket(AF_INET, SOCK_STREAM))
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = await sock.accept()
        tasks.append(handler(client, addr))

async def echo_handler(client, address):
    """
    An asynchronous handler for echo clients.
    """
    print('Connection from', address)
    while True:
        data = await client.recv(1000)
        if not data:
            break
        await client.send(b'GOT:' + data)
    print('Connection closed')
    client.close()
```

注意，`yield from` 已被 `await` 取代，并且函数现在使用 `async def` 而不是 `def` 来定义。这一改变使代码更直观、更易理解。

## 理解转换过程

从使用 `yield from` 的生成器过渡到 `async`/`await` 语法，不仅仅是简单的语法更改。它代表了我们对异步编程思考方式的转变。

1. **使用 `yield from` 的生成器**：
   - 使用带有 `yield from` 的生成器时，你需要显式地让出控制权，以表明某个任务已准备好。这意味着你必须手动管理任务何时可以继续执行。
   - 你还需要手动管理任务的调度。这可能很复杂，尤其是在大型程序中。
   - 重点在于控制流的机制，这可能会使代码更难阅读和维护。

2. **`async`/`await` 语法**：
   - 使用 `async`/`await` 语法时，控制权会在 `await` 点隐式让出。这使代码更简洁，因为你不必担心显式地让出控制权。
   - 事件循环会负责任务的调度，因此你不必手动管理。
   - 重点在于程序的逻辑流程，这使代码更易读、更易维护。

这种转变使得异步代码更易读、更易维护，这对于像网络服务器这样的复杂应用尤为重要。

## 现代异步编程

在现代 Python 中，我们通常使用 `asyncio` 模块进行异步编程，而不是自定义事件循环。`asyncio` 模块为许多有用的功能提供了内置支持：

- 并发运行多个协程。这允许你的程序同时处理多个任务。
- 管理网络 I/O。它简化了通过网络发送和接收数据的过程。
- 同步原语。这些有助于你在并发环境中管理对共享资源的访问。
- 任务调度和取消。你可以轻松地安排任务在特定时间运行，并在需要时取消它们。

以下是使用 `asyncio` 实现的服务器示例：

```python
import asyncio

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f'Connection from {addr}')

    while True:
        data = await reader.read(1000)
        if not data:
            break

        writer.write(b'GOT:' + data)
        await writer.drain()

    print('Connection closed')
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_client, 'localhost', 25000
    )

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
```

这段代码实现了与基于生成器的服务器相同的功能，但使用了标准的 `asyncio` 库，该库更健壮且功能更丰富。

## 总结

在这个实验中，你学习了几个重要的概念：

1. `yield from` 语句以及它如何委托给另一个生成器。这是理解生成器工作原理的基本概念。
2. 如何在协程中使用 `yield from` 进行消息传递。这允许你在异步程序的不同部分之间进行通信。
3. 使用生成器包装套接字操作，以使代码更简洁。这使与网络相关的代码更有条理、更易理解。
4. 从生成器到现代 `async`/`await` 语法的过渡。理解这一过渡将帮助你在 Python 中编写更易读、更易维护的异步代码，无论你是直接使用生成器还是现代的 `async`/`await` 语法。
