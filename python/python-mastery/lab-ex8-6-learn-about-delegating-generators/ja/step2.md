# ソケットのラッピング

前の演習では、ジェネレータを使って簡単なネットワークエコーサーバを書きました。サーバのコードはこのようになっていました：

```python
def tcp_server(address, handler):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        yield'recv', sock
        client, addr = sock.accept()
        tasks.append(handler(client, addr))

def echo_handler(client, address):
    print('Connection from', address)
    while True:
        yield'recv', client
        data = client.recv(1000)
        if not data:
            break
        yield'send', client
        client.send(b'GOT:', data)
    print('Connection closed')
```

`yield` 文を整理し、サーバを次のようにもっと簡単に書き直せるようにする `GenSocket` クラスを作成します：

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
        yield from client.send(b'GOT:', data)
    print('Connection closed')
```
