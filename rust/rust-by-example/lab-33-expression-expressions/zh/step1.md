# 表达式

Rust 程序（主要）由一系列语句组成：

```rust
fn main() {
    // 语句
    // 语句
    // 语句
}
```

Rust 中有几种语句。最常见的两种是声明变量绑定，以及在表达式后使用 `;`：

```rust
fn main() {
    // 变量绑定
    let x = 5;

    // 表达式;
    x;
    x + 1;
    15;
}
```

代码块也是表达式，所以它们可以在赋值中用作值。代码块中的最后一个表达式将被赋给诸如局部变量这样的位置表达式。然而，如果代码块的最后一个表达式以分号结尾，返回值将是 `()`。

```rust
fn main() {
    let x = 5u32;

    let y = {
        let x_squared = x * x;
        let x_cube = x_squared * x;

        // 这个表达式将被赋给 `y`
        x_cube + x_squared + x
    };

    let z = {
        // 分号抑制了这个表达式，`()` 被赋给 `z`
        2 * x;
    };

    println!("x is {:?}", x);
    println!("y is {:?}", y);
    println!("z is {:?}", z);
}
```
