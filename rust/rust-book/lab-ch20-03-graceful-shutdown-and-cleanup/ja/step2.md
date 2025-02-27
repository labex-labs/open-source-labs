# スレッドプールにおけるDropトレイトの実装

まずは、スレッドプールに`Drop`を実装しましょう。プールが破棄されるとき、すべてのスレッドがjoinして、作業を終えることができるようにする必要があります。リスト20-22は、`Drop`実装の最初の試みを示していますが、このコードはまだうまく動作しません。

ファイル名: `src/lib.rs`

```rust
impl Drop for ThreadPool {
    fn drop(&mut self) {
      1 for worker in &mut self.workers {
          2 println!("Shutting down worker {}", worker.id);

          3 worker.thread.join().unwrap();
        }
    }
}
```

リスト20-22: スレッドプールがスコープ外になるときに各スレッドをjoinする

まず、スレッドプールの各`worker`をループ処理します\[1\]。ここでは`&mut`を使っています。なぜなら`self`は可変参照であり、`worker`も変更する必要があるからです。各`worker`に対して、この特定の`Worker`インスタンスがシャットダウンされていることを示すメッセージを出力します\[2\]。そして、その`Worker`インスタンスのスレッドに`join`を呼び出します\[3\]。`join`の呼び出しが失敗した場合、`unwrap`を使ってRustがパニックになり、グレースフルでないシャットダウンに入ります。

このコードをコンパイルすると、以下のエラーが表示されます。

```bash
error[E0507]: cannot move out of `worker.thread` which is behind a mutable
reference
    --> src/lib.rs:52:13
     |
52   |             worker.thread.join().unwrap();
     |             ^^^^^^^^^^^^^ ------ `worker.thread` moved due to this
method call
     |             |
     |             move occurs because `worker.thread` has type
`JoinHandle<()>`, which does not implement the `Copy` trait
     |
note: this function takes ownership of the receiver `self`, which moves
`worker.thread`
```

このエラーは、各`worker`の可変参照しか持っていないのに`join`を呼び出せないことを示しています。`join`は引数の所有権を取得するからです。この問題を解決するには、`thread`を所有する`Worker`インスタンスからスレッドを移動させる必要があります。そうすることで`join`がスレッドを消費できるようになります。これは、リスト17-15で行ったことと同じです。`Worker`が`Option<thread::JoinHandle<()>>`を保持している場合、`Option`の`take`メソッドを呼び出して、`Some`バリアントから値を移動させ、その代わりに`None`バリアントを残すことができます。つまり、実行中の`Worker`は`thread`に`Some`バリアントがあり、`Worker`をクリーンアップしたいときには、`Some`を`None`に置き換えることで、`Worker`が実行するスレッドがなくなります。

ですから、`Worker`の定義を以下のように更新することがわかります。

ファイル名: `src/lib.rs`

```rust
struct Worker {
    id: usize,
    thread: Option<thread::JoinHandle<()>>,
}
```

次に、コンパイラに頼って、変更が必要な他の場所を見つけましょう。このコードをチェックすると、2つのエラーが表示されます。

```bash
error[E0599]: no method named `join` found for enum `Option` in the current
scope
  --> src/lib.rs:52:27
   |
52 |             worker.thread.join().unwrap();
   |                           ^^^^ method not found in
`Option<JoinHandle<()>>`

error[E0308]: mismatched types
  --> src/lib.rs:72:22
   |
72 |         Worker { id, thread }
   |                      ^^^^^^ expected enum `Option`, found struct
`JoinHandle`
   |
   = note: expected enum `Option<JoinHandle<()>>`
            found struct `JoinHandle<_>`
help: try wrapping the expression in `Some`
   |
72 |         Worker { id, thread: Some(thread) }
   |                      +++++++++++++      +
```

2番目のエラーを解決しましょう。これは、`Worker::new`の末尾のコードを指しています。新しい`Worker`を作成するとき、`thread`値を`Some`でラップする必要があります。このエラーを修正するために、次のように変更します。

ファイル名: `src/lib.rs`

```rust
impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        --snip--

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```

最初のエラーは、`Drop`実装にあります。前述の通り、`Option`値の`take`を呼び出して、`worker`から`thread`を移動させる予定でした。次の変更を行うことでそれができます。

ファイル名: `src/lib.rs`

```rust
impl Drop for ThreadPool {
    fn drop(&mut self) {
        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

          1 if let Some(thread) = worker.thread.take() {
              2 thread.join().unwrap();
            }
        }
    }
}
```

第17章で説明したように、`Option`の`take`メソッドは`Some`バリアントを取り出し、その代わりに`None`を残します。`if let`を使って`Some`を分解し、スレッドを取得します\[1\]。そして、そのスレッドに`join`を呼び出します\[2\]。`Worker`インスタンスのスレッドが既に`None`である場合、その`Worker`は既にスレッドがクリーンアップされていることがわかります。したがって、その場合何も起こりません。
