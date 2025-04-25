# 无效的数组元素访问

让我们看看如果你试图访问超出数组末尾的元素会发生什么。假设你运行这段类似于第 2 章猜数字游戏的代码，从用户那里获取一个数组索引：

文件名：`src/main.rs`

```rust
use std::io;

fn main() {
    let a = [1, 2, 3, 4, 5];

    println!("请输入一个数组索引。");

    let mut index = String::new();

    io::stdin()
     .read_line(&mut index)
     .expect("读取行失败");

    let index: usize = index
     .trim()
     .parse()
     .expect("输入的索引不是一个数字");

    let element = a[index];

    println!(
        "索引 {index} 处的元素值是：{element}"
    );
}
```

这段代码编译成功。如果你使用 `cargo run` 运行这段代码并输入 `0`、`1`、`2`、`3` 或 `4`，程序将打印出数组中该索引处的对应值。如果你输入一个超出数组末尾的数字，比如 `10`，你会看到如下输出：

    thread'main' panicked at 'index out of bounds: the len is 5 but the index is
    10', src/main.rs:19:19
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

程序在索引操作中使用无效值时导致了一个**运行时**错误。程序带着错误信息退出，没有执行最后的 `println!` 语句。当你试图使用索引访问元素时，Rust 会检查你指定的索引是否小于数组长度。如果索引大于或等于数组长度，Rust 将会 `panic`。这个检查必须在运行时进行，特别是在这种情况下，因为编译器不可能知道用户在运行代码时会输入什么值。

这是 Rust 内存安全原则起作用的一个例子。在许多低级语言中，不会进行这种检查，当你提供一个错误的索引时，可能会访问无效内存。Rust 通过立即退出而不是允许内存访问并继续来保护你免受这种错误的影响。第 9 章将讨论更多关于 Rust 的错误处理，以及如何编写既不会 `panic` 也不会允许无效内存访问的可读、安全的代码。
