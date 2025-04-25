# ガード

アームをフィルタリングするために `match` の _ガード_ を追加できます。

```rust
#[allow(dead_code)]
enum Temperature {
    Celsius(i32),
    Fahrenheit(i32),
}

fn main() {
    let temperature = Temperature::Celsius(35);
    // ^ `temperature` に対して異なる値を試してみてください
    match temperature {
        Temperature::Celsius(t) if t > 30 => println!("{}C は摂氏 30 度を超えています", t),
        // `if condition` の部分 ^ がガードです
        Temperature::Celsius(t) => println!("{}C は摂氏 30 度未満です", t),
        Temperature::Fahrenheit(t) if t > 86 => println!("{}F は華氏 86 度を超えています", t),
        Temperature::Fahrenheit(t) => println!("{}F は華氏 86 度未満です", t),
    }
}
```

マッチ式によってすべてのパターンがカバーされているかどうかをチェックする際に、コンパイラはガード条件を考慮しません。

```rust
fn main() {
    let number: u8 = 4;
    match number {
        i if i == 0 => println!("Zero"),
        i if i > 0 => println!("Greater than zero"),
        // _ => unreachable!("Should never happen."),
        // TODO ^ これをコメントアウトしてコンパイルを修正してください
    }
}
```
