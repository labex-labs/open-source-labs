# 将状态和行为编码为类型

我们将向你展示如何重新思考状态模式，以获得另一组权衡。我们不会将状态和转换完全封装起来，使外部代码对此一无所知，而是将状态编码为不同的类型。因此，Rust 的类型检查系统将通过发出编译器错误来阻止在只允许已发布文章的地方使用草稿文章的尝试。

让我们看看清单 17-11 中 `main` 的第一部分：

文件名：`src/main.rs`

```rust
fn main() {
    let mut post = Post::new();

    post.add_text("I ate a salad for lunch today");
    assert_eq!("", post.content());
}
```

我们仍然可以使用 `Post::new` 创建处于草稿状态的新文章，并能够向文章内容中添加文本。但是，我们不会让草稿文章有一个返回空字符串的 `content` 方法，而是让草稿文章根本没有 `content` 方法。这样，如果我们试图获取草稿文章的内容，就会得到一个编译器错误，告诉我们该方法不存在。结果，我们就不可能在生产环境中意外地显示草稿文章的内容，因为那段代码甚至无法编译。清单 17-19 展示了 `Post` 结构体和 `DraftPost` 结构体的定义，以及每个结构体上的方法。

文件名：`src/lib.rs`

```rust
pub struct Post {
    content: String,
}

pub struct DraftPost {
    content: String,
}

impl Post {
  1 pub fn new() -> DraftPost {
        DraftPost {
            content: String::new(),
        }
    }

  2 pub fn content(&self) -> &str {
        &self.content
    }
}

impl DraftPost {
  3 pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }
}
```

清单 17-19：一个有 `content` 方法的 `Post` 和一个没有 `content` 方法的 `DraftPost`

`Post` 和 `DraftPost` 结构体都有一个私有的 `content` 字段，用于存储博客文章的文本。结构体不再有 `state` 字段，因为我们将状态的编码转移到了结构体的类型上。`Post` 结构体将表示一篇已发布的文章，它有一个返回 `content` 的 `content` 方法\[2\]。

我们仍然有一个 `Post::new` 函数，但它返回的不是 `Post` 的实例，而是 `DraftPost` 的实例\[1\]。因为 `content` 是私有的，而且没有任何函数返回 `Post`，所以目前不可能创建 `Post` 的实例。

`DraftPost` 结构体有一个 `add_text` 方法，所以我们可以像以前一样向 `content` 中添加文本\[3\]，但要注意 `DraftPost` 没有定义 `content` 方法！所以现在程序确保所有文章都从草稿文章开始，并且草稿文章的内容不可用于显示。任何试图绕过这些限制的尝试都会导致编译器错误。
