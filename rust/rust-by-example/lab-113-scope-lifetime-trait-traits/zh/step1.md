# Traits

trait 方法中生命周期的标注基本上与函数类似。请注意，`impl` 也可能有生命周期标注。

```rust
// 一个带有生命周期标注的结构体。
#[derive(Debug)]
struct Borrowed<'a> {
    x: &'a i32,
}

// 为 impl 标注生命周期。
impl<'a> Default for Borrowed<'a> {
    fn default() -> Self {
        Self {
            x: &10,
        }
    }
}

fn main() {
    let b: Borrowed = Default::default();
    println!("b is {:?}", b);
}
```
