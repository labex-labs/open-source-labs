# execute メソッドの実装

さて、ついに `ThreadPool` の `execute` メソッドを実装しましょう。また、`Job` を構造体から、`execute` が受け取るクロージャの型を保持するトレイトオブジェクトの型エイリアスに変更します。「型エイリアスを使った型の同義語の作成」で説明したように、型エイリアスは使いやすさのために長い型を短くすることができます。リスト20-19を見てください。

ファイル名: `src/lib.rs`

```rust
--snip--

type Job = Box<dyn FnOnce() + Send + 'static>;

impl ThreadPool {
    --snip--

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
      1 let job = Box::new(f);

      2 self.sender.send(job).unwrap();
    }
}

--snip--
```

リスト20-19: 各クロージャを保持する `Box` 用の `Job` 型エイリアスを作成し、そのジョブをチャネルに送信する

`execute` で受け取ったクロージャを使って新しい `Job` インスタンスを作成した後 \[1\]、そのジョブをチャネルの送信側に送信します \[2\]。送信が失敗した場合に備えて、`send` で `unwrap` を呼んでいます。たとえば、すべてのスレッドの実行を停止した場合、つまり受信側が新しいメッセージの受信を停止した場合に、これが発生する可能性があります。現時点では、スレッドの実行を停止することはできません。プールが存在する限り、スレッドは継続して実行されます。`unwrap` を使う理由は、失敗のケースが起こらないことを私たちは知っているが、コンパイラはそれを知らないからです。

しかし、まだ終わりではありません！`Worker` では、`thread::spawn` に渡されるクロージャはまだ、チャネルの受信側を _参照_ するだけです。代わりに、クロージャが永久にループし、チャネルの受信側にジョブを要求し、ジョブを受け取ったときに実行するようにする必要があります。`Worker::new` に対して、リスト20-20に示す変更を加えましょう。

ファイル名: `src/lib.rs`

```rust
--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || loop {
            let job = receiver
              1.lock()
              2.unwrap()
              3.recv()
              4.unwrap();

            println!("Worker {id} got a job; executing.");

            job();
        });

        Worker { id, thread }
    }
}
```

リスト20-20: `Worker` インスタンスのスレッド内でジョブを受信して実行する

ここでは、まず `receiver` の `lock` を呼んでミューテックスを取得し \[1\]、次に `unwrap` を呼んでエラーがあった場合にパニックになります \[2\]。ミューテックスが _汚染された_ 状態にある場合、ロックを取得することが失敗する可能性があります。これは、他のスレッドがロックを保持したままパニックになり、ロックを解放しなかった場合に発生する可能性があります。この状況では、このスレッドがパニックになるように `unwrap` を呼ぶことが正しいアクションです。あなたが好きなら、この `unwrap` を、あなたにとって意味のあるエラーメッセージ付きの `expect` に変更しても構いません。

ミューテックスのロックを取得できた場合、`recv` を呼んでチャネルから `Job` を受信します \[3\]。最後の `unwrap` もまた、ここでエラーがあった場合にパニックになります \[4\]。これは、送信側を保持しているスレッドがシャットダウンした場合に発生する可能性があります。受信側がシャットダウンした場合に `send` メソッドが `Err` を返すのと同じようです。

`recv` の呼び出しはブロックされます。したがって、まだジョブがない場合、現在のスレッドはジョブが利用可能になるまで待ちます。`Mutex<T>` は、1つの `Worker` スレッドだけが1度にジョブを要求しようとしていることを保証します。

これで、私たちのスレッドプールは動作状態になりました！`cargo run` を実行して、いくつかの要求を行ってみましょう。

```bash
$ cargo run
   Compiling hello v0.1.0 (file:///projects/hello)
warning: field is never read: `workers`
 --> src/lib.rs:7:5
  |
7 |     workers: Vec<Worker>,
  |     ^^^^^^^^^^^^^^^^^^^^
  |
  = note: `#[warn(dead_code)]` on by default

warning: field is never read: `id`
  --> src/lib.rs:48:5
   |
48 |     id: usize,
   |     ^^^^^^^^^

warning: field is never read: `thread`
  --> src/lib.rs:49:5
   |
49 |     thread: thread::JoinHandle<()>,
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

warning: `hello` (lib) generated 3 warnings
    Finished dev [unoptimized + debuginfo] target(s) in 1.40s
     Running `target/debug/hello`
Worker 0 got a job; executing.
Worker 2 got a job; executing.
Worker 1 got a job; executing.
Worker 3 got a job; executing.
Worker 0 got a job; executing.
Worker 2 got a job; executing.
Worker 1 got a job; executing.
Worker 3 got a job; executing.
Worker 0 got a job; executing.
Worker 2 got a job; executing.
```

成功です！これで、非同期で接続を実行するスレッドプールができました。作成されるスレッドは4つを超えません。したがって、サーバが多くの要求を受け取った場合でも、システムが過負荷になることはありません。`/sleep` に要求を行うと、サーバは別のスレッドがそれらを実行することで、他の要求を処理することができます。

> 注: 同時に複数のブラウザウィンドウで _/sleep_ を開くと、5秒間隔で1つずつ読み込まれる場合があります。一部のウェブブラウザは、キャッシュの理由で、同じ要求の複数のインスタンスを順次実行します。この制限は、私たちのウェブサーバによるものではありません。

第18章で `while let` ループについて学んだ後、あなたはおそらく、なぜ私たちがリスト20-21に示すように `Worker` スレッドのコードを書かなかったのか疑問に思うでしょう。

ファイル名: `src/lib.rs`

```rust
--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || {
            while let Ok(job) = receiver.lock().unwrap().recv() {
                println!("Worker {id} got a job; executing.");

                job();
            }
        });

        Worker { id, thread }
    }
}
```

リスト20-21: `while let` を使った `Worker::new` の代替実装

このコードはコンパイルされて実行されますが、望ましいスレッドの動作をもたらさない。理由はやや微妙である。`Mutex` 構造体には公開の `unlock` メソッドがない。なぜなら、ロックの所有権は、`lock` メソッドが返す `LockResult<MutexGuard<T>>` 内の `MutexGuard<T>` の寿命に基づいているからである。コンパイル時に、バーローチェッカーは、`Mutex` によって保護されるリソースは、ロックを保持していない限りアクセスできないというルールを強制できる。しかし、この実装では、`MutexGuard<T>` の寿命に注意しない場合、ロックが意図したより長く保持される場合もある。

等号の右辺の式で使用される一時的な値は、`let` ステートメントが終了するとすぐに破棄される。しかし、`while let`（および `if let` と `match`）は、関連するブロックの終了まで一時的な値を破棄しない。リスト20-21では、`job()` の呼び出しの期間中、ロックが保持され続ける。これは、他の `Worker` インスタンスがジョブを受け取れないことを意味する。
