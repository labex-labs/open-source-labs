# 带有更多参数的方法

让我们通过在 `Rectangle` 结构体上实现第二个方法来练习使用方法。这次我们希望 `Rectangle` 的一个实例接受另一个 `Rectangle` 实例，并在第二个 `Rectangle` 能够完全放入 `self`（第一个 `Rectangle`）时返回 `true`；否则，返回 `false`。也就是说，一旦我们定义了 `can_hold` 方法，我们希望能够编写如清单 5-14 所示的程序。

文件名：`src/main.rs`

```rust
fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };
    let rect2 = Rectangle {
        width: 10,
        height: 40,
    };
    let rect3 = Rectangle {
        width: 60,
        height: 45,
    };

    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
    println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));
}
```

清单 5-14：使用尚未编写的 `can_hold` 方法

预期输出如下，因为 `rect2` 的两个维度都小于 `rect1` 的维度，但 `rect3` 比 `rect1` 宽：

```rust
Can rect1 hold rect2? true
Can rect1 hold rect3? false
```

我们知道要定义一个方法，所以它将在 `impl Rectangle` 块内。方法名是 `can_hold`，它将接受另一个 `Rectangle` 的不可变借用作为参数。通过查看调用该方法的代码，我们可以知道参数的类型：`rect1.can_hold(&rect2)` 传入了 `&rect2`，这是对 `rect2`（一个 `Rectangle` 实例）的不可变借用。这是有道理的，因为我们只需要读取 `rect2`（而不是写入，这意味着我们需要一个可变借用），并且我们希望 `main` 保留对 `rect2` 的所有权，以便在调用 `can_hold` 方法后再次使用它。`can_hold` 的返回值将是一个布尔值，并且实现将检查 `self` 的宽度和高度是否分别大于另一个 `Rectangle` 的宽度和高度。让我们将新的 `can_hold` 方法添加到清单 5-13 的 `impl` 块中，如清单 5-15 所示。

文件名：`src/main.rs`

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

清单 5-15：在 `Rectangle` 上实现接受另一个 `Rectangle` 实例作为参数的 `can_hold` 方法

当我们使用清单 5-14 中的 `main` 函数运行此代码时，我们将得到期望的输出。方法可以接受多个参数，我们在 `self` 参数之后将它们添加到签名中，并且这些参数的工作方式与函数中的参数相同。
