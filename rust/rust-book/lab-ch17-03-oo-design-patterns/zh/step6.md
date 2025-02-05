# 添加 approve 以更改 content 的行为

`approve` 方法将类似于 `request_review` 方法：它会将 `state` 设置为当前状态在被批准时应有的值，如清单 17-16 所示。

文件名：`src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn approve(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.approve())
        }
    }
}

trait State {
    fn request_review(self: Box<Self>) -> Box<dyn State>;
    fn approve(self: Box<Self>) -> Box<dyn State>;
}

struct Draft {}

impl State for Draft {
    --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
      1 self
    }
}

struct PendingReview {}

impl State for PendingReview {
    --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
      2 Box::new(Published {})
    }
}

struct Published {}

impl State for Published {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        self
    }

    fn approve(self: Box<Self>) -> Box<dyn State> {
        self
    }
}
```

清单 17-16：在 `Post` 和 `State` trait 上实现 `approve` 方法

我们将 `approve` 方法添加到 `State` trait 中，并添加一个新的实现 `State` 的结构体，即 `Published` 状态。

类似于 `PendingReview` 上的 `request_review` 的工作方式，如果我们在 `Draft` 上调用 `approve` 方法，它将没有效果，因为 `approve` 将返回 `self`\[1\]。当我们在 `PendingReview` 上调用 `approve` 时，它会返回一个新的、装箱的 `Published` 结构体实例\[2\]。`Published` 结构体实现了 `State` trait，对于 `request_review` 方法和 `approve` 方法，它都返回自身，因为在这些情况下文章应该保持在 `Published` 状态。

现在我们需要更新 `Post` 上的 `content` 方法。我们希望 `content` 返回的值取决于 `Post` 的当前状态，所以我们将让 `Post` 委托给在其 `state` 上定义的 `content` 方法，如清单 17-17 所示。

文件名：`src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn content(&self) -> &str {
        self.state.as_ref().unwrap().content(self)
    }
    --snip--
}
```

清单 17-17：更新 `Post` 上的 `content` 方法以委托给 `State` 上的 `content` 方法

因为目标是将所有这些规则保留在实现 `State` 的结构体内部，所以我们在 `state` 中的值上调用 `content` 方法，并将文章实例（即 `self`）作为参数传递。然后我们返回在 `state` 值上使用 `content` 方法返回的值。

我们在 `Option` 上调用 `as_ref` 方法，因为我们想要 `Option` 内部值的引用而不是值的所有权。因为 `state` 是一个 `Option<Box<dyn State>>`，当我们调用 `as_ref` 时，会返回一个 `Option<&Box<dyn State>>`。如果我们不调用 `as_ref`，就会得到一个错误，因为我们不能从函数参数的借用 `&self` 中移出 `state`。

然后我们调用 `unwrap` 方法，我们知道它永远不会恐慌，因为我们知道 `Post` 上的方法确保在这些方法完成时 `state` 将始终包含一个 `Some` 值。这是我们在“你比编译器知道更多信息的情况”中讨论的情况之一，即我们知道 `None` 值永远不可能出现，即使编译器无法理解这一点。

此时，当我们在 `&Box<dyn State>` 上调用 `content` 时，解引用强制转换将对 `&` 和 `Box` 生效，所以最终将在实现 `State` trait 的类型上调用 `content` 方法。这意味着我们需要将 `content` 添加到 `State` trait 定义中，并且我们将在那里根据我们所处的状态放置返回什么内容的逻辑，如清单 17-18 所示。

文件名：`src/lib.rs`

```rust
trait State {
    --snip--
    fn content<'a>(&self, post: &'a Post) -> &'a str {
      1 ""
    }
}

--snip--
struct Published {}

impl State for Published {
    --snip--
    fn content<'a>(&self, post: &'a Post) -> &'a str {
      2 &post.content
    }
}
```

清单 17-18：将 `content` 方法添加到 `State` trait 中

我们为 `content` 方法添加了一个默认实现，它返回一个空字符串切片\[1\]。这意味着我们不需要在 `Draft` 和 `PendingReview` 结构体上实现 `content`。`Published` 结构体将覆盖 `content` 方法并返回 `post.content` 中的值\[2\]。

请注意，正如我们在第 10 章中讨论的，我们需要对这个方法添加生命周期注释。我们将 `post` 的引用作为参数，并返回对该 `post` 的一部分的引用，所以返回引用的生命周期与 `post` 参数的生命周期相关。

至此，我们完成了——清单 17-11 中的所有内容现在都能正常工作了！我们已经使用博客文章工作流程的规则实现了状态模式。与规则相关的逻辑存在于状态对象中，而不是分散在整个 `Post` 中。

> **为什么不使用枚举？**
>
> 你可能一直在想为什么我们没有使用一个带有不同可能文章状态作为变体的枚举。这当然是一个可能的解决方案；试试看，并比较最终结果，看看你更喜欢哪种！使用枚举的一个缺点是，每个检查枚举值的地方都需要一个 `match` 表达式或类似的东西来处理每个可能的变体。这可能比这个 trait 对象解决方案更繁琐。
