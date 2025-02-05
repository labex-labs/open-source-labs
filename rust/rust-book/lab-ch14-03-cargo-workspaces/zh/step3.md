# 在工作区中创建第二个包

接下来，让我们在工作区中创建另一个成员包，并将其命名为 `add_one`。修改顶层的 `Cargo.toml` 文件，在 `members` 列表中指定 `add_one` 路径：

文件名：`Cargo.toml`

```toml
[workspace]

members = [
    "adder",
    "add_one",
]
```

然后生成一个名为 `add_one` 的新库板条箱：

```bash
$ cargo new add_one --lib
Created library $(add_one) package
```

现在你的 `add` 目录应该有以下这些目录和文件：

    ├── Cargo.lock
    ├── Cargo.toml
    ├── add_one
    │   ├── Cargo.toml
    │   └── src
    │       └── lib.rs
    ├── adder
    │   ├── Cargo.toml
    │   └── src
    │       └── main.rs
    └── target

在 `add_one/src/lib.rs` 文件中，让我们添加一个 `add_one` 函数：

文件名：`add_one/src/lib.rs`

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}
```

现在我们可以让包含二进制文件的 `adder` 包依赖于包含我们库的 `add_one` 包。首先，我们需要在 _adder/Cargo.toml_ 中添加对 `add_one` 的路径依赖：

文件名：`adder/Cargo.toml`

```tomlrust
[dependencies]
add_one = { path = "../add_one" }
```

Cargo 不会假设工作区中的板条箱会相互依赖，所以我们需要明确指定依赖关系。

接下来，让我们在 `adder` 板条箱中使用 `add_one` 函数（来自 `add_one` 板条箱）。打开 `adder/src/main.rs` 文件，在顶部添加一条 `use` 语句，将新的 `add_one` 库板条箱引入作用域。然后修改 `main` 函数来调用 `add_one` 函数，如清单 14 - 7 所示。

文件名：`adder/src/main.rs`

```rust
use add_one;

fn main() {
    let num = 10;
    println!(
        "Hello, world! {num} plus one is {}!",
        add_one::add_one(num)
    );
}
```

清单 14 - 7：在 `adder` 板条箱中使用 `add_one` 库板条箱

让我们通过在顶层的 _add_ 目录中运行 `cargo build` 来构建工作区！

```bash
$ cargo build
   Compiling add_one v0.1.0 (file:///projects/add/add_one)
   Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished dev [unoptimized + debuginfo] target(s) in 0.68s
```

要从 `add` 目录运行二进制板条箱，我们可以使用 `-p` 参数和包名，通过 `cargo run` 指定我们想要运行的工作区中的包：

```bash
$ cargo run -p adder
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/adder`
Hello, world! 10 plus one is 11!
```

这将运行 `adder/src/main.rs` 中的代码，该代码依赖于 `add_one` 板条箱。
