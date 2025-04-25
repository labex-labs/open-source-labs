# 戻り値を持つ関数

関数は、それを呼び出すコードに値を返すことができます。戻り値には名前を付けませんが、矢印 (`->`) の後にその型を宣言する必要があります。Rust では、関数の戻り値は、関数本体のブロック内の最終式の値と同義です。`return` キーワードを使って値を指定することで、関数から早期に戻ることができますが、ほとんどの関数は最後の式を暗黙的に返します。戻り値を持つ関数の例を以下に示します。

ファイル名：`src/main.rs`

```rust
fn five() -> i32 {
    5
}

fn main() {
    let x = five();

    println!("The value of x is: {x}");
}
```

`five` 関数には関数呼び出しもマクロも、さらに `let` 文すらありません。ただ数字 `5` だけです。これは Rust では完全に有効な関数です。関数の戻り型も `-> i32` と指定されていることに注意してください。このコードを実行してみてください。出力は以下のようになるはずです。

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/functions`
The value of x is: 5
```

`five` の中の `5` は関数の戻り値です。これが戻り型が `i32` である理由です。もう少し詳しく見てみましょう。重要な点は 2 つあります。まず、`let x = five();` の行は、関数の戻り値を使って変数を初期化していることを示しています。関数 `five` は `5` を返すので、この行は以下と同じです。

```rust
let x = 5;
```

2 番目に、`five` 関数にはパラメータがなく、戻り値の型が定義されていますが、関数本体はセミコロンのない孤独な `5` です。なぜなら、それは戻したい値の式だからです。

もう 1 つの例を見てみましょう。

ファイル名：`src/main.rs`

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1
}
```

このコードを実行すると、`The value of x is: 6` が表示されます。しかし、`x + 1` を含む行の末尾にセミコロンを置くと、式を文に変えてしまうので、エラーが発生します。

ファイル名：`src/main.rs`

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1;
}
```

このコードをコンパイルすると、以下のようなエラーが発生します。

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
error[E0308]: mismatched types
 --> src/main.rs:7:24
  |
7 | fn plus_one(x: i32) -> i32 {
  |    --------            ^^^ expected `i32`, found `()`
  |    |
  |    implicitly returns `()` as its body has no tail or `return` expression
8 |     x + 1;
  |          - help: remove this semicolon
```

主なエラーメッセージである `mismatched types` は、このコードの核心問題を明らかにしています。`plus_one` 関数の定義は、`i32` を返すと言っていますが、文は値に評価されません。これは、単位型である `()` で表されます。したがって、何も返されず、関数定義と矛盾してエラーが発生します。この出力では、Rust がこの問題を修正するためのメッセージを提供しています。セミコロンを削除することでエラーが解消されます。
