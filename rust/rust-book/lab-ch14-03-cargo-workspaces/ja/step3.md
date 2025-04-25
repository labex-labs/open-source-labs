# ワークスペース内の 2 番目のパッケージの作成

次に、ワークスペース内に別のメンバーパッケージを作成して「add_one」と呼びましょう。トップレベルの`Cargo.toml`を変更して、`members`リストに「add_one」のパスを指定します。

ファイル名：`Cargo.toml`

```toml
[workspace]

members = [
    "adder",
    "add_one",
]
```

次に、新しいライブラリクレート「add_one」を生成します。

```bash
$ cargo new add_one --lib
Created library $(add_one) package
```

この時点で、あなたの`add`ディレクトリには以下のディレクトリとファイルがあるはずです。

    ├── Cargo.lock
    ├── Cargo.toml
    ├── add_one
    │   ├── Cargo.toml
    │   └── src
    │       └── lib.rs
    ├── adder
    │   ├── Cargo.toml
    │   └── src
    │       └── main.rs
    └── target

`add_one/src/lib.rs`ファイルに、`add_one`関数を追加しましょう。

ファイル名：`add_one/src/lib.rs`

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}
```

これで、バイナリを持つ`adder`パッケージが、ライブラリを持つ`add_one`パッケージに依存するようになりました。まず、`adder/Cargo.toml`に`add_one`へのパス依存を追加する必要があります。

ファイル名：`adder/Cargo.toml`

```tomlrust
[dependencies]
add_one = { path = "../add_one" }
```

Cargo は、ワークスペース内のクレートが互いに依存することを想定していません。そのため、依存関係を明示する必要があります。

次に、`adder`クレートで`add_one`関数（`add_one`クレートから）を使用しましょう。`adder/src/main.rs`ファイルを開き、新しい`add_one`ライブラリクレートをスコープ内に持ち込むために、先頭に`use`行を追加します。その後、`main`関数を変更して`add_one`関数を呼び出します。以下はリスト 14-7 のようになります。

ファイル名：`adder/src/main.rs`

```rust
use add_one;

fn main() {
    let num = 10;
    println!(
        "Hello, world! {num} plus one is {}!",
        add_one::add_one(num)
    );
}
```

リスト 14-7: `adder`クレートから`add_one`ライブラリクレートを使用する

トップレベルの`add`ディレクトリで`cargo build`を実行して、ワークスペースをビルドしましょう！

```bash
$ cargo build
   Compiling add_one v0.1.0 (file:///projects/add/add_one)
   Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished dev [unoptimized + debuginfo] target(s) in 0.68s
```

`add`ディレクトリからバイナリクレートを実行するには、`-p`引数とパッケージ名を使って、ワークスペース内で実行したいパッケージを指定できます。`cargo run`を使います。

```bash
$ cargo run -p adder
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/adder`
Hello, world! 10 plus one is 11!
```

これは、`add_one`クレートに依存する`adder/src/main.rs`のコードを実行します。
