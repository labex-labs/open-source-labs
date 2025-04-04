# 实现面向对象设计模式

**状态模式**是一种面向对象设计模式。该模式的关键在于，我们在内部定义一个值可能具有的一组状态。这些状态由一组**状态对象**表示，并且该值的行为会根据其状态而变化。我们将通过一个博客文章结构体的示例来讲解，该结构体有一个字段用于保存其状态，这个状态将是来自“草稿”、“审核”或“已发布”集合中的一个状态对象。

状态对象共享功能：在 Rust 中，我们当然使用结构体和 trait 而不是对象和继承。每个状态对象负责自己的行为以及决定何时应转换为另一个状态。持有状态对象的值对状态的不同行为或何时在状态之间转换一无所知。

使用状态模式的优点是，当程序的业务需求发生变化时，我们无需更改持有状态的值的代码或使用该值的代码。我们只需要更新其中一个状态对象内部的代码以更改其规则，或者可能添加更多状态对象。

首先，我们将以更传统的面向对象方式实现状态模式，然后我们将使用一种在 Rust 中更自然的方法。让我们深入了解如何使用状态模式逐步实现博客文章工作流程。

最终功能如下：

1. 博客文章最初是一个空草稿。
2. 草稿完成后，请求对文章进行审核。
3. 文章被批准后，它会被发布。
4. 只有已发布的博客文章才会返回要打印的内容，因此未经批准的文章不会意外发布。

对文章尝试的任何其他更改都不应产生任何影响。例如，如果我们在请求审核之前尝试批准一篇草稿博客文章，该文章应保持为未发布的草稿。

清单 17-11 以代码形式展示了此工作流程：这是我们将在名为 `blog` 的库 crate 中实现的 API 的一个示例用法。由于我们尚未实现 `blog` crate，所以这段代码目前无法编译。

文件名：`src/main.rs`

```rust
use blog::Post;

fn main() {
  1 let mut post = Post::new();

  2 post.add_text("I ate a salad for lunch today");
  3 assert_eq!("", post.content());

  4 post.request_review();
  5 assert_eq!("", post.content());

  6 post.approve();
  7 assert_eq!("I ate a salad for lunch today", post.content());
}
```

清单 17-11：展示我们希望 `blog` crate 具有的期望行为的代码

我们希望允许用户使用 `Post::new` 创建一个新的草稿博客文章\[1\]。我们希望允许向博客文章添加文本\[2\]。如果我们在批准之前立即尝试获取文章的内容，我们不应得到任何文本，因为文章仍然是草稿。为了演示目的，我们在代码中添加了 `assert_eq!`\[3\]。对此的一个优秀单元测试是断言草稿博客文章从 `content` 方法返回一个空字符串，但我们不会为这个示例编写测试。

接下来，我们希望能够请求对文章进行审核\[4\]，并且我们希望在等待审核时 `content` 返回一个空字符串\[5\]。当文章获得批准时\[6\]，它应该被发布，这意味着当调用 `content` 时将返回文章的文本\[7\]。

请注意，我们从 crate 中与之交互的唯一类型是 `Post` 类型。这个类型将使用状态模式，并将持有一个值，该值将是表示文章可能处于的各种状态的三个状态对象之一——草稿、审核或已发布。从一种状态转换到另一种状态将在 `Post` 类型内部进行管理。状态根据我们库的用户在 `Post` 实例上调用的方法而变化，但他们不必直接管理状态变化。此外，用户不会在状态方面出错，例如在文章审核之前发布文章。
