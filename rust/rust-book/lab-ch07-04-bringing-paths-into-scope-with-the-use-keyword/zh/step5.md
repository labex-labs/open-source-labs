# 使用外部包

在第 2 章中，我们编写了一个猜数字游戏项目，该项目使用了一个名为 `rand` 的外部包来获取随机数。为了在我们的项目中使用 `rand`，我们在 `Cargo.toml` 中添加了这一行：

文件名：`Cargo.toml`

```tomltoml
rand = "0.8.5"
```

在 `Cargo.toml` 中将 `rand` 添加为依赖项会告诉 Cargo 从 *https://crates.io* 下载 `rand` 包及其所有依赖项，并使 `rand` 对我们的项目可用。

然后，为了将 `rand` 的定义引入我们包的作用域，我们添加了一行以包名 `rand` 开头的 `use` 语句，并列出了我们想要引入作用域的项。回想一下在“生成随机数”中，我们将 `Rng` 特性引入作用域并调用了 `rand::thread_rng` 函数：

```rust
use rand::Rng;

fn main() {
    let secret_number = rand::thread_rng().gen_range(1..=100);
}
```

Rust 社区的成员在 *https://crates.io* 上提供了许多包，将其中任何一个包引入你的包都涉及相同的步骤：在你的包的 `Cargo.toml` 文件中列出它们，并使用 `use` 将来自它们包的项引入作用域。

请注意，标准的 `std` 库也是我们包外部的一个包。因为标准库是随 Rust 语言一起提供的，所以我们不需要更改 `Cargo.toml` 来包含 `std`。但是我们确实需要使用 `use` 来引用它，以便将那里的项引入我们包的作用域。例如，对于 `HashMap`，我们会使用这一行：

```rust
use std::collections::HashMap;
```

这是一个以标准库包名 `std` 开头的绝对路径。
