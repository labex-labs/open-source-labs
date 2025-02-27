# スコープとシャドーイング

変数束縛にはスコープがあり、それは _ブロック_ 内に存在するように制限されます。ブロックは、波括弧 `{}` で囲まれた文のコレクションです。

```rust
fn main() {
    // この束縛は main 関数内に存在します
    let long_lived_binding = 1;

    // これはブロックであり、main 関数よりも小さなスコープを持っています
    {
        // この束縛はこのブロック内にのみ存在します
        let short_lived_binding = 2;

        println!("inner short: {}", short_lived_binding);
    }
    // ブロックの終わり

    // エラー！`short_lived_binding` はこのスコープ内に存在しません
    println!("outer short: {}", short_lived_binding);
    // FIXME ^ この行をコメントアウトしてください

    println!("outer long: {}", long_lived_binding);
}
```

また、変数のシャドーイングも許されています。

```rust
fn main() {
    let shadowed_binding = 1;

    {
        println!("before being shadowed: {}", shadowed_binding);

        // この束縛は外側の束縛を *シャドーイング* します
        let shadowed_binding = "abc";

        println!("shadowed in inner block: {}", shadowed_binding);
    }
    println!("outside inner block: {}", shadowed_binding);

    // この束縛は前の束縛を *シャドーイング* します
    let shadowed_binding = 2;
    println!("shadowed in outer block: {}", shadowed_binding);
}
```
