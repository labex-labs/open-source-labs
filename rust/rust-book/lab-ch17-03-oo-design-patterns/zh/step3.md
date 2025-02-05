# 存储文章内容的文本

我们在清单 17-11 中看到，我们希望能够调用一个名为 `add_text` 的方法，并向其传递一个 `&str`，然后将其作为博客文章的文本内容添加进去。我们将此实现为一个方法，而不是将 `content` 字段暴露为 `pub`，这样以后我们就可以实现一个方法来控制如何读取 `content` 字段的数据。`add_text` 方法非常简单，所以让我们在清单 17-13 中将实现添加到 `impl Post` 块中。

文件名：`src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }
}
```

清单 17-13：实现 `add_text` 方法以向文章的 `content` 中添加文本

`add_text` 方法接受一个对 `self` 的可变引用，因为我们正在更改调用 `add_text` 的 `Post` 实例。然后我们在 `content` 中的 `String` 上调用 `push_str`，并传递 `text` 参数以添加到保存的 `content` 中。此行为不依赖于文章所处的状态，因此它不是状态模式的一部分。`add_text` 方法根本不与 `state` 字段交互，但它是我们想要支持的行为的一部分。
