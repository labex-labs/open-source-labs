# main における run から返されるエラーの処理

エラーをチェックして、リスト 12-10 で`Config::build`に対して使用したものと同様の手法を使って処理しますが、少し違いがあります。

ファイル名：`src/main.rs`

```rust
fn main() {
    --snip--

    println!("Searching for {}", config.query);
    println!("In file {}", config.file_path);

    if let Err(e) = run(config) {
        println!("Application error: {e}");
        process::exit(1);
    }
}
```

`run`が`Err`値を返すかどうかをチェックし、返した場合に`process::exit(1)`を呼び出すために、`unwrap_or_else`ではなく`if let`を使用します。`run`関数は、`Config::build`が`Config`インスタンスを返すのと同じように、`unwrap`したい値を返しません。`run`は成功した場合に`()`を返すため、エラーを検出することだけに関心があります。したがって、`unwrap_or_else`が展開された値（これはただの`()`になります）を返す必要はありません。

`if let`と`unwrap_or_else`関数の本体はどちらの場合も同じです。エラーを表示して終了します。
