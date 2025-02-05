# use

`use` 声明可用于无需手动作用域：

```rust
// 一个用于隐藏未使用代码警告的属性。
#![allow(dead_code)]

enum Status {
    Rich,
    Poor,
}

enum Work {
    Civilian,
    Soldier,
}

fn main() {
    // 显式地 `use` 每个名称，这样它们无需手动作用域即可使用。
    use crate::Status::{Poor, Rich};
    // 自动 `use` `Work` 中的每个名称。
    use crate::Work::*;

    // 等同于 `Status::Poor`。
    let status = Poor;
    // 等同于 `Work::Civilian`。
    let work = Civilian;

    match status {
        // 注意由于上面的显式 `use`，这里无需作用域。
        Rich => println!("The rich have lots of money!"),
        Poor => println!("The poor have no money..."),
    }

    match work {
        // 再次注意这里无需作用域。
        Civilian => println!("Civilians work!"),
        Soldier  => println!("Soldiers fight!"),
    }
}
```
