# 为 Config 创建一个构造函数

到目前为止，我们已经从 `main` 函数中提取了负责解析命令行参数的逻辑，并将其放在了 `parse_config` 函数中。这样做有助于我们看到 `query` 和 `file_path` 值是相关的，并且这种关系应该在我们的代码中体现出来。然后，我们添加了一个 `Config` 结构体，以表明 `query` 和 `file_path` 的相关用途，并能够从 `parse_config` 函数中以结构体字段名的形式返回这些值的名称。

既然 `parse_config` 函数的目的是创建一个 `Config` 实例，那么我们可以将 `parse_config` 从一个普通函数改为一个与 `Config` 结构体关联的名为 `new` 的函数。做出这个改变会使代码更符合习惯用法。我们可以通过调用 `String::new` 来创建标准库中类型的实例，比如 `String`。类似地，通过将 `parse_config` 改为与 `Config` 关联的 `new` 函数，我们将能够通过调用 `Config::new` 来创建 `Config` 的实例。清单 12-7 展示了我们需要做的更改。

文件名：`src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

  1 let config = Config::new(&args);

    --snip--
}

--snip--

2 impl Config {
  3 fn new(args: &[String]) -> Config {
        let query = args[1].clone();
        let file_path = args[2].clone();

        Config { query, file_path }
    }
}
```

清单 12-7：将 `parse_config` 改为 `Config::new`

我们更新了 `main` 函数，将调用 `parse_config` 的地方改为调用 `Config::new` \[1\]。我们将 `parse_config` 的名称改为 `new` \[3\]，并将其移动到一个 `impl` 块中 \[2\]，这将 `new` 函数与 `Config` 关联起来。再次尝试编译这段代码，以确保它能正常工作。
