# `panic`

我们将看到的最简单的错误处理机制是 `panic`。它会打印一条错误消息，开始展开栈，并通常会退出程序。在这里，我们在错误条件下显式调用 `panic`：

```rust
fn drink(beverage: &str) {
    // 你不应饮用过多含糖饮料。
    if beverage == "lemonade" { panic!("AAAaaaaa!!!!"); }

    println!("Some refreshing {} is all I need.", beverage);
}

fn main() {
    drink("water");
    drink("lemonade");
}
```
