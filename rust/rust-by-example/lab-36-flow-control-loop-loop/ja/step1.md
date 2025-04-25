# loop

Rust では、無限ループを示すために`loop`キーワードが用意されています。

`break`文を使うと、いつでもループを抜けることができます。一方、`continue`文を使うと、その反復処理の残りをスキップして新しい反復処理を開始できます。

```rust
fn main() {
    let mut count = 0u32;

    println!("Let's count until infinity!");

    // 無限ループ
    loop {
        count += 1;

        if count == 3 {
            println!("three");

            // この反復処理の残りをスキップ
            continue;
        }

        println!("{}", count);

        if count == 5 {
            println!("OK, that's enough");

            // このループを抜ける
            break;
        }
    }
}
```
