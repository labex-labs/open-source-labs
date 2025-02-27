# 新しいプロジェクトのセットアップ

新しいプロジェクトをセットアップするには、第1章で作成した`project`ディレクトリに移動し、Cargoを使って新しいプロジェクトを作成します。次のようにします。

```bash
cargo new guessing_game
cd guessing_game
```

最初のコマンド`cargo new`は、プロジェクト名（`guessing_game`）を第一引数として取ります。第二のコマンドは新しいプロジェクトのディレクトリに移動します。

生成された`Cargo.toml`ファイルを見てみましょう。

ファイル名：`Cargo.toml`

```toml
[package]
name = "guessing_game"
version = "0.1.0"
edition = "2021"

# 詳細はこちらを参照ください
https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
```

第1章で見たように、`cargo new`はあなたに「Hello, world!」プログラムを生成します。`src/main.rs`ファイルを見てみましょう。

ファイル名：`src/main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

ここで、この「Hello, world!」プログラムをコンパイルして、`cargo run`コマンドを使って同じ手順で実行しましょう。

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50s
     Running `target/debug/guessing_game`
Hello, world!
```

このゲームで行うように、プロジェクトを迅速に反復する必要がある場合、`run`コマンドは便利です。次の反復に移る前に、各反復を迅速にテストできます。

`src/main.rs`ファイルを再開します。このファイルにすべてのコードを書きます。
