# 从 main 函数中提取逻辑

既然我们已经完成了配置解析的重构，现在来看看程序的逻辑。正如我们在“二进制项目的关注点分离”中所说，我们将提取一个名为 `run` 的函数，它将包含当前 `main` 函数中所有与配置设置或错误处理无关的逻辑。完成后，`main` 函数将变得简洁且易于通过检查进行验证，并且我们能够为所有其他逻辑编写测试。

清单 12-11 展示了提取的 `run` 函数。目前，我们只是进行了提取函数这个小的渐进式改进。我们仍然在 `src/main.rs` 中定义这个函数。

文件名：`src/main.rs`

```rust
fn main() {
    --snip--

    println!("Searching for {}", config.query);
    println!("In file {}", config.file_path);

    run(config);
}

fn run(config: Config) {
    let contents = fs::read_to_string(config.file_path)
     .expect("Should have been able to read the file");

    println!("With text:\n{contents}");
}

--snip--
```

清单 12-11：提取一个包含程序其余逻辑的 `run` 函数

`run` 函数现在包含了 `main` 函数中从读取文件开始的所有剩余逻辑。`run` 函数将 `Config` 实例作为参数。
