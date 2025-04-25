# コンパイラ駆動開発を使った ThreadPool の構築

リスト 20-12 の変更を `src/main.rs` に加え、その後、`cargo check` からのコンパイラエラーを使って開発を進めましょう。最初に得られるエラーは次の通りです。

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0433]: failed to resolve: use of undeclared type `ThreadPool`
  --> src/main.rs:11:16
   |
11 |     let pool = ThreadPool::new(4);
   |                ^^^^^^^^^^ use of undeclared type `ThreadPool`
```

素晴らしい！このエラーは、`ThreadPool` 型またはモジュールが必要であることを教えてくれます。ですから、今から作成しましょう。私たちの `ThreadPool` の実装は、Web サーバが行っている作業の種類に依存しません。ですから、`hello` クレートをバイナリクレートからライブラリクレートに切り替えて、`ThreadPool` の実装を保持しましょう。ライブラリクレートに変更した後は、スレッドプールを使用して行いたい作業に対して、Web 要求の処理に限定されることなく、別のスレッドプールライブラリを使用することもできます。

`src/lib.rs` ファイルを作成し、次の内容を含めます。これは、今のところで私たちが持てる `ThreadPool` 構造体の最も単純な定義です。

ファイル名：`src/lib.rs`

```rust
pub struct ThreadPool;
```

そして、`src/main.rs` の先頭に次のコードを追加することで、`main.rs` ファイルを編集して、ライブラリクレートから `ThreadPool` をスコープ内に持ち込みます。

ファイル名：`src/main.rs`

```rust
use hello::ThreadPool;
```

このコードはまだ動作しませんが、次に対処する必要のあるエラーを取得するために、もう一度チェックしましょう。

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0599]: no function or associated item named `new` found for struct
`ThreadPool` in the current scope
  --> src/main.rs:12:28
   |
12 |     let pool = ThreadPool::new(4);
   |                            ^^^ function or associated item not found in
`ThreadPool`
```

このエラーは、次に `ThreadPool` に対して `new` という名前の関連付けられた関数を作成する必要があることを示しています。また、`new` には、引数として `4` を受け取り、`ThreadPool` インスタンスを返す 1 つのパラメータが必要であることも知っています。これらの特性を持つ最も単純な `new` 関数を実装しましょう。

ファイル名：`src/lib.rs`

```rust
pub struct ThreadPool;

impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        ThreadPool
    }
}
```

`size` パラメータの型として `usize` を選んだのは、負の数のスレッドは意味をなさないことがわかっているからです。また、この `4` をスレッドのコレクションの要素数として使用することがわかっており、これが `usize` 型の目的であることも、「整数型」で説明した通りです。

もう一度コードをチェックしましょう。

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0599]: no method named `execute` found for struct `ThreadPool` in the
current scope
  --> src/main.rs:17:14
   |
17 |         pool.execute(|| {
   |              ^^^^^^^ method not found in `ThreadPool`
```

今回のエラーは、`ThreadPool` に `execute` メソッドがないために発生します。「有限数のスレッドを作成する」で思い出してください。私たちは、スレッドプールが `thread::spawn` と同じようなインターフェイスを持つべきだと決めました。また、`execute` 関数を実装して、与えられたクロージャを受け取り、プール内の待機中のスレッドに実行させます。

`ThreadPool` の `execute` メソッドを定義して、クロージャをパラメータとして取るようにします。「クロージャからキャプチャされた値を移動させるときと Fn トレイト」で思い出してください。クロージャを 3 つの異なるトレイト：`Fn`、`FnMut`、および `FnOnce` を使ってパラメータとして取ることができます。ここでどの種類のクロージャを使うかを決める必要があります。最終的には、標準ライブラリの `thread::spawn` の実装と同じようなことを行うことになるので、`thread::spawn` のシグネチャがパラメータにどのような制約を持つかを見ることができます。ドキュメントからは次のように示されています。

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
    where
        F: FnOnce() -> T,
        F: Send + 'static,
        T: Send + 'static,
```

ここでは `F` 型パラメータが関心の対象です。`T` 型パラメータは戻り値に関係しており、これには関心がありません。`spawn` は `F` に対するトレイトバウンドとして `FnOnce` を使用していることがわかります。これもおそらく私たちが望むものです。なぜなら、最終的には `execute` で受け取った引数を `spawn` に渡すからです。`FnOnce` が私たちが使用したいトレイトであることをさらに確信できるのは、要求を実行するためのスレッドがその要求のクロージャを一度だけ実行するだけであり、これは `FnOnce` の `Once` に一致するからです。

`F` 型パラメータにはまた、トレイトバウンド `Send` と寿命バウンド `'static` があります。これらは私たちの状況で役立ちます。クロージャを 1 つのスレッドから別のスレッドに転送するために `Send` が必要であり、スレッドが実行するのにどれくらいの時間がかかるかわからないために `'static` が必要です。これらの制約を持つ型 `F` のジェネリックパラメータを取る `ThreadPool` の `execute` メソッドを作成しましょう。

ファイル名：`src/lib.rs`

```rust
impl ThreadPool {
    --snip--
    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() 1 + Send + 'static,
    {
    }
}
```

`FnOnce` の後にまだ `()` を使用しています \[1\]。この `FnOnce` は、パラメータを持たず、ユニット型 `()` を返すクロージャを表しています。関数定義と同様に、シグネチャから戻り値の型を省略できますが、パラメータがなくても、依然として括弧が必要です。

再び、これは `execute` メソッドの最も単純な実装です。何もしませんが、私たちはただコードをコンパイルさせようとしています。もう一度チェックしましょう。

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 0.24s
```

コンパイルされました！ただし、`cargo run` を試してブラウザで要求を行うと、章の冒頭で見たブラウザのエラーが表示されます。私たちのライブラリは、実際には `execute` に渡されたクロージャを呼び出していません！

> 注：Haskell や Rust のような厳密なコンパイラを持つ言語に関して、「コードがコンパイルされれば、動作する」という言葉を耳にすることがあります。しかし、この言葉は必ずしも普遍的に正しいとは限りません。私たちのプロジェクトはコンパイルされますが、まったく何もしません！本当の完全なプロジェクトを構築している場合、これはコードがコンパイルされ _ かつ _ 私たちが望む動作を持つことを確認するためのユニットテストを書き始めるのに良いタイミングです。
