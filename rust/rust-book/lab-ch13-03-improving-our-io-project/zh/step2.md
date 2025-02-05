# 使用迭代器消除克隆操作

在清单 12-6 中，我们添加了一些代码，这些代码获取了一个 `String` 值的切片，并通过对切片进行索引和克隆这些值来创建 `Config` 结构体的实例，从而使 `Config` 结构体拥有这些值。在清单 13-17 中，我们重现了清单 12-23 中 `Config::build` 函数的实现。

文件名：`src/lib.rs`

```rust
impl Config {
    pub fn build(
        args: &[String]
    ) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

清单 13-17：重现清单 12-23 中的 `Config::build` 函数

当时，我们说过不用担心效率低下的 `clone` 调用，因为我们会在将来移除它们。嗯，现在就是那个时候了！

我们在这里需要 `clone`，是因为在参数 `args` 中有一个包含 `String` 元素的切片，但 `build` 函数并不拥有 `args`。为了返回 `Config` 实例的所有权，我们必须从 `Config` 的 `query` 和 `filename` 字段克隆值，这样 `Config` 实例才能拥有它自己的值。

有了关于迭代器的新知识，我们可以将 `build` 函数修改为接受一个迭代器的所有权作为参数，而不是借用一个切片。我们将使用迭代器功能来替代检查切片长度并索引到特定位置的代码。这将使 `Config::build` 函数的功能更加清晰，因为迭代器会访问这些值。

一旦 `Config::build` 获得了迭代器的所有权并停止使用借用的索引操作，我们就可以将迭代器中的 `String` 值移动到 `Config` 中，而不是调用 `clone` 并进行新的分配。
