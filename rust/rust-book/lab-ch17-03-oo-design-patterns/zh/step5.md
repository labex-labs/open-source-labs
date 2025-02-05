# 请求审核会更改文章的状态

接下来，我们需要添加功能来请求对文章进行审核，这应该会将其状态从“草稿”更改为“待审核”。清单 17-15 展示了此代码。

文件名：`src/lib.rs`

```rust
impl Post {
    --snip--
  1 pub fn request_review(&mut self) {
      2 if let Some(s) = self.state.take() {
          3 self.state = Some(s.request_review())
        }
    }
}

trait State {
  4 fn request_review(self: Box<Self>) -> Box<dyn State>;
}

struct Draft {}

impl State for Draft {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
      5 Box::new(PendingReview {})
    }
}

struct PendingReview {}

impl State for PendingReview {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
      6 self
    }
}
```

清单 17-15：在 `Post` 和 `State` trait 上实现 `request_review` 方法

我们为 `Post` 提供一个名为 `request_review` 的公共方法，它将接受对 `self` 的可变引用\[1\]。然后我们在 `Post` 的当前状态上调用一个内部的 `request_review` 方法\[3\]，并且这个第二个 `request_review` 方法会消耗当前状态并返回一个新状态。

我们将 `request_review` 方法添加到 `State` trait 中\[4\]；所有实现该 trait 的类型现在都需要实现 `request_review` 方法。注意，该方法的第一个参数不是 `self`、`&self` 或 `&mut self`，而是 `self: Box<Self>`。这种语法意味着该方法仅在对持有该类型的 `Box` 调用时才有效。这种语法获取了 `Box<Self>` 的所有权，使旧状态无效，这样 `Post` 的状态值就可以转换为新状态。

为了消耗旧状态，`request_review` 方法需要获取状态值的所有权。这就是 `Post` 的 `state` 字段中的 `Option` 发挥作用的地方：我们调用 `take` 方法从 `state` 字段中取出 `Some` 值，并在其位置留下一个 `None`，因为 Rust 不允许我们在结构体中有未填充的字段\[2\]。这使我们能够将 `state` 值从 `Post` 中移出而不是借用它。然后我们将文章的 `state` 值设置为这个操作的结果。

我们需要暂时将 `state` 设置为 `None`，而不是直接用像 `self.state = self.state.request_review();` 这样的代码来设置它，以便获取 `state` 值的所有权。这确保了在我们将 `Post` 的状态转换为新状态后，它不能再使用旧的 `state` 值。

`Draft` 上的 `request_review` 方法返回一个新的、装箱的 `PendingReview` 结构体实例\[5\]，它表示文章等待审核时的状态。`PendingReview` 结构体也实现了 `request_review` 方法，但不进行任何转换。相反，它返回自身\[6\]，因为当我们对已经处于“待审核”状态的文章请求审核时，它应该保持在“待审核”状态。

现在我们可以开始看到状态模式的优点了：无论 `Post` 的 `state` 值如何，`request_review` 方法都是相同的。每个状态都负责自己的规则。

我们将 `Post` 上的 `content` 方法保持不变，返回一个空字符串切片。现在我们可以有处于“待审核”状态以及“草稿”状态的 `Post`，但我们希望在“待审核”状态下有相同的行为。清单 17-11 现在直到\[5\]行都能正常工作！
