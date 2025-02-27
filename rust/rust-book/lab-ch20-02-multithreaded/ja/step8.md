# スレッドを格納するための空間を作成する

これで、プールに格納するための有効な数のスレッドがあることを知る方法があるので、それらのスレッドを作成して、構造体を返す前に `ThreadPool` 構造体に格納することができます。しかし、どのようにしてスレッドを「格納」するのでしょうか。`thread::spawn` のシグネチャをもう一度見てみましょう。

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
    where
        F: FnOnce() -> T,
        F: Send + 'static,
        T: Send + 'static,
```

`spawn` 関数は `JoinHandle<T>` を返します。ここで、`T` はクロージャが返す型です。`JoinHandle` も使ってみて、何が起こるか見てみましょう。私たちの場合、スレッドプールに渡すクロージャは接続を処理して何も返さないので、`T` はユニット型 `()` になります。

リスト20-14のコードはコンパイルされますが、まだスレッドは作成されていません。`ThreadPool` の定義を変更して、`thread::JoinHandle<()>` インスタンスのベクトルを保持するようにし、ベクトルを `size` の容量で初期化し、スレッドを作成するためのコードを実行する `for` ループを設定し、それらを含む `ThreadPool` インスタンスを返しました。

ファイル名: `src/lib.rs`

```rust
1 use std::thread;

pub struct ThreadPool {
  2 threads: Vec<thread::JoinHandle<()>>,
}

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

      3 let mut threads = Vec::with_capacity(size);

        for _ in 0..size {
            // create some threads and store them in the vector
        }

        ThreadPool { threads }
    }
    --snip--
}
```

リスト20-14: `ThreadPool` がスレッドを保持するためのベクトルを作成する

`std::thread` をライブラリクレートのスコープ内に持ち込んでいます \[1\]。なぜなら、`ThreadPool` のベクトル内の要素の型として `thread::JoinHandle<()>` を使用しているからです \[2\]。

有効なサイズを受け取ると、私たちの `ThreadPool` は `size` 個の要素を保持できる新しいベクトルを作成します \[3\]。`with_capacity` 関数は `Vec::new` と同じタスクを行いますが、重要な違いがあります。それは、ベクトル内に事前に空間を割り当てます。ベクトル内に `size` 個の要素を格納する必要があることがわかっているので、この事前割り当ては、要素が挿入されるときに自動的にサイズを調整する `Vec::new` を使うよりもわずかに効率的です。

もう一度 `cargo check` を実行すると、成功するはずです。
