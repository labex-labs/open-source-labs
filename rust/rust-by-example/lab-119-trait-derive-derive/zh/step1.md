# 通过 `#[derive]` 实现

编译器能够通过 `#[derive]` 属性为某些 trait 提供基本实现。如果需要更复杂的行为，这些 trait 仍然可以手动实现。

以下是可通过 `#[derive]` 实现的 trait 列表：

- 比较 trait：`Eq`、`PartialEq`、`Ord`、`PartialOrd`。
- `Clone`，用于通过复制从 `&T` 创建 `T`。
- `Copy`，用于赋予类型“复制语义”而非“移动语义”。
- `Hash`，用于从 `&T` 计算哈希值。
- `Default`，用于创建数据类型的空实例。
- `Debug`，用于使用 `{:?}` 格式化器格式化值。

```rust
// `Centimeters`，一个可比较的元组结构体
#[derive(PartialEq, PartialOrd)]
struct Centimeters(f64);

// `Inches`，一个可打印的元组结构体
#[derive(Debug)]
struct Inches(i32);

impl Inches {
    fn to_centimeters(&self) -> Centimeters {
        let &Inches(inches) = self;

        Centimeters(inches as f64 * 2.54)
    }
}

// `Seconds`，一个没有附加属性的元组结构体
struct Seconds(i32);

fn main() {
    let _one_second = Seconds(1);

    // 错误：`Seconds` 不可打印；它没有实现 `Debug` trait
    //println!("One second looks like: {:?}", _one_second);
    // TODO ^ 尝试取消注释这一行

    // 错误：`Seconds` 不可比较；它没有实现 `PartialEq` trait
    //let _this_is_true = (_one_second == _one_second);
    // TODO ^ 尝试取消注释这一行

    let foot = Inches(12);

    println!("One foot equals {:?}", foot);

    let meter = Centimeters(100.0);

    let cmp =
        if foot.to_centimeters() < meter {
            "smaller"
        } else {
            "bigger"
        };

    println!("One foot is {} than one meter.", cmp);
}
```
