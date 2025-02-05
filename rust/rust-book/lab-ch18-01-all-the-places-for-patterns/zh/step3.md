# 条件 `if let` 表达式

在第 6 章中，我们讨论了如何使用 `if let` 表达式，主要是作为编写等效 `match` 的一种更简短的方式，该 `match` 只匹配一种情况。可选地，`if let` 可以有一个相应的 `else`，其中包含如果 `if let` 中的模式不匹配时要运行的代码。

清单 18-1 展示了也可以混合使用 `if let`、`else if` 和 `else if let` 表达式。这样做比 `match` 表达式给我们提供了更多的灵活性，在 `match` 表达式中我们只能表达一个要与模式进行比较的值。此外，Rust 并不要求一系列 `if let`、`else if` 和 `else if let` 分支中的条件相互关联。

清单 18-1 中的代码根据对几个条件的一系列检查来确定你的背景颜色应该是什么。对于这个示例，我们创建了一些带有硬编码值的变量，实际程序可能会从用户输入中获取这些值。

文件名：`src/main.rs`

```rust
fn main() {
    let favorite_color: Option<&str> = None;
    let is_tuesday = false;
    let age: Result<u8, _> = "34".parse();

    if let Some(color) = favorite_color {
        println!(
            "Using your favorite, {color}, as the background"
        );
    } else if is_tuesday {
        println!("Tuesday is green day!");
    } else if let Ok(age) = age {
        if age > 30 {
            println!("Using purple as the background color");
        } else {
            println!("Using orange as the background color");
        }
    } else {
        println!("Using blue as the background color");
    }
}
```

清单 18-1：混合使用 `if let`、`else if`、`else if let` 和 `else`

如果用户指定了最喜欢的颜色 \[1\]，那么该颜色将被用作背景 \[2\]。如果没有指定最喜欢的颜色且今天是星期二 \[3\]，则背景颜色为绿色 \[4\]。否则，如果用户将他们的年龄指定为字符串并且我们可以成功地将其解析为数字 \[5\]，那么根据数字的值，颜色要么是紫色 \[7\] 要么是橙色 \[8\] \[6\]。如果这些条件都不适用 \[9\]，则背景颜色为蓝色 \[10\]。

这种条件结构使我们能够支持复杂的需求。基于我们这里的硬编码值，这个示例将打印 `Using purple as the background color`。

你可以看到 `if let` 也可以像 `match` 分支一样引入遮蔽变量：`if let Ok(age) = age` 这一行 \[5\] 引入了一个新的被遮蔽的 `age` 变量，它包含 `Ok` 变体中的值。这意味着我们需要将 `if age > 30` 条件 \[6\] 放在该块内：我们不能将这两个条件组合成 `if let Ok(age) = age && age > 30`。我们想要与 30 进行比较的被遮蔽的 `age` 在新作用域以花括号开始之前是无效的。

使用 `if let` 表达式的缺点是编译器不会检查是否详尽无遗，而对于 `match` 表达式它会检查。如果我们省略了最后一个 `else` 块 \[9\]，从而遗漏了处理某些情况，编译器不会提醒我们可能存在的逻辑错误。
