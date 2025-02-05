# 定义 Post 并创建处于草稿状态的新实例

让我们开始实现这个库吧！我们知道我们需要一个公共的 `Post` 结构体来保存一些内容，所以我们将从结构体的定义和一个相关的公共 `new` 函数开始，用于创建 `Post` 的实例，如清单 17-12 所示。我们还将创建一个私有的 `State` trait，它将定义 `Post` 的所有状态对象必须具备的行为。

然后，`Post` 将在一个名为 `state` 的私有字段中，在 `Option<T>` 内部持有一个 `Box<dyn State>` 的 trait 对象，以保存状态对象。稍后你会明白为什么需要 `Option<T>`。

文件名：`src/lib.rs`

```rust
pub struct Post {
    state: Option<Box<dyn State>>,
    content: String,
}

impl Post {
    pub fn new() -> Post {
        Post {
          1 state: Some(Box::new(Draft {})),
          2 content: String::new(),
        }
    }
}

trait State {}

struct Draft {}

impl State for Draft {}
```

清单 17-12：`Post` 结构体和创建新 `Post` 实例的 `new` 函数的定义，`State` trait 和 `Draft` 结构体

`State` trait 定义了不同文章状态共享的行为。状态对象有 `Draft`、`PendingReview` 和 `Published`，它们都将实现 `State` trait。目前，这个 trait 没有任何方法，我们将从定义 `Draft` 状态开始，因为这是文章开始时的状态。

当我们创建一个新的 `Post` 时，我们将其 `state` 字段设置为一个包含 `Box` 的 `Some` 值\[1\]。这个 `Box` 指向 `Draft` 结构体的一个新实例。这确保了每当我们创建一个新的 `Post` 实例时，它将以草稿状态开始。因为 `Post` 的 `state` 字段是私有的，所以没有办法以任何其他状态创建 `Post`！在 `Post::new` 函数中，我们将 `content` 字段设置为一个新的空 `String`\[2\]。
