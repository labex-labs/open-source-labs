# 创建一个新项目

要创建一个新项目，进入你在第一章中创建的 `project` 目录，然后使用 Cargo 创建一个新项目，如下所示：

```bash
cargo new guessing_game
cd guessing_game
```

第一个命令 `cargo new`，将项目名称（`guessing_game`）作为第一个参数。第二个命令切换到新项目的目录。

看看生成的 `Cargo.toml` 文件：

文件名：`Cargo.toml`

```toml
[package]
name = "guessing_game"
version = "0.1.0"
edition = "2021"

# 更多键及其定义请参阅
https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
```

正如你在第一章中看到的，`cargo new` 为你生成了一个“Hello, world!”程序。看看 `src/main.rs` 文件：

文件名：`src/main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

现在让我们编译这个“Hello, world!”程序，并使用 `cargo run` 命令在同一步骤中运行它：

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50s
     Running `target/debug/guessing_game`
Hello, world!
```

当你需要在项目上快速迭代时，`run` 命令非常方便，就像我们在这个游戏中要做的那样，在进入下一次迭代之前快速测试每次迭代。

重新打开 `src/main.rs` 文件。你将在这个文件中编写所有代码。
