# 文字列への変換と文字列からの変換

## 文字列への変換

任意の型を `String` に変換するには、その型に対して \[`ToString`\] トレイトを実装するだけです。直接そうする代わりに、`fmt::Display` トレイトを実装する方が良いでしょう。これは自動的に \[`ToString`\] を提供し、`print!` に関するセクションで説明したように、型を表示することも可能にします。

```rust
use std::fmt;

struct Circle {
    radius: i32
}

impl fmt::Display for Circle {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Circle of radius {}", self.radius)
    }
}

fn main() {
    let circle = Circle { radius: 6 };
    println!("{}", circle.to_string());
}
```

## 文字列の解析

文字列から数値に変換することは、より一般的なタスクの一つです。これに対する慣用的なアプローチは、 \[`parse`\] 関数を使って、型推論を行うか、'turbofish' 構文を使って解析する型を指定することです。両方の方法を以下の例に示します。

これは、その型に対して \[`FromStr`\] トレイトが実装されている限り、文字列を指定された型に変換します。これは標準ライブラリ内の多数の型に対して実装されています。ユーザー定義型でこの機能を得るには、その型に対して単に \[`FromStr`\] トレイトを実装します。

```rust
fn main() {
    let parsed: i32 = "5".parse().unwrap();
    let turbo_parsed = "10".parse::<i32>().unwrap();

    let sum = parsed + turbo_parsed;
    println!("Sum: {:?}", sum);
}
```
