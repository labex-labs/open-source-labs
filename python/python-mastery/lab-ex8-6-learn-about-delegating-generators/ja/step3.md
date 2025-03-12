# ジェネレーターを使ったソケットのラッピング

このステップでは、ジェネレーターを使ってソケット操作をラッピングする方法を学びます。これは非常に重要な概念であり、特に非同期プログラミングに関係しています。非同期プログラミングにより、プログラムはあるタスクが終了するのを待たずに複数のタスクを同時に処理することができます。ジェネレーターを使ってソケット操作をラッピングすることで、コードをより効率的かつ管理しやすくすることができます。

## 問題の理解

`server.py` ファイルには、ジェネレーターを使ったシンプルなネットワークサーバーの実装が含まれています。現在のコードを見てみましょう。このコードはサーバーの基礎であり、何か変更を加える前に理解することが重要です。

```python
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
    client.close()
```

このコードでは、`yield` キーワードを使用しています。`yield` キーワードは Python でジェネレーターを作成するために使用されます。ジェネレーターは、関数の実行を一時停止したり再開したりできる特殊なタイプのイテレーターです。ここでは、`yield` はサーバーが接続を受け入れる準備ができたとき、またはクライアントハンドラーがデータを受信または送信する準備ができたときを示すために使用されています。しかし、手動の `yield` 文はイベントループの内部動作をユーザーに公開しています。これは、ユーザーがイベントループの動作を知っている必要があり、コードの理解と保守が難しくなることを意味します。

## GenSocket クラスの作成

ジェネレーターを使ってソケット操作をラッピングする `GenSocket` クラスを作成しましょう。これにより、コードがクリーンで読みやすくなります。ソケット操作をクラスにカプセル化することで、イベントループの詳細をユーザーから隠し、サーバーの高レベルなロジックに集中することができます。

1. エディタで `server.py` ファイルを開きます。

```bash
cd /home/labex/project
```

このコマンドは、カレントディレクトリを `server.py` ファイルがあるプロジェクトディレクトリに変更します。正しいディレクトリに移動したら、好みのテキストエディタでファイルを開くことができます。

2. 既存の関数の前に、ファイルの末尾に次の `GenSocket` クラスを追加します。

```python
class GenSocket:
    """
    A generator-based wrapper for socket operations.
    """
    def __init__(self, sock):
        self.sock = sock

    def accept(self):
        """Accept a connection and return a new GenSocket"""
        yield 'recv', self.sock
        client, addr = self.sock.accept()
        return GenSocket(client), addr

    def recv(self, maxsize):
        """Receive data from the socket"""
        yield 'recv', self.sock
        return self.sock.recv(maxsize)

    def send(self, data):
        """Send data to the socket"""
        yield 'send', self.sock
        return self.sock.send(data)

    def __getattr__(self, name):
        """Forward any other attributes to the underlying socket"""
        return getattr(self.sock, name)
```

この `GenSocket` クラスは、ソケット操作のラッパーとして機能します。`__init__` メソッドは、ソケットオブジェクトでクラスを初期化します。`accept`、`recv`、および `send` メソッドは、対応するソケット操作を実行し、操作が準備できたときを示すために `yield` を使用します。`__getattr__` メソッドは、他の属性を基になるソケットオブジェクトに転送することを可能にします。

3. これで、`tcp_server` および `echo_handler` 関数を `GenSocket` クラスを使用するように変更しましょう。

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
        yield from client.send(b'GOT:' + data)
    print('Connection closed')
    client.close()
```

明示的な `yield 'recv', sock` および `yield 'send', client` 文が、よりクリーンな `yield from` 式に置き換えられたことに注意してください。`yield from` キーワードは、実行を別のジェネレーターに委任するために使用されます。これにより、コードが読みやすくなり、イベントループの詳細がユーザーから隠されます。今では、コードは通常の関数呼び出しのように見え、ユーザーはイベントループの内部動作を心配する必要がありません。

4. サーバーの使用方法を示すために、簡単なテスト関数を追加しましょう。

```python
def run_server():
    """Start the server on port 25000"""
    tasks.append(tcp_server(('localhost', 25000), echo_handler))
    try:
        event_loop()
    except KeyboardInterrupt:
        print("Server stopped")

if __name__ == '__main__':
    print("Starting echo server on port 25000...")
    print("Press Ctrl+C to stop")
    run_server()
```

このコードは、より読みやすく保守しやすくなっています。`GenSocket` クラスは `yield` ロジックをカプセル化し、サーバーコードがイベントループの詳細ではなく高レベルな流れに集中できるようにします。`run_server` 関数は、ポート 25000 でサーバーを起動し、`KeyboardInterrupt` 例外を処理します。これにより、ユーザーは `Ctrl+C` を押すことでサーバーを停止することができます。

## 利点の理解

`yield from` アプローチにはいくつかの利点があります。

1. **クリーンなコード**：ソケット操作は通常の関数呼び出しのように見えます。これにより、特に初心者にとってコードが読みやすく理解しやすくなります。
2. **抽象化**：イベントループの詳細がユーザーから隠されています。ユーザーはサーバーコードを使用するためにイベントループの動作を知る必要はありません。
3. **可読性**：コードは何をしているかを表現するのに重点が置かれており、どのようにしているかではなくなっています。これにより、コードが自己説明的になり、保守が容易になります。
4. **保守性**：イベントループに変更を加えても、サーバーコードを変更する必要はありません。これは、将来イベントループを変更する必要がある場合、サーバーコードに影響を与えることなく行うことができることを意味します。

このパターンは、次のステップで探る現代的な `async/await` 構文への足がかりとなります。`async/await` 構文は、Python で非同期コードを書くためのより高度でクリーンな方法であり、`yield from` パターンを理解することで、より簡単に移行することができます。
