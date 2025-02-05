# 测试用例：空约束条件

约束条件的工作方式带来的一个结果是，即使一个 `trait` 不包含任何功能，你仍然可以将其用作约束条件。`Eq` 和 `Copy` 就是 `std` 库中这类 `trait` 的示例。

```rust
struct Cardinal;
struct BlueJay;
struct Turkey;

trait Red {}
trait Blue {}

impl Red for Cardinal {}
impl Blue for BlueJay {}

// 这些函数仅对实现了这些
// trait 的类型有效。这些 trait 为空这一事实无关紧要。
fn red<T: Red>(_: &T)   -> &'static str { "red" }
fn blue<T: Blue>(_: &T) -> &'static str { "blue" }

fn main() {
    let cardinal = Cardinal;
    let blue_jay = BlueJay;
    let _turkey   = Turkey;

    // 由于约束条件，`red()` 对冠蓝鸦不起作用，反之亦然
    println!("一只主红雀是 {}", red(&cardinal));
    println!("一只冠蓝鸦是 {}", blue(&blue_jay));
    //println!("一只火鸡是 {}", red(&_turkey));
    // ^ TODO：尝试取消注释这一行。
}
```
