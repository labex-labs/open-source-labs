# 直接使用返回的迭代器

打开你 I/O 项目的 `src/main.rs` 文件，它应该看起来像这样：

文件名：`src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    --snip--
}
```

我们首先将清单 12-24 中的 `main` 函数开头部分改为清单 13-18 中的代码，这次使用了一个迭代器。在我们更新 `Config::build` 之前，这段代码无法编译。

文件名：`src/main.rs`

```rust
fn main() {
    let config =
        Config::build(env::args()).unwrap_or_else(|err| {
            eprintln!("Problem parsing arguments: {err}");
            process::exit(1);
        });

    --snip--
}
```

清单 13-18：将 `env::args` 的返回值传递给 `Config::build`

`env::args` 函数返回一个迭代器！现在我们不再将迭代器的值收集到一个向量中，然后将一个切片传递给 `Config::build`，而是直接将 `env::args` 返回的迭代器的所有权传递给 `Config::build`。

接下来，我们需要更新 `Config::build` 的定义。在你的 I/O 项目的 `src/lib.rs` 文件中，让我们将 `Config::build` 的签名改为清单 13-19 中的样子。这仍然无法编译，因为我们需要更新函数体。

文件名：`src/lib.rs`

```rust
impl Config {
    pub fn build(
        mut args: impl Iterator<Item = String>,
    ) -> Result<Config, &'static str> {
        --snip--
```

清单 13-19：更新 `Config::build` 的签名以接受一个迭代器

`env::args` 函数的标准库文档显示，它返回的迭代器类型是 `std::env::Args`，并且该类型实现了 `Iterator` 特性并返回 `String` 值。

我们已经更新了 `Config::build` 函数的签名，这样参数 `args` 就有了一个通用类型，其特性边界为 `impl Iterator<Item = String>`，而不是 `&[String]`。我们在“作为参数的特性”中讨论过的 `impl Trait` 语法的这种用法意味着 `args` 可以是任何实现了 `Iterator` 类型并返回 `String` 项的类型。

因为我们获取了 `args` 的所有权，并且我们将通过迭代它来修改 `args`，所以我们可以在 `args` 参数的规范中添加 `mut` 关键字，使其可变。
