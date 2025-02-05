# 使用 `..` 忽略值的其余部分

对于具有多个部分的值，我们可以使用 `..` 语法来使用特定部分并忽略其余部分，这样就无需为每个要忽略的值列出下划线。`..` 模式会忽略我们在模式的其余部分未明确匹配的任何值的部分。在清单18-23中，我们有一个 `Point` 结构体，它表示三维空间中的一个坐标。在 `match` 表达式中，我们只想对 `x` 坐标进行操作，并忽略 `y` 和 `z` 字段中的值。

文件名：`src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
    z: i32,
}

let origin = Point { x: 0, y: 0, z: 0 };

match origin {
    Point { x,.. } => println!("x is {x}"),
}
```

清单18-23：通过使用 `..` 忽略 `Point` 结构体中除 `x` 之外的所有字段

我们列出 `x` 值，然后只包含 `..` 模式。这比必须列出 `y: _` 和 `z: _` 要快，特别是当我们处理具有许多字段的结构体，而只有一两个字段相关的情况时。

`..` 语法会扩展到所需的任意多个值。清单18-24展示了如何在元组中使用 `..`。

文件名：`src/main.rs`

```rust
fn main() {
    let numbers = (2, 4, 8, 16, 32);

    match numbers {
        (first,.., last) => {
            println!("Some numbers: {first}, {last}");
        }
    }
}
```

清单18-24：仅匹配元组中的第一个和最后一个值，并忽略所有其他值

在这段代码中，第一个和最后一个值分别与 `first` 和 `last` 匹配。`..` 会匹配并忽略中间的所有内容。

然而，使用 `..` 必须是明确的。如果不清楚哪些值用于匹配，哪些值应被忽略，Rust会给我们一个错误。清单18-25展示了使用 `..` 不明确的示例，因此它不会编译。

文件名：`src/main.rs`

```rust
fn main() {
    let numbers = (2, 4, 8, 16, 32);

    match numbers {
        (.., second,..) => {
            println!("Some numbers: {second}");
        },
    }
}
```

清单18-25：以不明确的方式尝试使用 `..`

当我们编译这个示例时，会得到以下错误：

```bash
error: `..` can only be used once per tuple pattern
 --> src/main.rs:5:22
  |
5 |         (.., second,..) => {
  |          --          ^^ can only be used once per tuple pattern
  |          |
  |          previously used here
```

Rust无法确定在将一个值与 `second` 匹配之前要忽略元组中的多少个值，以及在那之后还要忽略多少个值。这段代码可能意味着我们想忽略 `2`，将 `second` 绑定到 `4`，然后忽略 `8`、`16` 和 `32`；或者我们想忽略 `2` 和 `4`，将 `second` 绑定到 `8`，然后忽略 `16` 和 `32`；等等。变量名 `second` 对Rust来说没有什么特殊含义，所以我们会得到一个编译器错误，因为像这样在两个地方使用 `..` 是不明确的。
