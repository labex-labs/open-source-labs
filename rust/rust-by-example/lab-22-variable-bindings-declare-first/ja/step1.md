# 先に宣言する

変数バインディングを先に宣言し、後で初期化することができます。ただし、この形式はほとんど使用されず、未初期化の変数が使用される可能性があるためです。

```rust
fn main() {
    // 変数バインディングを宣言する
    let a_binding;

    {
        let x = 2;

        // バインディングを初期化する
        a_binding = x * x;
    }

    println!("a binding: {}", a_binding);

    let another_binding;

    // エラー！未初期化のバインディングを使用しています
    println!("another binding: {}", another_binding);
    // FIXME ^ この行をコメントアウトする

    another_binding = 1;

    println!("another binding: {}", another_binding);
}
```

コンパイラは未初期化の変数の使用を禁止します。これは未定義の動作につながるためです。
