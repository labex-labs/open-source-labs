# Config::build を呼び出してエラーを処理する

エラーケースを処理してユーザーに親切なメッセージを表示するには、`main`を更新して`Config::build`が返す`Result`を処理する必要があります。これはリスト 12-10 に示されています。また、コマンドラインツールを非ゼロのエラーコードで終了させる責任を`panic!`から外し、代わりに手動で実装します。非ゼロの終了ステータスは、プログラムがエラー状態で終了したことを呼び出し元のプロセスに知らせるための慣例です。

ファイル名：`src/main.rs`

```rust
1 use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();

  2 let config = Config::build(&args).3 unwrap_or_else(|4 err| {
      5 println!("Problem parsing arguments: {err}");
      6 process::exit(1);
    });

    --snip--
```

リスト 12-10: `Config`の構築に失敗した場合にエラーコードで終了する

このリストでは、まだ詳細を説明していないメソッドを使用しています。`unwrap_or_else`です。これは、標準ライブラリによって`Result<T, E>`に定義されています\[2\]。`unwrap_or_else`を使用することで、`panic!`ではないカスタムのエラーハンドリングを定義できます。`Result`が`Ok`値の場合、このメソッドの動作は`unwrap`と似ています。つまり、`Ok`がラップしている内部値を返します。ただし、値が`Err`値の場合、このメソッドはクロージャ内のコードを呼び出します。クロージャは、定義して`unwrap_or_else`に引数として渡す匿名関数です\[3\]。第 13 章でクロージャについてもっと詳しく説明します。今のところ、`unwrap_or_else`が`Err`の内部値を渡すことだけを知っておけば十分です。この場合、それはリスト 12-9 で追加した静的文字列`"not enough arguments"`で、縦棒の間に表示される引数`err`のクロージャに渡されます\[4\]。その後、クロージャ内のコードは実行時に`err`値を使用できます。

標準ライブラリから`process`をスコープ内に持ち込むために新しい`use`行を追加しました\[1\]。エラーケースで実行されるクロージャ内のコードは 2 行だけです。`err`値を表示し\[5\]、その後`process::exit`を呼び出します\[6\]。`process::exit`関数は、プログラムを即座に停止し、終了ステータスコードとして渡された数を返します。これは、リスト 12-8 で使用した`panic!`ベースのハンドリングに似ていますが、もはや余分な出力は得られません。試してみましょう。

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.48s
     Running `target/debug/minigrep`
Problem parsing arguments: not enough arguments
```

素晴らしい！この出力はユーザーにとってははるかに親切です。
