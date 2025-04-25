# match

Rust は`match`キーワードを通じてパターンマッチングを提供します。これは C 言語の`switch`文のように使うことができます。最初に一致するアームが評価され、すべての可能な値がカバーされなければなりません。

```rust
fn main() {
    let number = 13;
    // TODO ^ `number` に対して異なる値を試してみる
    println!("Tell me about {}", number);
    match number {
        // 単一の値をマッチ
        1 => println!("One!"),
        // 複数の値をマッチ
        2 | 3 | 5 | 7 | 11 => println!("This is a prime"),
        // TODO ^ 素数のリストに 13 を追加してみる
        // 包含範囲をマッチ
        13..=19 => println!("A teen"),
        // その他のケースを処理
        _ => println!("Ain't special"),
        // TODO ^ この全てをキャッチするアームをコメントアウトしてみる
    }

    let boolean = true;
    // Match は式でもある
    let binary = match boolean {
        // マッチのアームはすべての可能な値をカバーしなければならない
        false => 0,
        true => 1,
        // TODO ^ これらのアームの 1 つをコメントアウトしてみる
    };

    println!("{} -> {}", boolean, binary);
}
```
