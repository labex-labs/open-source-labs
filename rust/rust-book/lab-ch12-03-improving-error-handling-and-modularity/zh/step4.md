# 对配置值进行分组

我们可以再迈出一小步，进一步改进 `parse_config` 函数。目前，我们返回的是一个元组，但随后又立即将该元组拆分成各个部分。这表明我们可能还没有正确的抽象。

另一个表明有改进空间的迹象是 `parse_config` 中的 `config` 部分，这意味着我们返回的两个值是相关的，并且都是一个配置值的一部分。除了将这两个值组合成一个元组之外，我们目前并没有通过数据结构来传达这种含义；相反，我们将这两个值放入一个结构体中，并为结构体的每个字段赋予一个有意义的名称。这样做将使这段代码的未来维护者更容易理解不同的值是如何相互关联的以及它们的用途是什么。

清单 12-6 展示了对 `parse_config` 函数的改进。

文件名：`src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

  1 let config = parse_config(&args);

    println!("Searching for {}", 2 config.query);
    println!("In file {}", 3 config.file_path);

    let contents = fs::read_to_string(4 config.file_path)
     .expect("Should have been able to read the file");

    --snip--
}

5 struct Config {
    query: String,
    file_path: String,
}

6 fn parse_config(args: &[String]) -> Config {
  7 let query = args[1].clone();
  8 let file_path = args[2].clone();

    Config { query, file_path }
}
```

清单 12-6：重构 `parse_config` 函数以返回 `Config` 结构体的实例

我们添加了一个名为 `Config` 的结构体，它有两个字段，分别名为 `query` 和 `file_path` \[5\]。`parse_config` 的签名现在表明它返回一个 `Config` 值 \[6\]。在 `parse_config` 的主体中，我们以前返回的是引用 `args` 中 `String` 值的字符串切片，现在我们定义 `Config` 来包含拥有所有权的 `String` 值。`main` 中的 `args` 变量是参数值的所有者，它只是让 `parse_config` 函数借用它们，这意味着如果 `Config` 试图获取 `args` 中值的所有权，我们将违反 Rust 的借用规则。

我们可以通过多种方式来管理 `String` 数据；最简单的方法（尽管有点低效）是对这些值调用 `clone` 方法 \[7\] \[8\]。这将为 `Config` 实例创建数据的完整副本以供其拥有，这比存储对字符串数据的引用需要更多的时间和内存。然而，克隆数据也使我们的代码非常简单，因为我们不必管理引用的生命周期；在这种情况下，为了获得简单性而牺牲一点性能是值得的权衡。

> **使用 clone 的权衡**
>
> 由于其运行时成本，许多 Rust 开发者倾向于避免使用 `clone` 来解决所有权问题。在第 13 章中，你将学习如何在这种情况下使用更高效的方法。但目前，复制几个字符串以继续推进是可以的，因为你只会复制一次，而且你的文件路径和查询字符串非常小。拥有一个有点低效但能正常工作的程序比在第一次尝试时就过度优化代码要好。随着你对 Rust 越来越有经验，从最有效的解决方案开始会更容易，但目前，调用 `clone` 是完全可以接受的。

我们更新了 `main` 函数，使其将 `parse_config` 返回的 `Config` 实例放入一个名为 `config` 的变量中 \[1\]，并且我们更新了之前使用单独的 `query` 和 `file_path` 变量的代码，现在改为使用 `Config` 结构体的字段 \[2\] \[3\] \[4\]。

现在我们的代码更清楚地表明 `query` 和 `file_path` 是相关的，并且它们的目的是配置程序的工作方式。任何使用这些值的代码都知道在 `config` 实例中以其命名的字段中找到它们。
