# 实现 trait

现在我们将添加一些实现 `Draw` trait 的类型。我们将提供 `Button` 类型。同样，实际实现一个 GUI 库超出了本书的范围，所以 `draw` 方法在其主体中不会有任何有用的实现。为了想象实现可能是什么样的，一个 `Button` 结构体可能有 `width`、`height` 和 `label` 字段，如清单 17-7 所示。

文件名：`src/lib.rs`

```rust
pub struct Button {
    pub width: u32,
    pub height: u32,
    pub label: String,
}

impl Draw for Button {
    fn draw(&self) {
        // 实际绘制按钮的代码
    }
}
```

清单 17-7：实现 `Draw` trait 的 `Button` 结构体

`Button` 上的 `width`、`height` 和 `label` 字段将与其他组件上的字段不同；例如，`TextField` 类型可能有相同的这些字段再加上一个 `placeholder` 字段。我们想要在屏幕上绘制的每种类型都将实现 `Draw` trait，但会在 `draw` 方法中使用不同的代码来定义如何绘制该特定类型，就像这里的 `Button` 一样（如前所述，没有实际的 GUI 代码）。例如，`Button` 类型可能有一个额外的 `impl` 块，包含与用户点击按钮时发生的事情相关的方法。这些类型的方法不适用于 `TextField` 之类的类型。

如果使用我们库的人决定实现一个有 `width`、`height` 和 `options` 字段的 `SelectBox` 结构体，他们也会在 `SelectBox` 类型上实现 `Draw` trait，如清单 17-8 所示。

文件名：`src/main.rs`

```rust
use gui::Draw;

struct SelectBox {
    width: u32,
    height: u32,
    options: Vec<String>,
}

impl Draw for SelectBox {
    fn draw(&self) {
        // 实际绘制选择框的代码
    }
}
```

清单 17-8：另一个使用 `gui` 并在 `SelectBox` 结构体上实现 `Draw` trait 的 crate

我们库的用户现在可以编写他们的 `main` 函数来创建一个 `Screen` 实例。对于 `Screen` 实例，他们可以通过将每个组件放入 `Box<T>` 中以成为 trait 对象的方式来添加一个 `SelectBox` 和一个 `Button`。然后他们可以在 `Screen` 实例上调用 `run` 方法，该方法将对每个组件调用 `draw` 方法。清单 17-9 展示了这个实现。

文件名：`src/main.rs`

```rust
use gui::{Button, Screen};

fn main() {
    let screen = Screen {
        components: vec![
            Box::new(SelectBox {
                width: 75,
                height: 10,
                options: vec![
                    String::from("Yes"),
                    String::from("Maybe"),
                    String::from("No"),
                ],
            }),
            Box::new(Button {
                width: 50,
                height: 10,
                label: String::from("OK"),
            }),
        ],
    };

    screen.run();
}
```

清单 17-9：使用 trait 对象来存储实现相同 trait 的不同类型的值

当我们编写库时，我们不知道有人可能会添加 `SelectBox` 类型，但我们的 `Screen` 实现能够对新类型进行操作并绘制它，因为 `SelectBox` 实现了 `Draw` trait，这意味着它实现了 `draw` 方法。

这种只关注值响应的消息而不是值的具体类型的概念，类似于动态类型语言中的“鸭子类型”概念：如果它走路像鸭子，叫声像鸭子，那么它一定是只鸭子！在清单 17-5 中 `Screen` 的 `run` 实现中，`run` 不需要知道每个组件的具体类型是什么。它不会检查一个组件是否是 `Button` 或 `SelectBox` 的实例，它只是对组件调用 `draw` 方法。通过将 `Box<dyn Draw>` 指定为 `components` 向量中值的类型，我们定义了 `Screen` 需要可以调用 `draw` 方法的值。

使用 trait 对象和 Rust 的类型系统来编写类似于使用鸭子类型编写的代码的优点是，我们永远不必在运行时检查一个值是否实现了特定方法，也不必担心如果一个值没有实现某个方法但我们仍然调用它会出错。如果值没有实现 trait 对象所需的 trait，Rust 不会编译我们的代码。

例如，清单 17-10 展示了如果我们尝试创建一个以 `String` 作为组件的 `Screen` 会发生什么。

文件名：`src/main.rs`

```rust
use gui::Screen;

fn main() {
    let screen = Screen {
        components: vec![Box::new(String::from("Hi"))],
    };

    screen.run();
}
```

清单 17-10：尝试使用未实现 trait 对象的 trait 的类型

我们会得到这个错误，因为 `String` 没有实现 `Draw` trait：

```bash
error[E0277]: the trait bound `String: Draw` is not satisfied
 --> src/main.rs:5:26
  |
5 |         components: vec![Box::new(String::from("Hi"))],
  |                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ the trait `Draw` is
not implemented for `String`
  |
  = note: required for the cast to the object type `dyn Draw`
```

这个错误让我们知道，要么我们向 `Screen` 传递了不应该传递的东西，所以应该传递不同的类型，要么我们应该在 `String` 上实现 `Draw` trait，以便 `Screen` 能够对其调用 `draw` 方法。
