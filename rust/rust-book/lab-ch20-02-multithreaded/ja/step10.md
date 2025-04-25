# チャネルを通じてスレッドに要求を送信する

次に解決する問題は、`thread::spawn` に与えられるクロージャが何もしないことです。現在、`execute` メソッドで実行したいクロージャを取得しています。しかし、`ThreadPool` を作成する際に各 `Worker` を作成するときに、`thread::spawn` に実行するクロージャを与える必要があります。

先ほど作成した `Worker` 構造体が、`ThreadPool` に保持されているキューから実行するコードを取得し、そのコードを自分のスレッドに送信して実行するようにしたいです。

第 16 章で学んだチャネルは、2 つのスレッド間で通信する簡単な方法です。このユースケースには最適です。チャネルをジョブのキューとして機能させ、`execute` がジョブを `ThreadPool` から `Worker` インスタンスに送信し、それがジョブを自分のスレッドに送信します。これが計画です。

1. `ThreadPool` はチャネルを作成し、送信側を保持する。
2. 各 `Worker` は受信側を保持する。
3. チャネルを通じて送信したいクロージャを保持する新しい `Job` 構造体を作成する。
4. `execute` メソッドは、実行したいジョブを送信側を通じて送信する。
5. そのスレッド内で、`Worker` は受信側をループ処理し、受信したジョブのクロージャを実行する。

まず、`ThreadPool::new` でチャネルを作成し、`ThreadPool` インスタンスに送信側を保持するようにしましょう。これはリスト 20-16 に示されています。`Job` 構造体は現在何も保持していませんが、チャネルを通じて送信するアイテムの型になります。

ファイル名：`src/lib.rs`

```rust
use std::{sync::mpsc, thread};

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: mpsc::Sender<Job>,
}

struct Job;

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

      1 let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id));
        }

        ThreadPool { workers, 2 sender }
    }
    --snip--
}
```

リスト 20-16: `Job` インスタンスを送信するチャネルの送信側を格納するように `ThreadPool` を変更する

`ThreadPool::new` では、新しいチャネルを作成し \[1\]、プールが送信側を保持するようにします \[2\]。これは正常にコンパイルされます。

`ThreadPool` がチャネルを作成するときに、各 `Worker` にチャネルの受信側を渡してみましょう。`Worker` インスタンスが生成するスレッドで受信側を使用したいので、クロージャ内で `receiver` パラメータを参照します。リスト 20-17 のコードはまだコンパイルされません。

ファイル名：`src/lib.rs`

```rust
impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
          1 workers.push(Worker::new(id, receiver));
        }

        ThreadPool { workers, sender }
    }
    --snip--
}

--snip--

impl Worker {
    fn new(id: usize, receiver: mpsc::Receiver<Job>) -> Worker {
        let thread = thread::spawn(|| {
          2 receiver;
        });

        Worker { id, thread }
    }
}
```

リスト 20-17: 各 `Worker` に受信側を渡す

小さな単純な変更を加えました。受信側を `Worker::new` に渡し \[1\]、そしてクロージャ内で使用します \[2\]。

このコードをチェックしようとすると、次のエラーが表示されます。

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0382]: use of moved value: `receiver`
  --> src/lib.rs:26:42
   |
21 |         let (sender, receiver) = mpsc::channel();
   |                      -------- move occurs because `receiver` has type
`std::sync::mpsc::Receiver<Job>`, which does not implement the `Copy` trait
...
26 |             workers.push(Worker::new(id, receiver));
   |                                          ^^^^^^^^ value moved here, in
previous iteration of loop
```

コードは `receiver` を複数の `Worker` インスタンスに渡そうとしています。これは機能しません。第 16 章で思い出してください。Rust が提供するチャネルの実装は、複数の _ プロデューサー _、単一の _ コンシューマー _ です。これは、このコードを修正するためにチャネルの消費側を単にクローンすることはできないことを意味します。また、複数のコンシューマーにメッセージを複数回送信したくはありません。複数の `Worker` インスタンスがある場合に、各メッセージが 1 回だけ処理されるように、1 つのメッセージのリストが欲しいです。

また、チャネルキューからジョブを取り出すには、`receiver` を変更する必要があります。したがって、スレッドは `receiver` を共有して変更する安全な方法が必要です。そうでなければ、競合条件が発生する可能性があります（第 16 章で説明されています）。

第 16 章で説明したスレッドセーフなスマートポインタを思い出してください。複数のスレッド間で所有権を共有し、スレッドが値を変更できるようにするには、`Arc<Mutex<T>>` を使用する必要があります。`Arc` 型は、複数の `Worker` インスタンスが受信側を所有できるようにし、`Mutex` は、1 つの `Worker` だけが受信側からジョブを取得できるようにします。リスト 20-18 に必要な変更を示します。

ファイル名：`src/lib.rs`

```rust
use std::{
    sync::{mpsc, Arc, Mutex},
    thread,
};
--snip--

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

      1 let receiver = Arc::new(Mutex::new(receiver));

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(
                Worker::new(id, Arc::clone(& 2 receiver))
            );
        }

        ThreadPool { workers, sender }
    }

    --snip--
}

--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        --snip--
    }
}
```

リスト 20-18: `Arc` と `Mutex` を使用して `Worker` インスタンス間で受信側を共有する

`ThreadPool::new` では、受信側を `Arc` と `Mutex` に入れます \[1\]。各新しい `Worker` に対して、`Arc` をクローンして参照カウントを増やし、`Worker` インスタンスが受信側の所有権を共有できるようにします \[2\]。

これらの変更により、コードはコンパイルされます！着々と進んでいます！
