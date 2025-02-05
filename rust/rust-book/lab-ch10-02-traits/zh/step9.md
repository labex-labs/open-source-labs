# 返回实现特性的类型

我们还可以在返回位置使用 `impl Trait` 语法来返回实现某个特性的某种类型的值，如下所示：

```rust
fn returns_summarizable() -> impl Summary {
    Tweet {
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    }
}
```

通过在返回类型中使用 `impl Summary`，我们指定 `returns_summarizable` 函数返回某种实现了 `Summary` 特性的类型，而无需指定具体类型。在这种情况下，`returns_summarizable` 返回一个 `Tweet`，但调用此函数的代码无需知道这一点。

仅通过特性来指定返回类型的能力在闭包和迭代器的上下文中特别有用，我们将在第 13 章中介绍。闭包和迭代器创建的类型只有编译器知道，或者是非常长而难以指定的类型。`impl Trait` 语法让你可以简洁地指定一个函数返回某种实现了 `Iterator` 特性的类型，而无需写出很长的类型。

然而，只有在返回单个类型时才能使用 `impl Trait`。例如，这段返回 `NewsArticle` 或 `Tweet` 且返回类型指定为 `impl Summary` 的代码无法正常工作：

```rust
fn returns_summarizable(switch: bool) -> impl Summary {
    if switch {
        NewsArticle {
            headline: String::from(
                "Penguins win the Stanley Cup Championship!",
            ),
            location: String::from("Pittsburgh, PA, USA"),
            author: String::from("Iceburgh"),
            content: String::from(
                "The Pittsburgh Penguins once again are the best \
                 hockey team in the NHL.",
            ),
        }
    } else {
        Tweet {
            username: String::from("horse_ebooks"),
            content: String::from(
                "of course, as you probably already know, people",
            ),
            reply: false,
            retweet: false,
        }
    }
}
```

由于编译器对 `impl Trait` 语法的实现限制，不允许返回 `NewsArticle` 或 `Tweet` 中的任意一个。我们将在“使用允许不同类型值的特性对象”中介绍如何编写具有这种行为的函数。
