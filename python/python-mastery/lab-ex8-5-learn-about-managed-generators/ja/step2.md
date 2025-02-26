# ネットワーク接続を提供するタスクとしてのジェネレータ

`server.py` というファイルに、次のコードを入力します。

```python
# server.py

from socket import *
from select import select
from collections import deque

tasks = deque()
recv_wait = {}   #  sock -> task
send_wait = {}   #  sock -> task

def run():
    while any([tasks, recv_wait, send_wait]):
        while not tasks:
            can_recv, can_send, _ = select(recv_wait, send_wait, [])
            for s in can_recv:
                tasks.append(recv_wait.pop(s))
            for s in can_send:
                tasks.append(send_wait.pop(s))
        task = tasks.popleft()
        try:
            reason, resource = task.send(None)
            if reason == 'recv':
                recv_wait[resource] = task
            elif reason == 'send':
                send_wait[resource] = task
            else:
                raise RuntimeError('Unknown reason %r' % reason)
        except StopIteration:
            print('Task done')
```

このコードは、(a)のタスクスケジューラのやや複雑なバージョンです。少し勉強が必要ですが、その考え方は、各タスクがyieldするだけでなく、その理由（受信または送信）を示すことです。理由に応じて、タスクは待機エリアに移動します。その後、スケジューラは利用可能なタスクを実行するか、何もすることがなくなったときにI/Oイベントが発生するのを待ちます。

多分少々難しいかもしれませんが、次のコードを追加してください。これは簡単なエコーサーバを実装しています。

```python
# server.py
...

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

if __name__ == '__main__':
    tasks.append(tcp_server(('',25000), echo_handler))
    run()
```

このサーバを独自のターミナルウィンドウで実行します。別のターミナルで、`telnet` や `nc` などのコマンドを使って接続します。たとえば：

```bash
nc localhost 25000
Hello
Got: Hello
World
Got: World
```

`nc` や `telnet` にアクセスできない場合は、Python自体を使うこともできます。

```bash
python3 -m telnetlib localhost 25000
Hello
Got: Hello
World
Got: World
```

正常に動作していれば、出力がエコーバックされるはずです。それだけでなく、複数のクライアントを接続すると、すべてが同時に動作します。

このようなジェネレータの難しい使い方は、直接コードを書く必要があることはありません。ただし、Python 3.4で標準ライブラリに追加された `asyncio` などの特定の高度なパッケージでは使用されています。
