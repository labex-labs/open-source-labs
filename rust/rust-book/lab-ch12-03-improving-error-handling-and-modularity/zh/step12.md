# 在 main 函数中处理 run 函数返回的错误

我们将检查错误并使用一种与清单 12-10 中处理 `Config::build` 类似的技术来处理错误，但有一个细微的差别：

文件名：`src/main.rs`

```rust
fn main() {
    --snip--

    println!("Searching for {}", config.query);
    println!("In file {}", config.file_path);

    if let Err(e) = run(config) {
        println!("Application error: {e}");
        process::exit(1);
    }
}
```

我们使用 `if let` 而不是 `unwrap_or_else` 来检查 `run` 是否返回一个 `Err` 值，如果返回则调用 `process::exit(1)`。`run` 函数不像 `Config::build` 返回 `Config` 实例那样返回一个我们想要解包的值。因为 `run` 在成功的情况下返回 `()`，我们只关心检测到错误，所以我们不需要 `unwrap_or_else` 来返回解包后的值，因为解包后的值只会是 `()`。

在这两种情况下，`if let` 和 `unwrap_or_else` 函数的主体是相同的：我们打印错误并退出。
