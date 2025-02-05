# `Option`

有时，捕获程序某些部分的失败情况而不是调用 `panic!` 是很有必要的；这可以使用 `Option` 枚举来实现。

`Option<T>` 枚举有两个变体：

- `None`，表示失败或值缺失，以及
- `Some(value)`，一个元组结构体，它将一个类型为 `T` 的 `value` 包装起来。

```rust
// 一个不会 `panic!` 的整数除法
fn checked_division(dividend: i32, divisor: i32) -> Option<i32> {
    if divisor == 0 {
        // 失败用 `None` 变体表示
        None
    } else {
        // 结果包装在 `Some` 变体中
        Some(dividend / divisor)
    }
}

// 这个函数处理可能不成功的除法
fn try_division(dividend: i32, divisor: i32) {
    // `Option` 值可以像其他枚举一样进行模式匹配
    match checked_division(dividend, divisor) {
        None => println!("{} / {} 失败！", dividend, divisor),
        Some(quotient) => {
            println!("{} / {} = {}", dividend, divisor, quotient)
        },
    }
}

fn main() {
    try_division(4, 2);
    try_division(1, 0);

    // 将 `None` 绑定到变量需要进行类型注释
    let none: Option<i32> = None;
    let _equivalent_none = None::<i32>;

    let optional_float = Some(0f32);

    // 解包 `Some` 变体将提取包装的值。
    println!("{:?} 解包后为 {:?}", optional_float, optional_float.unwrap());

    // 解包 `None` 变体将导致 `panic!`
    println!("{:?} 解包后为 {:?}", none, none.unwrap());
}
```
