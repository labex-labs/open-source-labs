# バインディング

変数に間接的にアクセスすると、再バインディングせずにその変数を分岐して使用することができなくなります。`match` は値を名前にバインドするための `@` シグイルを提供します。

```rust
// `u32` を返す関数 `age`。
fn age() -> u32 {
    15
}

fn main() {
    println!("Tell me what type of person you are");

    match age() {
        0             => println!("I haven't celebrated my first birthday yet"),
        // 1..= 12 を直接 `match` することもできますが、その場合子供の年齢は何になりますか？代わりに、1..= 12 のシーケンスに対して `n` にバインドします。これで年齢を報告できます。
        n @ 1 ..= 12 => println!("I'm a child of age {:?}", n),
        n @ 13..= 19 => println!("I'm a teen of age {:?}", n),
        // 何もバインドされていません。結果を返します。
        n             => println!("I'm an old person of age {:?}", n),
    }
}
```

また、`enum` のバリアント（たとえば `Option`）を「分解」するためにバインディングを使用することもできます。

```rust
fn some_number() -> Option<u32> {
    Some(42)
}

fn main() {
    match some_number() {
        // `Some` バリアントを取得し、その値が `n` にバインドされて 42 に等しい場合にマッチします。
        Some(n @ 42) => println!("The Answer: {}!", n),
        // その他の任意の数にマッチします。
        Some(n)      => println!("Not interesting... {}", n),
        // その他の何か（`None` バリアント）にマッチします。
        _            => (),
    }
}
```
