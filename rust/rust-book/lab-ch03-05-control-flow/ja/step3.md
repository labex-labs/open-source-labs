# else if を使った複数の条件の処理

`else if`式で`if`と`else`を組み合わせることで、複数の条件を使うことができます。たとえば：

ファイル名：`src/main.rs`

```rust
fn main() {
    let number = 6;

    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else if number % 2 == 0 {
        println!("number is divisible by 2");
    } else {
        println!("number is not divisible by 4, 3, or 2");
    }
}
```

このプログラムは 4 つの可能な経路を持っています。実行後、次の出力が表示されるはずです：

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
number is divisible by 3
```

このプログラムが実行されると、各`if`式を順番にチェックし、条件が`true`と評価される最初の本体を実行します。6 は 2 で割り切れることに注意してくださいが、`number is divisible by 2`の出力は表示されず、`else`ブロックの`number is not divisible by 4, 3, or 2`のテキストも表示されません。それは、Rust は最初の`true`条件のブロックのみを実行し、見つけるとそれ以降をチェックしないからです。

`else if`式をたくさん使うとコードが混乱するので、1 つ以上ある場合はコードをリファクタリングする必要があるかもしれません。第 6 章では、これらのケースに対して`match`と呼ばれる強力な Rust の分岐構文について説明しています。
