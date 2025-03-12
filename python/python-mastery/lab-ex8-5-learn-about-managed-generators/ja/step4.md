# ジェネレーターを使ったネットワークサーバーの構築

このセクションでは、これまで学んだタスクスケジューラーの概念を拡張して、より実用的なもの、つまり簡単なネットワークサーバーを作成します。このサーバーは、ジェネレーターを使って複数のクライアント接続を同時に処理することができます。ジェネレーターは Python の強力な機能で、関数の実行を一時停止し再開することができ、ブロッキングすることなく複数のタスクを処理するのに非常に便利です。

まず、`/home/labex/project` ディレクトリに `server.py` という名前の新しいファイルを作成する必要があります。このファイルには、ネットワークサーバーのコードが含まれます。

```python
# server.py

from socket import *
from select import select
from collections import deque

# Task system
tasks = deque()
recv_wait = {}   # Map: socket -> task (for tasks waiting to receive)
send_wait = {}   # Map: socket -> task (for tasks waiting to send)

def run():
    while any([tasks, recv_wait, send_wait]):
        # If no active tasks, wait for I/O
        while not tasks:
            # Wait for any socket to become ready for I/O
            can_recv, can_send, _ = select(recv_wait, send_wait, [])

            # Add tasks waiting on readable sockets back to active queue
            for s in can_recv:
                tasks.append(recv_wait.pop(s))

            # Add tasks waiting on writable sockets back to active queue
            for s in can_send:
                tasks.append(send_wait.pop(s))

        # Get next task to run
        task = tasks.popleft()

        try:
            # Resume the task
            reason, resource = task.send(None)

            # Handle different yield reasons
            if reason == 'recv':
                # Task is waiting to receive data
                recv_wait[resource] = task
            elif reason == 'send':
                # Task is waiting to send data
                send_wait[resource] = task
            else:
                raise RuntimeError('Unknown yield reason %r' % reason)

        except StopIteration:
            print('Task done')
```

この改良版のスケジューラーは前のものより少し複雑ですが、基本的な考え方は同じです。主な違いを解説しましょう。

1. タスクは理由（'recv' または 'send'）とリソース（ソケット）を生成（yield）することができます。これは、タスクが特定のソケットでデータの受信または送信を待っていることをスケジューラーに伝えることができることを意味します。
2. 生成（yield）された理由に応じて、タスクは異なる待機領域に移動します。タスクがデータの受信を待っている場合は、`recv_wait` 辞書に移動します。データの送信を待っている場合は、`send_wait` 辞書に移動します。
3. `select()` 関数は、どのソケットが I/O 操作の準備ができているかを判断するために使用されます。この関数は、`recv_wait` および `send_wait` 辞書内のソケットをチェックし、データの受信または送信の準備ができているソケットを返します。
4. ソケットが準備できたら、関連するタスクはアクティブキューに戻されます。これにより、タスクは実行を続け、待っていた I/O 操作を実行することができます。

これらの技術を使用することで、タスクは他のタスクの実行をブロッキングすることなく、ネットワーク I/O を効率的に待つことができます。これにより、ネットワークサーバーはより応答性が高く、複数のクライアント接続を同時に処理することができます。
