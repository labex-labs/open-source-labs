# new におけるスレッド数の検証

`new` と `execute` のパラメータに対して何もしていません。これらの関数の本体を、私たちが望む動作で実装しましょう。まず、`new` について考えてみましょう。前述の通り、`size` パラメータに対して符号なし型を選びました。なぜなら、負の数のスレッドを持つプールは意味をなさないからです。しかし、ゼロ個のスレッドを持つプールも意味をなさないですが、ゼロは完全に有効な `usize` です。`ThreadPool` インスタンスを返す前に、`size` がゼロより大きいことを確認するコードを追加し、`assert!` マクロを使ってゼロを受け取った場合にプログラムをパニックにさせます。これはリスト 20-13 に示されています。

ファイル名：`src/lib.rs`

```rust
impl ThreadPool {
    /// Create a new ThreadPool.
    ///
    /// The size is the number of threads in the pool.
    ///
  1 /// # Panics
    ///
    /// The `new` function will panic if the size is zero.
    pub fn new(size: usize) -> ThreadPool {
      2 assert!(size > 0);

        ThreadPool
    }

    --snip--
}
```

リスト 20-13: `size` がゼロの場合にパニックになるように `ThreadPool::new` を実装する

また、doc コメントを使って `ThreadPool` のドキュメントを追加しました。第 14 章で説明したように、関数がパニックになる状況を明記するセクションを追加することで、良いドキュメントの作成方法を守っています \[1\]。`cargo doc --open` を実行し、`ThreadPool` 構造体をクリックして、`new` の生成されたドキュメントを見てみてください！

ここで行ったように `assert!` マクロを追加する代わりに \[2\]、`new` を `build` に変更して、リスト 12-9 の I/O プロジェクトの `Config::build` と同じように `Result` を返すこともできます。しかし、この場合、ゼロ個のスレッドでスレッドプールを作成しようとすることは回復不可能なエラーであると判断しました。もし意欲的であれば、次のシグネチャを持つ `build` という名前の関数を書いて、`new` 関数と比較してみてください。

```rust
pub fn build(
    size: usize
) -> Result<ThreadPool, PoolCreationError> {
```
