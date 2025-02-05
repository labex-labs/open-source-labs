# 循环

Rust 提供了一个 `loop` 关键字来表示无限循环。

`break` 语句可用于在任何时候退出循环，而 `continue` 语句可用于跳过剩余的迭代并开始新的迭代。

```rust
fn main() {
    let mut count = 0u32;

    println!("让我们一直数到无穷大！");

    // 无限循环
    loop {
        count += 1;

        if count == 3 {
            println!("三");

            // 跳过本次迭代的剩余部分
            continue;
        }

        println!("{}", count);

        if count == 5 {
            println!("好的，够了");

            // 退出此循环
            break;
        }
    }
}
```
