# match

Rust 通过 `match` 关键字提供模式匹配，它的用法类似于 C 语言中的 `switch`。会计算第一个匹配的分支，并且必须涵盖所有可能的值。

```rust
fn main() {
    let number = 13;
    // TODO ^ 尝试为 `number` 设置不同的值

    println!("告诉我关于 {}", number);
    match number {
        // 匹配单个值
        1 => println!("一！"),
        // 匹配多个值
        2 | 3 | 5 | 7 | 11 => println!("这是一个质数"),
        // TODO ^ 尝试将 13 添加到质数列表中
        // 匹配一个包含边界的范围
        13..=19 => println!("一个十几岁的数字"),
        // 处理其余情况
        _ => println!("没什么特别的"),
        // TODO ^ 尝试注释掉这个通配分支
    }

    let boolean = true;
    // match 也是一个表达式
    let binary = match boolean {
        // match 的分支必须涵盖所有可能的值
        false => 0,
        true => 1,
        // TODO ^ 尝试注释掉其中一个分支
    };

    println!("{} -> {}", boolean, binary);
}
```
