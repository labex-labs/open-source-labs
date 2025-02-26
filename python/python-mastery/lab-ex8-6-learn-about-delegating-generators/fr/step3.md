# Async/Await

Prenez la classe `GenSocket` que vous venez d'écrire et emballez toutes les méthodes qui utilisent `yield` avec le décorateur `@coroutine` du module `types`.

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

Maintenant, réécrivez votre code de serveur pour utiliser des fonctions `async` et des instructions `await` comme ceci :

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
