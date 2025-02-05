# 在类型上实现特性

既然我们已经定义了 `Summary` 特性的方法所需的签名，那么我们就可以在媒体聚合器中的类型上实现它。清单 10-13 展示了在 `NewsArticle` 结构体上对 `Summary` 特性的实现，它使用标题、作者和位置来创建 `summarize` 的返回值。对于 `Tweet` 结构体，我们将 `summarize` 定义为用户名加上推文的完整文本，假设推文内容已经限制在 280 个字符以内。

文件名：`src/lib.rs`

```rust
pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!(
            "{}, by {} ({})",
            self.headline,
            self.author,
            self.location
        )
    }
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}
```

清单 10-13：在 `NewsArticle` 和 `Tweet` 类型上实现 `Summary` 特性

在类型上实现特性类似于实现常规方法。不同之处在于，在 `impl` 之后，我们写上想要实现的特性名称，然后使用 `for` 关键字，接着指定想要为其实现该特性的类型名称。在 `impl` 块内，我们放入特性定义中定义的方法签名。我们不是在每个签名后加分号，而是使用花括号，并在方法体中填充我们希望该特性的方法针对特定类型所具有的具体行为。

现在库已经在 `NewsArticle` 和 `Tweet` 上实现了 `Summary` 特性，该箱的用户可以像调用常规方法一样在 `NewsArticle` 和 `Tweet` 的实例上调用特性方法。唯一的区别是用户必须将特性以及类型引入作用域。下面是一个二进制箱如何使用我们的 `aggregator` 库箱的示例：

```rust
use aggregator::{Summary, Tweet};

fn main() {
    let tweet = Tweet {
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    };

    println!("1 new tweet: {}", tweet.summarize());
}
```

这段代码打印出 `1 new tweet: horse_ebooks: of course, as you probably already know, people`。

其他依赖 `aggregator` 箱的箱也可以将 `Summary` 特性引入作用域，以便在它们自己的类型上实现 `Summary`。需要注意的一个限制是，只有当特性或类型，或者两者都在我们的箱内时，我们才能在一个类型上实现一个特性。例如，作为我们 `aggregator` 箱功能的一部分，我们可以在像 `Tweet` 这样的自定义类型上实现标准库特性，如 `Display`，因为类型 `Tweet` 在我们的 `aggregator` 箱内。我们也可以在我们的 `aggregator` 箱内对 `Vec<T>` 实现 `Summary`，因为特性 `Summary` 在我们的 `aggregator` 箱内。

但是我们不能在外部类型上实现外部特性。例如，我们不能在我们的 `aggregator` 箱内对 `Vec<T>` 实现 `Display` 特性，因为 `Display` 和 `Vec<T>` 都在标准库中定义，并且不在我们的 `aggregator` 箱内。这个限制是一个称为「一致性」属性的一部分，更具体地说是「孤儿规则」，之所以这样命名是因为父类型不存在。这个规则确保其他人的代码不会破坏你的代码，反之亦然。没有这个规则，两个箱可能会为同一类型实现相同的特性，而 Rust 就不知道该使用哪个实现了。
