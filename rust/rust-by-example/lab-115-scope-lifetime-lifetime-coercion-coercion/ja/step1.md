# 強制変換

長いライフタイムを短いライフタイムに強制変換することができ、通常は機能しないスコープ内で機能するようになります。これは、Rust コンパイラによる推論による強制変換の形で、またライフタイムの違いを宣言する形でもあります。

```rust
// ここでは、Rust ができる限り短いライフタイムを推論します。
// その後、2 つの参照はそのライフタイムに強制変換されます。
fn multiply<'a>(first: &'a i32, second: &'a i32) -> i32 {
    first * second
}

// `<'a: 'b, 'b>` は、ライフタイム `'a` が `'b` と同じくらい長いことを意味します。
// ここでは、`&'a i32` を受け取り、強制変換の結果として `&'b i32` を返します。
fn choose_first<'a: 'b, 'b>(first: &'a i32, _: &'b i32) -> &'b i32 {
    first
}

fn main() {
    let first = 2; // より長いライフタイム

    {
        let second = 3; // より短いライフタイム

        println!("The product is {}", multiply(&first, &second));
        println!("{} is the first", choose_first(&first, &second));
    };
}
```
