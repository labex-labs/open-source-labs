# 標準エラーにエラーを出力する

エラーメッセージの出力方法を変更するには、リスト 12-24 のコードを使用します。この章の前半で行ったリファクタリングのおかげで、エラーメッセージを出力するすべてのコードは、1 つの関数 `main` にまとまっています。標準ライブラリには、標準エラーストリームに出力する `eprintln!` マクロが用意されているので、エラーを出力するために `println!` を呼び出していた 2 箇所を `eprintln!` に変更しましょう。

ファイル名：`src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    if let Err(e) = minigrep::run(config) {
        eprintln!("Application error: {e}");
        process::exit(1);
    }
}
```

リスト 12-24: `eprintln!` を使って標準エラーにエラーメッセージを書き込む

では、再度同じように引数なしでプログラムを実行し、`>` で標準出力をリダイレクトしましょう。

```bash
$ cargo run > output.txt
Problem parsing arguments: not enough arguments
```

今回はエラーが画面に表示され、_output.txt_ には何も含まれていません。これはコマンドラインプログラムが期待する動作です。

次に、エラーを引き起こさない引数を使って再度プログラムを実行し、標準出力をまだファイルにリダイレクトします。

```bash
cargo run -- to poem.txt > output.txt
```

端末には出力が表示されず、_output.txt_ には結果が含まれます。

ファイル名：output.txt

```rust
Are you nobody, too?
How dreary to be somebody!
```

これは、成功した出力には標準出力を、エラー出力には標準エラーをそれぞれ適切に使用していることを示しています。
