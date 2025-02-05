# 使用迭代器特性方法而非索引

接下来，我们将修复 `Config::build` 的函数体。因为 `args` 实现了 `Iterator` 特性，所以我们知道可以对它调用 `next` 方法！清单 13-20 更新了清单 12-23 中的代码以使用 `next` 方法。

文件名：`src/lib.rs`

```rust
impl Config {
    pub fn build(
        mut args: impl Iterator<Item = String>,
    ) -> Result<Config, &'static str> {
        args.next();

        let query = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a query string"),
        };

        let file_path = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a file path"),
        };

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

清单 13-20：更改 `Config::build` 的函数体以使用迭代器方法

记住，`env::args` 返回值中的第一个值是程序的名称。我们想要忽略它并获取下一个值，所以首先我们调用 `next` 并且不处理返回值。然后我们调用 `next` 来获取我们想要放入 `Config` 的 `query` 字段中的值。如果 `next` 返回 `Some`，我们使用 `match` 来提取值。如果它返回 `None`，这意味着没有提供足够的参数，我们就提前返回一个 `Err` 值。对于 `filename` 值，我们做同样的事情。
