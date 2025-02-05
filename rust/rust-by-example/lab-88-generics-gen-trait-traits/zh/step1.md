# 特性

当然，`trait` 也可以是泛型的。这里我们定义了一个 `trait`，它将 `Drop` `trait` 重新实现为一个泛型方法，用于释放自身和一个输入。

```rust
// 不可复制类型。
struct Empty;
struct Null;

// 一个以 `T` 为泛型的 `trait`。
trait DoubleDrop<T> {
    // 在调用者类型上定义一个方法，该方法接受一个
    // 额外的单参数 `T`，但不对其进行任何操作。
    fn double_drop(self, _: T);
}

// 为任何泛型参数 `T` 和调用者 `U` 实现 `DoubleDrop<T>`。
impl<T, U> DoubleDrop<T> for U {
    // 此方法获取两个传入参数的所有权，
    // 并释放两者。
    fn double_drop(self, _: T) {}
}

fn main() {
    let empty = Empty;
    let null  = Null;

    // 释放 `empty` 和 `null`。
    empty.double_drop(null);

    //empty;
    //null;
    // ^ TODO: 尝试取消注释这些行。
}
```
