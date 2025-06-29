# エコーサーバーの実装

ここでは、`server.py` ファイルにエコーサーバーの実装を追加します。エコーサーバーは、クライアントから受信したデータをそのまま返すタイプのサーバーです。これは、サーバーが受信したデータをどのように処理し、クライアントと通信するかを理解するのに最適な方法です。

`server.py` ファイルの末尾に以下のコードを追加します。このコードは、エコーサーバーをセットアップし、クライアント接続を処理します。

```python
# TCP Server implementation
def tcp_server(address, handler):
    # Create a TCP socket
    sock = socket(AF_INET, SOCK_STREAM)
    # Set the socket option to reuse the address
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # Bind the socket to the given address
    sock.bind(address)
    # Start listening for incoming connections, with a backlog of 5
    sock.listen(5)

    while True:
        # Yield to pause the function until a client connects
        yield 'recv', sock        # Wait for a client connection
        # Accept a client connection
        client, addr = sock.accept()
        # Add a new handler task for this client to the tasks list
        tasks.append(handler(client, addr))  # Start a handler task for this client

# Echo handler - echoes back whatever the client sends
def echo_handler(client, address):
    print('Connection from', address)

    while True:
        # Yield to pause the function until the client sends data
        yield 'recv', client      # Wait until client sends data
        # Receive up to 1000 bytes of data from the client
        data = client.recv(1000)

        if not data:              # Client closed connection
            break

        # Yield to pause the function until the client can receive data
        yield 'send', client      # Wait until client can receive data
        # Send the data back to the client with 'GOT:' prefix
        client.send(b'GOT:' + data)

    print('Connection closed')
    # Close the client connection
    client.close()

# Start the server
if __name__ == '__main__':
    # Add the tcp_server task to the tasks list
    tasks.append(tcp_server(('', 25000), echo_handler))
    # Start the scheduler
    run()
```

このコードを段階的に理解しましょう。

1. `tcp_server` 関数：
   - まず、着信接続を待ち受けるソケットをセットアップします。ソケットは、2 台のマシン間の通信のエンドポイントです。
   - 次に、`yield 'recv', sock` を使用して、クライアントが接続するまで関数を一時停止します。これは、非同期アプローチの重要な部分です。
   - 最後に、各クライアント接続に対して新しいハンドラータスクを作成します。これにより、サーバーは複数のクライアントを同時に処理することができます。

2. `echo_handler` 関数：
   - `'recv', client` を生成（yield）して、クライアントがデータを送信するのを待ちます。これにより、データが利用可能になるまで関数が一時停止します。
   - `'send', client` を生成（yield）して、クライアントにデータを返送できる状態になるまで待ちます。これにより、クライアントがデータを受信できる準備ができていることが保証されます。
   - クライアントが接続を閉じるまで、クライアントデータを処理します。

3. サーバーを実行すると、`tcp_server` タスクがキューに追加され、スケジューラーが起動します。スケジューラーは、すべてのタスクを管理し、非同期で実行されるようにする役割を果たします。

サーバーをテストするには、1 つのターミナルで以下のコマンドを実行します。

```bash
python3 /home/labex/project/server.py
```

サーバーが実行中であることを示すメッセージが表示されるはずです。これは、サーバーが着信接続を待ち受けていることを意味します。

別のターミナルを開き、`nc`（netcat）を使用してサーバーに接続します。Netcat は、サーバーに接続してデータを送信できるシンプルなユーティリティです。

```bash
nc localhost 25000
```

これで、メッセージを入力し、「GOT:」が付加されてエコーバックされるのを確認できます。

```
Hello
GOT:Hello
World
GOT:World
```

`nc` がインストールされていない場合は、Python の組み込みライブラリ `telnetlib` を使用できます。Telnetlib は、Telnet プロトコルを使用してサーバーに接続できるライブラリです。

```bash
python3 -c "import telnetlib; t = telnetlib.Telnet('localhost', 25000); t.interact()"
```

複数のターミナルウィンドウを開き、複数のクライアントを同時に接続することができます。サーバーは単一スレッドであるにもかかわらず、すべての接続を同時に処理します。これは、ジェネレーターベースのタスクスケジューラーのおかげで、サーバーが必要に応じてタスクを一時停止および再開できるためです。

## 動作原理

この例は、非同期 I/O のためのジェネレーターの強力なアプリケーションを示しています。

1. サーバーは、I/O を待ってブロックする場合に生成（yield）します。これは、データを無期限に待つ代わりに、サーバーが一時停止して他のタスクを実行できることを意味します。
2. スケジューラーは、I/O が準備できるまでサーバーを待機領域に移動します。これにより、サーバーが I/O を待ってリソースを浪費しないようになります。
3. I/O が完了するのを待っている間、他のタスクを実行できます。これにより、サーバーは複数のタスクを同時に処理することができます。
4. I/O が準備できたら、タスクは中断したところから続行します。これは、非同期プログラミングの重要な機能です。

このパターンは、Python 3.4 で Python 標準ライブラリに追加された `asyncio` のような、現代の非同期 Python フレームワークの基礎を形成しています。
