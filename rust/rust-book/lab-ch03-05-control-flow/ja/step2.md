# if 式

`if`式を使うと、条件に応じてコードを分岐させることができます。条件を指定して、「この条件が満たされた場合、このコードブロックを実行します。条件が満たされない場合、このコードブロックを実行しません。」と述べます。

`if`式を調べるために、`project`ディレクトリに新しいプロジェクト`branches`を作成しましょう。`src/main.rs`ファイルに次のコードを入力します：

```bash
cd ~/project
cargo new branches
```

ファイル名：`src/main.rs`

```rust
fn main() {
    let number = 3;

    if number < 5 {
        println!("condition was true");
    } else {
        println!("condition was false");
    }
}
```

すべての`if`式はキーワード`if`から始まり、その後に条件が続きます。この場合、条件は変数`number`の値が 5 未満であるかどうかをチェックしています。条件が`true`の場合に実行するコードブロックを、カッコ内の条件の直後に配置します。`if`式の条件に関連付けられたコードブロックは、「比較的推測する秘密の数」で議論した`match`式のアームのように、時には「アーム」と呼ばれます。

任意ですが、ここでは`else`式も含めることができます。これにより、条件が`false`の場合に実行する代替のコードブロックをプログラムに与えることができます。`else`式を提供せず、条件が`false`の場合、プログラムは`if`ブロックをスキップし、次のコードに進みます。

このコードを実行してみましょう。以下の出力が表示されるはずです：

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
condition was true
```

`number`の値を条件が`false`になる値に変更して、何が起こるか見てみましょう：

```rust
    let number = 7;
```

再度プログラムを実行して、出力を見てみましょう：

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
condition was false
```

また、このコードの条件は`bool`型でなければならないことにも注意してください。条件が`bool`型でない場合、エラーが発生します。たとえば、次のコードを実行してみましょう：

ファイル名：`src/main.rs`

```rust
fn main() {
    let number = 3;

    if number {
        println!("number was three");
    }
}
```

今回は`if`条件が値`3`を評価し、Rust がエラーを投げます：

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
error[E0308]: mismatched types
 --> src/main.rs:4:8
  |
4 |     if number {
  |        ^^^^^^ expected `bool`, found integer
```

このエラーは、Rust が`bool`型を期待していたが整数型を受け取ったことを示しています。Ruby や JavaScript などの言語とは異なり、Rust は非ブール型を自動的にブール型に変換しようとしません。条件として常にブール型を`if`に提供する必要があります。たとえば、数値が`0`でない場合にのみ`if`コードブロックを実行したい場合は、`if`式を次のように変更できます：

ファイル名：`src/main.rs`

```rust
fn main() {
    let number = 3;

    if number!= 0 {
        println!("number was something other than zero");
    }
}
```

このコードを実行すると、`number was something other than zero`が表示されます。
