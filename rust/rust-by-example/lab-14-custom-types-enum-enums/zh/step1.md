# 枚举

`enum` 关键字允许创建一种类型，它可以是几种不同变体之一。任何作为 `struct` 有效的变体在 `enum` 中也同样有效。

```rust
// 创建一个 `enum` 来对网页事件进行分类。注意名称和类型信息如何共同指定变体：
// `PageLoad!= PageUnload` 且 `KeyPress(char)!= Paste(String)`。
// 每个变体都是不同且独立的。
enum WebEvent {
    // 一个 `enum` 变体可以是类似单元类型的，
    PageLoad,
    PageUnload,
    // 类似元组结构体的，
    KeyPress(char),
    Paste(String),
    // 或者是类 C 结构体。
    Click { x: i64, y: i64 },
}

// 一个函数，它接受一个 `WebEvent` 枚举作为参数并且
// 不返回任何值。
fn inspect(event: WebEvent) {
    match event {
        WebEvent::PageLoad => println!("页面已加载"),
        WebEvent::PageUnload => println!("页面已卸载"),
        // 从 `enum` 变体内部解构出 `c`。
        WebEvent::KeyPress(c) => println!("按下了 '{}'。", c),
        WebEvent::Paste(s) => println!("粘贴了 \"{}\"。", s),
        // 将 `Click` 解构为 `x` 和 `y`。
        WebEvent::Click { x, y } => {
            println!("在 x={}, y={} 处点击。", x, y);
        },
    }
}

fn main() {
    let pressed = WebEvent::KeyPress('x');
    // `to_owned()` 从字符串切片创建一个拥有所有权的 `String`。
    let pasted  = WebEvent::Paste("我的文本".to_owned());
    let click   = WebEvent::Click { x: 20, y: 80 };
    let load    = WebEvent::PageLoad;
    let unload  = WebEvent::PageUnload;

    inspect(pressed);
    inspect(pasted);
    inspect(click);
    inspect(load);
    inspect(unload);
}
```

## 类型别名

如果你使用类型别名，你可以通过其别名来引用每个枚举变体。如果枚举的名称太长或太通用，而你想给它重命名，这可能会很有用。

```rust
enum VeryVerboseEnumOfThingsToDoWithNumbers {
    Add,
    Subtract,
}

// 创建一个类型别名
type Operations = VeryVerboseEnumOfThingsToDoWithNumbers;

fn main() {
    // 我们可以通过其别名而不是冗长且不方便的
    // 名称来引用每个变体。
    let x = Operations::Add;
}
```

你最常看到这种情况的地方是在使用 `Self` 别名的 `impl` 块中。

```rust
enum VeryVerboseEnumOfThingsToDoWithNumbers {
    Add,
    Subtract,
}

impl VeryVerboseEnumOfThingsToDoWithNumbers {
    fn run(&self, x: i32, y: i32) -> i32 {
        match self {
            Self::Add => x + y,
            Self::Subtract => x - y,
        }
    }
}
```

要了解有关枚举和类型别名的更多信息，你可以阅读此功能在 Rust 中稳定时的稳定报告。
