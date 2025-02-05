# 异步/等待

使用你刚刚编写的 `GenSocket` 类，并使用 `types` 模块中的 `@coroutine` 装饰器来包装所有使用 `yield` 的方法。

```python
from types import coroutine
...

class GenSocket:
    def __init__(self, sock):
        self.sock = sock

    @coroutine
    def accept(self):
        yield'recv', self.sock
        client, addr = self.sock.accept()
        return GenSocket(client), addr

    @coroutine
    def recv(self, maxsize):
        yield'recv', self.sock
        return self.sock.recv(maxsize)

    @coroutine
    def send(self, data):
        yield'send', self.sock
        return self.sock.send(data)

    def __getattr__(self, name):
        return getattr(self.sock, name)
```

现在，将你的服务器代码重写为使用 `async` 函数和 `await` 语句，如下所示：

```python
async def tcp_server(address, handler):
    sock = GenSocket(socket(AF_INET, SOCK_STREAM))
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = await sock.accept()
        tasks.append(handler(client, addr))

async def echo_handler(client, address):
    print('来自', address, '的连接')
    while True:
        data = await client.recv(1000)
        if not data:
            break
        await client.send(b'GOT:', data)
    print('连接已关闭')
```
