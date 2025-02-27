# HashMap

ベクターは整数インデックスで値を格納するのに対し、`HashMap` はキーで値を格納します。`HashMap` のキーは、ブール値、整数、文字列、または `Eq` と `Hash` トレイトを実装する他の任意の型であることができます。次のセクションでこれについてもっと詳しく説明します。

ベクターと同様に、`HashMap` は拡張可能ですが、余分な空間がある場合には `HashMap` 自身も縮小することができます。`HashMap::with_capacity(uint)` を使って特定の初期容量で `HashMap` を作成することもできますし、デフォルトの初期容量で `HashMap` を取得するには `HashMap::new()` を使います（推奨）。

```rust
use std::collections::HashMap;

fn call(number: &str) -> &str {
    match number {
        "798-1364" => "We're sorry, the call cannot be completed as dialed.
            Please hang up and try again.",
        "645-7689" => "Hello, this is Mr. Awesome's Pizza. My name is Fred.
            What can I get for you today?",
        _ => "Hi! Who is this again?"
    }
}

fn main() {
    let mut contacts = HashMap::new();

    contacts.insert("Daniel", "798-1364");
    contacts.insert("Ashley", "645-7689");
    contacts.insert("Katie", "435-8291");
    contacts.insert("Robert", "956-1745");

    // 参照を取り、Option<&V> を返す
    match contacts.get(&"Daniel") {
        Some(&number) => println!("Calling Daniel: {}", call(number)),
        _ => println!("Don't have Daniel's number."),
    }

    // `HashMap::insert()` は、挿入される値が新しい場合には `None` を返し、
    // それ以外の場合には `Some(value)` を返します
    contacts.insert("Daniel", "164-6743");

    match contacts.get(&"Ashley") {
        Some(&number) => println!("Calling Ashley: {}", call(number)),
        _ => println!("Don't have Ashley's number."),
    }

    contacts.remove(&"Ashley");

    // `HashMap::iter()` は、(&'a key, &'a value) のペアを任意の順序で返すイテレータを返します。
    for (contact, &number) in contacts.iter() {
        println!("Calling {}: {}", contact, call(number));
    }
}
```

ハッシュ化とハッシュマップ（時々ハッシュテーブルと呼ばれます）の仕組みに関する詳細は、Hash Table Wikipedia を参照してください。
