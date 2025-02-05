# 将转换实现为转换为不同类型

那么我们如何得到一篇已发布的文章呢？我们要强制执行这样的规则：草稿文章必须经过审核和批准才能发布。处于待审核状态的文章仍然不应显示任何内容。让我们通过添加另一个结构体 `PendingReviewPost` 来实现这些约束，在 `DraftPost` 上定义 `request_review` 方法以返回一个 `PendingReviewPost`，并在 `PendingReviewPost` 上定义一个 `approve` 方法以返回一个 `Post`，如清单 17-20 所示。

文件名：`src/lib.rs`

```rust
impl DraftPost {
    --snip--
    pub fn request_review(self) -> PendingReviewPost {
        PendingReviewPost {
            content: self.content,
        }
    }
}

pub struct PendingReviewPost {
    content: String,
}

impl PendingReviewPost {
    pub fn approve(self) -> Post {
        Post {
            content: self.content,
        }
    }
}
```

清单 17-20：通过在 `DraftPost` 上调用 `request_review` 创建的 `PendingReviewPost`，以及将 `PendingReviewPost` 转换为已发布 `Post` 的 `approve` 方法

`request_review` 和 `approve` 方法获取 `self` 的所有权，从而消耗 `DraftPost` 和 `PendingReviewPost` 实例，并分别将它们转换为一个 `PendingReviewPost` 和一篇已发布的 `Post`。这样，在我们对它们调用 `request_review` 之后，就不会有任何残留的 `DraftPost` 实例了，依此类推。`PendingReviewPost` 结构体没有定义 `content` 方法，所以尝试读取其内容会导致编译器错误，就像 `DraftPost` 一样。因为获得一个定义了 `content` 方法的已发布 `Post` 实例的唯一方法是在 `PendingReviewPost` 上调用 `approve` 方法，而获得一个 `PendingReviewPost` 的唯一方法是在 `DraftPost` 上调用 `request_review` 方法，我们现在已经将博客文章工作流程编码到类型系统中了。

但是我们还需要对 `main` 做一些小的修改。`request_review` 和 `approve` 方法返回新的实例，而不是修改它们所调用的结构体，所以我们需要添加更多的 `let post =` 遮蔽赋值来保存返回的实例。我们也不能再让关于草稿和待审核文章内容为空字符串的断言存在了，实际上我们也不需要它们了：我们再也无法编译尝试使用那些状态下文章内容的代码了。`main` 中更新后的代码如清单 17-21 所示。

文件名：`src/main.rs`

```rust
use blog::Post;

fn main() {
    let mut post = Post::new();

    post.add_text("I ate a salad for lunch today");

    let post = post.request_review();

    let post = post.approve();

    assert_eq!("I ate a salad for lunch today", post.content());
}
```

清单 17-21：对 `main` 的修改，以使用博客文章工作流程的新实现

我们在 `main` 中为重新赋值 `post` 所做的更改意味着这个实现不再完全遵循面向对象的状态模式了：状态之间的转换不再完全封装在 `Post` 的实现内部。然而，我们的收获是，由于类型系统和编译时的类型检查，现在不可能出现无效状态了！这确保了某些错误，比如显示未发布文章的内容，在进入生产环境之前就会被发现。

在清单 17-21 之后的 `blog` 包上尝试本节开头提出的任务，看看你对这个版本代码的设计有什么看法。请注意，在这个设计中有些任务可能已经完成了。

我们已经看到，尽管 Rust 能够实现面向对象的设计模式，但其他模式，比如将状态编码到类型系统中，在 Rust 中也是可行的。这些模式有不同的权衡。尽管你可能非常熟悉面向对象模式，但重新思考问题以利用 Rust 的特性可以带来好处，比如在编译时防止一些错误。由于某些特性，比如所有权，面向对象语言没有这些特性，所以在 Rust 中面向对象模式并不总是最佳解决方案。
