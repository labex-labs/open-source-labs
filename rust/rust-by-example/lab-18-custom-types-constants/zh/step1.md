# 常量

Rust 有两种不同类型的常量，它们可以在包括全局作用域在内的任何作用域中声明。两者都需要显式的类型注释：

- `const`：一个不可变的值（常见情况）。
- `static`：一个可能可变的具有 `'static` 生命周期的变量。静态生命周期是推断出来的，不必指定。访问或修改可变的静态变量是 `unsafe` 的。

```rust
// 全局变量在所有其他作用域之外声明。
static LANGUAGE: &str = "Rust";
const THRESHOLD: i32 = 10;

fn is_big(n: i32) -> bool {
    // 在某个函数中访问常量
    n > THRESHOLD
}

fn main() {
    let n = 16;

    // 在主线程中访问常量
    println!("This is {}", LANGUAGE);
    println!("The threshold is {}", THRESHOLD);
    println!("{} is {}", n, if is_big(n) { "big" } else { "small" });

    // 错误！不能修改 `const`。
    THRESHOLD = 5;
    // FIXME ^ 注释掉这一行
}
```
