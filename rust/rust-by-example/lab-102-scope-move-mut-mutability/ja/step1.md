# 可変性

所有権が移されるとき、データの可変性は変更できます。

```rust
fn main() {
    let immutable_box = Box::new(5u32);

    println!("immutable_box contains {}", immutable_box);

    // 可変性エラー
    //*immutable_box = 4;

    // ボックスを *移動* して、所有権（および可変性）を変更します
    let mut mutable_box = immutable_box;

    println!("mutable_box contains {}", mutable_box);

    // ボックスの内容を変更します
    *mutable_box = 4;

    println!("mutable_box now contains {}", mutable_box);
}
```
