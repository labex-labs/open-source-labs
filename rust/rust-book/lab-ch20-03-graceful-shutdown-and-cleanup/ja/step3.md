# スレッドに対してジョブの受信を停止するように信号を送る

これまでに行ったすべての変更により、コードは警告なしでコンパイルされます。しかし、残念なことに、このコードはまだ私たちが望むように機能しません。鍵は、`Worker`インスタンスのスレッドによって実行されるクロージャ内のロジックにあります。現在のところ、`join`を呼び出していますが、これではスレッドが停止しません。なぜなら、ジョブを探し続けるために永久に`loop`しているからです。現在の`drop`の実装で`ThreadPool`を破棄しようとすると、メインスレッドは最初のスレッドが終了するのを永久に待ち、ブロックされます。

この問題を解決するには、`ThreadPool`の`drop`実装を変更し、その後`Worker`のループを変更する必要があります。

まず、`ThreadPool`の`drop`実装を変更して、スレッドが終了するのを待つ前に明示的に`sender`を破棄します。リスト20-23は、`sender`を明示的に破棄するための`ThreadPool`の変更を示しています。スレッドと同じ`Option`と`take`テクニックを使用して、`sender`を`ThreadPool`から移動させることができます。

ファイル名: `src/lib.rs`

```rust
pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: Option<mpsc::Sender<Job>>,
}
--snip--
impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        --snip--

        ThreadPool {
            workers,
            sender: Some(sender),
        }
    }

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
        let job = Box::new(f);

        self.sender
           .as_ref()
           .unwrap()
           .send(job)
           .unwrap();
    }
}

impl Drop for ThreadPool {
    fn drop(&mut self) {
      1 drop(self.sender.take());

        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

            if let Some(thread) = worker.thread.take() {
                thread.join().unwrap();
            }
        }
    }
}
```

リスト20-23: `Worker`スレッドにjoinする前に`sender`を明示的に破棄する

`sender`を破棄することで\[1\]、チャネルが閉じられ、これはもうメッセージが送信されないことを示します。そのとき、`Worker`インスタンスが無限ループで行うすべての`recv`の呼び出しはエラーを返します。リスト20-24では、その場合にループをグレースフルに終了するように`Worker`のループを変更します。これは、`ThreadPool`の`drop`実装が`join`を呼び出すときに、スレッドが終了することを意味します。

ファイル名: `src/lib.rs`

```rust
impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || loop {
            let message = receiver.lock().unwrap().recv();

            match message {
                Ok(job) => {
                    println!(
                        "Worker {id} got a job; executing."
                    );

                    job();
                }
                Err(_) => {
                    println!(
                        "Worker {id} shutting down."
                    );
                    break;
                }
            }
        });

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```

リスト20-24: `recv`がエラーを返すときに明示的にループから抜ける

このコードを動作させるには、`main`を変更して、サーバーをグレースフルにシャットダウンする前に2つの要求のみを受け付けるようにします。これは、リスト20-25に示されています。

ファイル名: `src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    let pool = ThreadPool::new(4);

    for stream in listener.incoming().take(2) {
        let stream = stream.unwrap();

        pool.execute(|| {
            handle_connection(stream);
        });
    }

    println!("Shutting down.");
}
```

リスト20-25: ループを抜けることで2つの要求を処理した後にサーバーをシャットダウンする

本当の世界のウェブサーバーは、2つの要求を処理した後にシャットダウンすることは望ましくありません。このコードは、グレースフルなシャットダウンとクリーンアップが機能していることを示すだけです。

`take`メソッドは`Iterator`トレイトに定義されており、反復処理を最大2つの最初の項目に制限します。`ThreadPool`は`main`の末尾でスコープ外になり、`drop`実装が実行されます。

`cargo run`でサーバーを起動し、3つの要求を行ってみましょう。3番目の要求はエラーになり、ターミナルには以下のような出力が表示されるはずです。

```bash
$ cargo run
   Compiling hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 1.0s
     Running `target/debug/hello`
Worker 0 got a job; executing.
Shutting down.
Shutting down worker 0
Worker 3 got a job; executing.
Worker 1 disconnected; shutting down.
Worker 2 disconnected; shutting down.
Worker 3 disconnected; shutting down.
Worker 0 disconnected; shutting down.
Shutting down worker 1
Shutting down worker 2
Shutting down worker 3
```

`Worker`のIDと表示されるメッセージの順序は異なる場合があります。このコードがどのように機能するかは、メッセージからわかります。`Worker`インスタンス0と3が最初の2つの要求を受け取りました。2番目の接続後、サーバーは接続を受け付けなくなり、`ThreadPool`の`Drop`実装は`Worker` 3が作業を開始する前に実行され始めます。`sender`を破棄することで、すべての`Worker`インスタンスが切断され、シャットダウンするように指示されます。`Worker`インスタンスはそれぞれ切断するときにメッセージを出力し、その後、スレッドプールは各`Worker`スレッドが終了するのを待つために`join`を呼び出します。

この特定の実行の興味深い点に注意してください。`ThreadPool`は`sender`を破棄し、どの`Worker`もエラーを受け取る前に、`Worker` 0に`join`を試みました。`Worker` 0はまだ`recv`からエラーを受け取っていなかったので、メインスレッドは`Worker` 0が終了するのを待ってブロックされました。その間、`Worker` 3はジョブを受け取り、その後すべてのスレッドはエラーを受け取りました。`Worker` 0が終了すると、メインスレッドは残りの`Worker`インスタンスが終了するのを待ちました。その時点で、すべてのインスタンスはループを抜け、停止しました。

おめでとうございます！これでプロジェクトが完了しました。非同期で応答するためにスレッドプールを使用する基本的なウェブサーバーができました。サーバーのグレースフルなシャットダウンができ、プール内のすべてのスレッドがクリーンアップされます。この章のコード全体をダウンロードするには、*https://www.nostarch.com/Rust2021*を参照してください。

ここではもっとできます！このプロジェクトをさらに強化したい場合は、以下のアイデアがあります。

- `ThreadPool`とその公開メソッドに追加のドキュメントを追加する。
- ライブラリの機能のテストを追加する。
- `unwrap`への呼び出しを、より堅牢なエラー処理に変更する。
- ウェブ要求を処理する以外のタスクを実行するために`ThreadPool`を使用する。
- *https://crates.io*でスレッドプールのクレートを見つけ、そのクレートを使用して同様のウェブサーバーを実装する。その後、実装したスレッドプールとのAPIと堅牢性を比較する。
