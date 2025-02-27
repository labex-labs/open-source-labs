# 可変性

変数バインディングは既定では不変ですが、`mut` 修飾子を使用してこれを上書きできます。

```rust
fn main() {
    let _immutable_binding = 1;
    let mut mutable_binding = 1;

    println!("変更前: {}", mutable_binding);

    // オッケー
    mutable_binding += 1;

    println!("変更後: {}", mutable_binding);

    // エラー！不変変数に新しい値を割り当てることはできません
    _immutable_binding += 1;
}
```

コンパイラは可変性エラーに関する詳細な診断を投げます。
