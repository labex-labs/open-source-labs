# 匹配字面量

正如你在第 6 章中看到的，你可以直接将模式与字面量进行匹配。以下代码给出了一些示例：

文件名：`src/main.rs`

```rust
let x = 1;

match x {
    1 => println!("one"),
    2 => println!("two"),
    3 => println!("three"),
    _ => println!("anything"),
}
```

这段代码会打印出 `one`，因为 `x` 中的值是 `1`。当你希望代码在获取到特定的具体值时执行某个操作时，这种语法很有用。
