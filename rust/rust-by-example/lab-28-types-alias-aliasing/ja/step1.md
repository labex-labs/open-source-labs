# エイリアシング

`type` ステートメントを使って、既存の型に新しい名前を付けることができます。型は `UpperCamelCase` の名前を持たなければならず、そうでない場合、コンパイラは警告を発します。このルールの例外は基本型です。`usize`、`f32` などです。

```rust
// `NanoSecond`、`Inch`、および `U64` は `u64` の新しい名前です。
type NanoSecond = u64;
type Inch = u64;
type U64 = u64;

fn main() {
    // `NanoSecond` = `Inch` = `U64` = `u64`。
    let nanoseconds: NanoSecond = 5 as U64;
    let inches: Inch = 2 as U64;

    // 型エイリアスは追加の型安全性を提供しないことに注意してください。なぜなら、
    // エイリアスは新しい型ではないからです。
    println!("{} nanoseconds + {} inches = {} unit?",
             nanoseconds,
             inches,
             nanoseconds + inches);
}
```

エイリアスの主な用途は、定型句を減らすことです。たとえば、`io::Result<T>` 型は `Result<T, io::Error>` 型のエイリアスです。
