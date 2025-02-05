# 包装套接字

在前一个练习中，你使用生成器编写了一个简单的网络回显服务器。服务器的代码如下所示：

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
    print('来自', address, '的连接')
    while True:
        yield'recv', client
        data = client.recv(1000)
        if not data:
            break
        yield'send', client
        client.send(b'GOT:', data)
    print('连接已关闭')
```

创建一个 `GenSocket` 类，清理 `yield` 语句，并允许将服务器更简单地重写如下：

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
    print('来自', address, '的连接')
    while True:
        data = yield from client.recv(1000)
        if not data:
            break
        yield from client.send(b'GOT:', data)
    print('连接已关闭')
```
