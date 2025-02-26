# Async/Await

Возьмите класс `GenSocket`, который вы только что написали, и оберните все методы, которые используют `yield`, декоратором `@coroutine` из модуля `types`.

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

Теперь перепишите код сервера, чтобы использовать `async` функции и `await` выражения, как показано ниже:

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
    print('Connection from', address)
    while True:
        data = await client.recv(1000)
        if not data:
            break
        await client.send(b'GOT:', data)
    print('Connection closed')
```
