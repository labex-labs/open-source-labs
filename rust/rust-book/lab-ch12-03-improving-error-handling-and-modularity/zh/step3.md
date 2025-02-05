# 提取参数解析器

我们将把解析参数的功能提取到一个函数中，`main` 函数会调用这个函数，以便为将命令行解析逻辑移动到 `src/lib.rs` 做准备。清单 12-5 展示了 `main` 函数新的起始部分，它调用了一个新函数 `parse_config`，目前我们将在 `src/main.rs` 中定义这个函数。

文件名：`src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let (query, file_path) = parse_config(&args);

    --snip--
}

fn parse_config(args: &[String]) -> (&str, &str) {
    let query = &args[1];
    let file_path = &args[2];

    (query, file_path)
}
```

清单 12-5：从 `main` 函数中提取 `parse_config` 函数

我们仍然将命令行参数收集到一个向量中，但不是在 `main` 函数中把索引为 1 的参数值赋给变量 `query`，把索引为 2 的参数值赋给变量 `file_path`，而是将整个向量传递给 `parse_config` 函数。然后，`parse_config` 函数包含了确定哪个参数对应哪个变量的逻辑，并将这些值返回给 `main` 函数。我们仍然在 `main` 函数中创建 `query` 和 `file_path` 变量，但 `main` 函数不再负责确定命令行参数和变量之间的对应关系。

对于我们这个小程序来说，这种重构可能看起来有些小题大做，但我们是在以小的、渐进的步骤进行重构。做出这个更改后，再次运行程序以验证参数解析仍然有效。经常检查你的进展是有好处的，这样在出现问题时有助于确定问题的原因。
