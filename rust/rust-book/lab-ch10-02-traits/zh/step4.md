# 默认实现

有时，为特性中的某些或所有方法提供默认行为是很有用的，而不是要求每个类型都为所有方法提供实现。然后，当我们在特定类型上实现该特性时，可以保留或覆盖每个方法的默认行为。

在清单 10-14 中，我们为 `Summary` 特性的 `summarize` 方法指定了一个默认字符串，而不是像清单 10-12 那样只定义方法签名。

文件名：`src/lib.rs`

```rust
pub trait Summary {
    fn summarize(&self) -> String {
        String::from("(Read more...)")
    }
}
```

清单 10-14：定义一个带有 `summarize` 方法默认实现的 `Summary` 特性

为了使用默认实现来总结 `NewsArticle` 的实例，我们指定一个空的 `impl` 块 `impl Summary for NewsArticle {}`。

即使我们不再直接在 `NewsArticle` 上定义 `summarize` 方法，但我们已经提供了默认实现，并指定 `NewsArticle` 实现了 `Summary` 特性。因此，我们仍然可以在 `NewsArticle` 的实例上调用 `summarize` 方法，如下所示：

```rust
let article = NewsArticle {
    headline: String::from(
        "Penguins win the Stanley Cup Championship!"
    ),
    location: String::from("Pittsburgh, PA, USA"),
    author: String::from("Iceburgh"),
    content: String::from(
        "The Pittsburgh Penguins once again are the best \
         hockey team in the NHL.",
    ),
};

println!("New article available! {}", article.summarize());
```

这段代码打印出 `New article available! (Read more...)`。

创建默认实现并不需要我们对清单 10-13 中 `Tweet` 上的 `Summary` 实现做任何更改。原因是覆盖默认实现的语法与实现没有默认实现的特性方法的语法相同。

默认实现可以调用同一特性中的其他方法，即使这些其他方法没有默认实现。通过这种方式，一个特性可以提供很多有用的功能，并且只要求实现者指定其中的一小部分。例如，我们可以将 `Summary` 特性定义为有一个需要实现的 `summarize_author` 方法，然后定义一个 `summarize` 方法，其默认实现调用 `summarize_author` 方法：

```rust
pub trait Summary {
    fn summarize_author(&self) -> String;

    fn summarize(&self) -> String {
        format!(
            "(Read more from {}...)",
            self.summarize_author()
        )
    }
}
```

要使用这个版本的 `Summary`，当我们在一个类型上实现该特性时，只需要定义 `summarize_author`：

```rust
impl Summary for Tweet {
    fn summarize_author(&self) -> String {
        format!("@{}", self.username)
    }
}
```

在我们定义了 `summarize_author` 之后，我们就可以在 `Tweet` 结构体的实例上调用 `summarize`，并且 `summarize` 的默认实现会调用我们提供的 `summarize_author` 的定义。因为我们已经实现了 `summarize_author`，`Summary` 特性为我们提供了 `summarize` 方法的行为，而无需我们编写更多代码。如下所示：

```rust
let tweet = Tweet {
    username: String::from("horse_ebooks"),
    content: String::from(
        "of course, as you probably already know, people",
    ),
    reply: false,
    retweet: false,
};

println!("1 new tweet: {}", tweet.summarize());
```

这段代码打印出 `1 new tweet: (Read more from @horse_ebooks...)`。

请注意，在同一方法的覆盖实现中不可能调用默认实现。
