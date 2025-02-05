# 解构枚举

在本书中我们已经对枚举进行了解构（例如，清单6-5），但我们尚未明确讨论解构枚举的模式与枚举中存储的数据的定义方式相对应。例如，在清单18-15中，我们使用清单6-2中的 `Message` 枚举，并编写一个 `match` 语句，其中的模式将解构每个内部值。

文件名：`src/main.rs`

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

fn main() {
  1 let msg = Message::ChangeColor(0, 160, 255);

    match msg {
      2 Message::Quit => {
            println!(
                "The Quit variant has no data to destructure."
            );
        }
      3 Message::Move { x, y } => {
            println!(
                "Move in the x dir {x}, in the y dir {y}"
            );
        }
      4 Message::Write(text) => {
            println!("Text message: {text}");
        }
      5 Message::ChangeColor(r, g, b) => println!(
            "Change color to red {r}, green {g}, and blue {b}"
        ),
    }
}
```

清单18-15：解构包含不同类型值的枚举变体

这段代码将打印 `Change color to red 0, green 160, and blue 255`。尝试更改 `msg` 的值 \[1\]，以查看其他分支的代码运行情况。

对于没有任何数据的枚举变体，比如 `Message::Quit` \[2\]，我们无法进一步解构该值。我们只能匹配字面量 `Message::Quit` 值，并且该模式中没有变量。

对于类似结构体的枚举变体，比如 `Message::Move` \[3\]，我们可以使用与匹配结构体时指定的模式类似的模式。在变体名称之后，我们放置花括号，然后列出带有变量的字段，这样我们就可以拆解这些部分以便在该分支的代码中使用。这里我们使用了与清单18-13中相同的简写形式。

对于类似元组的枚举变体，比如包含一个元素的元组的 `Message::Write` \[4\] 和包含三个元素的元组的 `Message::ChangeColor` \[5\]，模式与我们指定用于匹配元组的模式类似。模式中的变量数量必须与我们正在匹配的变体中的元素数量相匹配。
