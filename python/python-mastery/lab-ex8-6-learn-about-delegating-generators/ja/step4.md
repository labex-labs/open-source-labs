# ジェネレーターから async/await へ

この最後のステップでは、Python の `yield from` パターンが現代的な `async`/`await` 構文にどのように進化したかを探ります。この進化を理解することは、ジェネレーターと非同期プログラミングの関係を把握する上で重要です。非同期プログラミングにより、プログラムは各タスクが終了するのを待たずに複数のタスクを処理することができ、これはネットワークプログラミングやその他の I/O バウンド操作で特に有用です。

## ジェネレーターと async/await の関係

Python 3.5 で導入された `async`/`await` 構文は、ジェネレーターと `yield from` 機能を基に構築されています。内部的には、`async` 関数はジェネレーターを使って実装されています。これは、あなたが学んだジェネレーターに関する概念が、`async`/`await` の動作に直接関係していることを意味します。

ジェネレーターの使用から `async`/`await` 構文へ移行するには、以下の手順に従う必要があります。

1. `types` モジュールから `@coroutine` デコレーターを使用します。このデコレーターは、ジェネレーターベースの関数を `async`/`await` で使用できる形式に変換するのに役立ちます。
2. `yield from` を使用する関数を、代わりに `async` と `await` を使用するように変換します。これにより、コードが読みやすくなり、操作の非同期的な性質がより明確に表現されます。
3. イベントループを更新して、ネイティブコルーチンを処理できるようにします。イベントループは、非同期タスクのスケジューリングと実行を担当します。

## GenSocket クラスの更新

では、`GenSocket` クラスを `@coroutine` デコレーターと共に動作するように変更しましょう。これにより、クラスを `async`/`await` コンテキストで使用できるようになります。

1. エディタで `server.py` ファイルを開きます。ターミナルで次のコマンドを実行することで、これを行うことができます。

```bash
cd /home/labex/project
```

2. `server.py` ファイルの先頭に、`coroutine` のインポートを追加します。このインポートは、`@coroutine` デコレーターを使用するために必要です。

```python
from types import coroutine
```

3. `GenSocket` クラスを更新して、`@coroutine` デコレーターを使用するようにします。このデコレーターは、ジェネレーターベースのメソッドを `await` 可能なコルーチンに変換します。つまり、`await` キーワードと共に使用できるようになります。

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

## async/await 構文への変換

次に、サーバーコードを `async`/`await` 構文を使用するように変換しましょう。これにより、コードが読みやすくなり、操作の非同期的な性質が明確に表現されます。

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

`yield from` が `await` に置き換えられ、関数が `def` ではなく `async def` で定義されていることに注意してください。この変更により、コードがより直感的で理解しやすくなります。

## 変換の理解

`yield from` を使ったジェネレーターから `async`/`await` 構文への移行は、単なる構文の変更ではありません。これは、非同期プログラミングに対する考え方の変化を表しています。

1. **yield from を使ったジェネレーター**：

   - `yield from` を使ったジェネレーターを使用する場合、タスクが準備できたことを信号するために明示的に制御を `yield` します。これは、タスクがいつ続行できるかを手動で管理する必要があることを意味します。
   - タスクのスケジューリングも手動で管理する必要があります。これは、特に大規模なプログラムでは複雑になる可能性があります。
   - 制御フローの仕組みに焦点が当てられており、これによりコードの読み取りと保守が難しくなる可能性があります。

2. **async/await 構文**：
   - `async`/`await` 構文では、`await` ポイントで暗黙的に制御が `yield` されます。これにより、明示的に制御を `yield` することを心配する必要がなくなり、コードがよりシンプルになります。
   - イベントループがタスクのスケジューリングを処理するため、手動で管理する必要はありません。
   - プログラムの論理的な流れに焦点が当てられており、これによりコードが読みやすく保守しやすくなります。

この変換により、より読みやすく保守しやすい非同期コードが可能になり、これはネットワークサーバーのような複雑なアプリケーションに特に重要です。

## 現代的な非同期プログラミング

現代の Python では、通常、カスタムイベントループではなく `asyncio` モジュールを非同期プログラミングに使用します。`asyncio` モジュールは、多くの有用な機能を組み込みでサポートしています。

- 複数のコルーチンを同時に実行すること。これにより、プログラムは複数のタスクを同時に処理することができます。
- ネットワーク I/O の管理。ネットワークを介したデータの送受信プロセスを簡素化します。
- 同期プリミティブ。これらは、並行環境で共有リソースへのアクセスを管理するのに役立ちます。
- タスクのスケジューリングとキャンセル。特定の時間にタスクを実行するように簡単にスケジューリングでき、必要に応じてキャンセルすることもできます。

以下は、`asyncio` を使用した場合のサーバーの例です。

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

このコードは、ジェネレーターベースのサーバーと同じ機能を実現していますが、より堅牢で機能豊富な標準の `asyncio` ライブラリを使用しています。

## まとめ

この実験では、いくつかの重要な概念を学びました。

1. `yield from` 文と、それが別のジェネレーターに委任する方法。これは、ジェネレーターの動作を理解する上で基本的な概念です。
2. コルーチンと共に `yield from` を使用してメッセージを受け渡す方法。これにより、非同期プログラムの異なる部分間で通信することができます。
3. ジェネレーターを使ってソケット操作をラッピングし、コードをクリーンにする方法。これにより、ネットワーク関連のコードがより整理され、理解しやすくなります。
4. ジェネレーターから現代的な `async`/`await` 構文への移行。この移行を理解することで、ジェネレーターを直接使用する場合でも、現代的な `async`/`await` 構文を使用する場合でも、Python でより読みやすく保守しやすい非同期コードを書くことができます。
