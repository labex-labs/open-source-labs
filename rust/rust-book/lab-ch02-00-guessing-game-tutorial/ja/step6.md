# Result を使った潜在的なエラーの処理

まだこのコード行に取り組んでいます。今は 3 行目のコードについて話していますが、1 つの論理的なコード行の一部であることに注意してください。次の部分はこのメソッドです。

```rust
.expect("Failed to read line");
```

このコードを次のように書くこともできました。

```rust
io::stdin().read_line(&mut guess).expect("Failed to read line");
```

しかし、1 行が長くなると読みにくくなるので、分割するのが良いでしょう。`.method_name()`構文でメソッドを呼び出す際に、改行やその他の空白を入れて長い行を分割するのは、多くの場合賢明です。では、この行が何をするか見てみましょう。

前述の通り、`read_line`はユーザーが入力したものを渡された文字列に入れますが、`Result`値を返します。`Result`は「列挙型」と呼ばれるもので、通常は「enum」と略されます。これは、複数の可能な状態のいずれかになり得る型です。それぞれの可能な状態を「バリアント」と呼びます。

第 6 章で列挙型についてもっと詳しく説明します。これらの`Result`型の目的は、エラー処理情報をエンコードすることです。

`Result`のバリアントは`Ok`と`Err`です。`Ok`バリアントは操作が成功したことを示し、`Ok`の中には成功して生成された値があります。`Err`バリアントは操作が失敗したことを意味し、`Err`には操作がどのように、またはなぜ失敗したかに関する情報が含まれています。

`Result`型の値は、他の型の値と同様に、それに定義されたメソッドがあります。`Result`のインスタンスには、呼び出すことができる`expect`メソッドがあります。この`Result`のインスタンスが`Err`値である場合、`expect`はプログラムをクラッシュさせ、`expect`に引数として渡したメッセージを表示します。`read_line`メソッドが`Err`を返す場合、それはおそらく基礎となるオペレーティングシステムからのエラーの結果でしょう。この`Result`のインスタンスが`Ok`値である場合、`expect`は`Ok`が保持している戻り値を取り、その値だけを返してくれます。それで、その値を使うことができます。この場合、その値はユーザー入力のバイト数です。

`expect`を呼び出さない場合、プログラムはコンパイルされますが、警告が表示されます。

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
warning: unused `Result` that must be used
  --> src/main.rs:10:5
   |
10 |     io::stdin().read_line(&mut guess);
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   |
   = note: `#[warn(unused_must_use)]` on by default
   = note: this `Result` may be an `Err` variant, which should be handled

warning: `guessing_game` (bin "guessing_game") generated 1 warning
    Finished dev [unoptimized + debuginfo] target(s) in 0.59s
```

Rust は、`read_line`から返された`Result`値を使っていないことを警告しており、これはプログラムが潜在的なエラーを処理していないことを示しています。

警告を抑制する正しい方法は、実際にエラー処理コードを書くことですが、この場合、問題が発生したときにこのプログラムをクラッシュさせたいだけなので、`expect`を使うことができます。第 9 章でエラーから回復する方法について学びます。
