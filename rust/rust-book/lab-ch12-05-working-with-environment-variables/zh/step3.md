# 实现 search_case_insensitive 函数

清单 12 - 21 中展示的`search_case_insensitive`函数与`search`函数几乎相同。唯一的区别在于，我们会将`query`和每一行`line`都转换为小写形式，这样无论输入参数的大小写如何，在检查该行是否包含查询内容时，它们的大小写都是一致的。

文件名：`src/lib.rs`

```rust
pub fn search_case_insensitive<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
  1 let query = query.to_lowercase();
    let mut results = Vec::new();

    for line in contents.lines() {
        if 2 line.to_lowercase().contains(3 &query) {
            results.push(line);
        }
    }

    results
}
```

清单 12 - 21：定义`search_case_insensitive`函数，在比较之前将查询和行转换为小写

首先，我们将`query`字符串转换为小写形式，并将其存储在一个同名的遮蔽变量中\[1\]。对查询调用`to_lowercase`是必要的，这样无论用户的查询是`"rust"`、`"RUST"`、`"Rust"`还是`"rUsT"`，我们都将把查询视为`"rust"`，而不区分大小写。虽然`to_lowercase`可以处理基本的 Unicode，但它并不完全准确。如果我们编写一个实际应用程序，在这里需要做更多工作，但本节是关于环境变量的，而不是 Unicode，所以我们就先这样处理。

注意，`query`现在是一个`String`而不是字符串切片，因为调用`to_lowercase`会创建新的数据，而不是引用现有数据。例如，假设查询是`"rUsT"`：那个字符串切片中不包含小写的`u`或`t`供我们使用，所以我们必须分配一个新的包含`"rust"`的`String`。当我们现在将`query`作为参数传递给`contains`方法时，我们需要添加一个`&`符号\[3\]，因为`contains`的签名定义为接受一个字符串切片。

接下来，我们对每一行`line`调用`to_lowercase`，将所有字符转换为小写\[2\]。现在我们已经将`line`和`query`都转换为小写，无论查询的大小写如何，我们都能找到匹配项。

让我们看看这个实现是否能通过测试：

    running 2 tests
    test tests::case_insensitive... ok
    test tests::case_sensitive... ok

    test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

太棒了！测试通过了。现在，让我们从`run`函数中调用新的`search_case_insensitive`函数。首先，我们将在`Config`结构体中添加一个配置选项，用于在区分大小写和不区分大小写的搜索之间进行切换。添加这个字段会导致编译器错误，因为我们还没有在任何地方初始化这个字段：

文件名：`src/lib.rs`

```rust
pub struct Config {
    pub query: String,
    pub file_path: String,
    pub ignore_case: bool,
}
```

我们添加了一个存储布尔值的`ignore_case`字段。接下来，我们需要`run`函数检查`ignore_case`字段的值，并据此决定调用`search`函数还是`search_case_insensitive`函数，如清单 12 - 22 所示。不过，这仍然无法编译。

文件名：`src/lib.rs`

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    let results = if config.ignore_case {
        search_case_insensitive(&config.query, &contents)
    } else {
        search(&config.query, &contents)
    };

    for line in results {
        println!("{line}");
    }

    Ok(())
}
```

清单 12 - 22：根据`config.ignore_case`中的值调用`search`或`search_case_insensitive`

最后，我们需要检查环境变量。处理环境变量的函数在标准库的`env`模块中，所以我们在`src/lib.rs`的顶部将该模块引入作用域。然后，我们将使用`env`模块中的`var`函数来检查是否为名为`IGNORE_CASE`的环境变量设置了任何值，如清单 12 - 23 所示。

文件名：`src/lib.rs`

```rust
use std::env;
--snip--

impl Config {
    pub fn build(
        args: &[String]
    ) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

清单 12 - 23：检查名为`IGNORE_CASE`的环境变量中是否有任何值

在这里，我们创建了一个新变量`ignore_case`。为了设置它的值，我们调用`env::var`函数，并将`IGNORE_CASE`环境变量的名称传递给它。`env::var`函数返回一个`Result`，如果环境变量设置了任何值，它将是包含环境变量值的成功的`Ok`变体。如果环境变量未设置，它将返回`Err`变体。

我们使用`Result`上的`is_ok`方法来检查环境变量是否已设置，这意味着程序应该进行不区分大小写的搜索。如果`IGNORE_CASE`环境变量未设置任何值，`is_ok`将返回`false`，程序将进行区分大小写的搜索。我们不关心环境变量的值，只关心它是否已设置，所以我们检查`is_ok`，而不是使用`unwrap`、`expect`或我们在`Result`上看到的任何其他方法。

我们将`ignore_case`变量中的值传递给`Config`实例，这样`run`函数就可以读取该值，并决定是调用`search_case_insensitive`还是`search`，就像我们在清单 12 - 22 中实现的那样。

让我们试试看！首先，我们在未设置环境变量的情况下运行程序，并使用查询`to`，它应该匹配任何包含全小写单词`to`的行：

```bash
$ cargo run -- to poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep to poem.txt`
Are you nobody, too?
How dreary to be somebody!
```

看起来仍然有效！现在，我们将`IGNORE_CASE`设置为`1`并使用相同的查询`to`来运行程序：

```bash
IGNORE_CASE=1 cargo run -- to poem.txt
```

如果你使用的是 PowerShell，你需要分别设置环境变量并运行程序：

```rust
PS> $Env:IGNORE_CASE=1; cargo run -- to poem.txt
```

这将使`IGNORE_CASE`在你的 shell 会话的剩余时间内持续存在。可以使用`Remove-Item` cmdlet 取消设置：

```rust
PS> Remove-Item Env:IGNORE_CASE
```

我们应该会得到包含`to`的行，这些行可能包含大写字母：

    Are you nobody, too?
    How dreary to be somebody!
    To tell your name the livelong day
    To an admiring bog!

太棒了，我们还得到了包含`To`的行！我们的`minigrep`程序现在可以通过环境变量控制进行不区分大小写的搜索了。现在你知道如何管理通过命令行参数或环境变量设置的选项了。

有些程序允许对相同的配置同时使用参数和环境变量。在这种情况下，程序会决定其中一个优先。作为另一个练习，你可以尝试通过命令行参数或环境变量来控制大小写敏感性。如果程序在一个设置为区分大小写而另一个设置为不区分大小写的情况下运行，决定命令行参数或环境变量应该优先。

`std::env`模块包含许多处理环境变量的更有用的功能：查看其文档以了解可用的功能。
