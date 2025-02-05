# 可变性

当所有权转移时，数据的可变性可以改变。

```rust
fn main() {
    let immutable_box = Box::new(5u32);

    println!("immutable_box contains {}", immutable_box);

    // 可变性错误
    //*immutable_box = 4;

    // *移动* 这个盒子，改变所有权（以及可变性）
    let mut mutable_box = immutable_box;

    println!("mutable_box contains {}", mutable_box);

    // 修改盒子的内容
    *mutable_box = 4;

    println!("mutable_box now contains {}", mutable_box);
}
```
