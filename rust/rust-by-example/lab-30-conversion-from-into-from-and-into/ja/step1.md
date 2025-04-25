# `From` と `Into`

[`From`](#from) と [`Into`](#into) トレイトは本質的に関連付けられており、これは実際にその実装の一部です。型 A を型 B から変換できる場合、型 B を型 A に変換できるはずだと考えるのは簡単です。

## `From`

[`From`](#from) トレイトは、型が別の型から自身を作成する方法を定義することを可能にし、いくつかの型間の変換に非常に単純なメカニズムを提供します。標準ライブラリ内には、基本型と一般的な型の変換に対するこのトレイトの多数の実装があります。

たとえば、`str` を `String` に簡単に変換できます。

```rust
let my_str = "hello";
let my_string = String::from(my_str);
```

独自の型の変換を定義する場合も同様にできます。

```rust
use std::convert::From;

#[derive(Debug)]
struct Number {
    value: i32,
}

impl From<i32> for Number {
    fn from(item: i32) -> Self {
        Number { value: item }
    }
}

fn main() {
    let num = Number::from(30);
    println!("My number is {:?}", num);
}
```

## `Into`

[`Into`](#into) トレイトは、単に `From` トレイトの逆です。つまり、型に対して `From` トレイトを実装している場合、`Into` は必要に応じてそれを呼び出します。

`Into` トレイトを使用する場合、通常は変換先の型を指定する必要があります。なぜなら、コンパイラはほとんどの場合これを判断できないからです。ただし、この機能を無料で得られることを考えると、これは小さなトレードオフにすぎません。

```rust
use std::convert::Into;

#[derive(Debug)]
struct Number {
    value: i32,
}

impl Into<Number> for i32 {
    fn into(self) -> Number {
        Number { value: self }
    }
}

fn main() {
    let int = 5;
    // 型注釈を削除してみてください
    let num: Number = int.into();
    println!("My number is {:?}", num);
}
```
