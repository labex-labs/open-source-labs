# Debug

`std::fmt` のフォーマット `特性` を使用したいすべての型は、表示可能な実装が必要です。自動実装は、`std` ライブラリのような型にのみ提供されます。その他のすべての型は、何らかの方法で手動で実装する必要があります。

`fmt::Debug` `特性` はこれを非常に簡単にします。すべての型は、`fmt::Debug` の実装を `派生`（自動的に作成）できます。これは、手動で実装する必要がある `fmt::Display` には当てはまりません。

```rust
// この構造体は、`fmt::Display` でも `fmt::Debug` でも表示できません。
struct UnPrintable(i32);

// `derive` 属性は、この `構造体` を `fmt::Debug` で表示可能にするために必要な実装を自動的に作成します。
#[derive(Debug)]
struct DebugPrintable(i32);
```

すべての `std` ライブラリの型も、`{:?}` で自動的に表示可能です：

```rust
// `Structure` に対して `fmt::Debug` の実装を派生させます。`Structure` は、1つの `i32` を含む構造体です。
#[derive(Debug)]
struct Structure(i32);

// `Deep` という構造体の中に `Structure` を入れます。これも表示可能にします。
#[derive(Debug)]
struct Deep(Structure);

fn main() {
    // `{:?}` を使った表示は、`{}` を使った場合と似ています。
    println!("{:?} months in a year.", 12);
    println!("{1:?} {0:?} is the {actor:?} name.",
             "Slater",
             "Christian",
             actor="actor's");

    // `Structure` は表示可能です！
    println!("Now {:?} will print!", Structure(3));

    // `derive` の問題は、結果の見た目を制御できないことです。もし私がこれがただの `7` を表示したいのであればどうすればいいでしょうか？
    println!("Now {:?} will print!", Deep(Structure(7)));
}
```

ですから、`fmt::Debug` は確かにこれを表示可能にしますが、ある程度のエレガンスを犠牲にします。Rust はまた、`{:#?}` を使った「見やすい表示」も提供しています。

```rust
#[derive(Debug)]
struct Person<'a> {
    name: &'a str,
    age: u8
}

fn main() {
    let name = "Peter";
    let age = 27;
    let peter = Person { name, age };

    // 見やすい表示
    println!("{:#?}", peter);
}
```

表示を制御するために、`fmt::Display` を手動で実装することができます。
