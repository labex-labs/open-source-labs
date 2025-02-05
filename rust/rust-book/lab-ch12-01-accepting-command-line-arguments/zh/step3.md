# 将参数值保存到变量中

程序目前能够访问作为命令行参数指定的值。现在我们需要将这两个参数的值保存到变量中，以便在程序的其余部分使用这些值。我们在清单 12-2 中进行此操作。

文件名：`src/main.rs`

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let query = &args[1];
    let file_path = &args[2];

    println!("Searching for {}", query);
    println!("In file {}", file_path);
}
```

清单 12-2：创建变量来保存查询参数和文件路径参数

正如我们在打印向量时看到的，程序的名称占据了向量中 `args[0]` 处的第一个值，所以我们从索引 1 开始处理参数。`minigrep` 接受的第一个参数是我们要搜索的字符串，所以我们将对第一个参数的引用放入变量 `query` 中。第二个参数将是文件路径，所以我们将对第二个参数的引用放入变量 `file_path` 中。

我们暂时打印这些变量的值，以证明代码按我们预期的方式工作。让我们再次使用参数 `test` 和 `sample.txt` 运行此程序：

```bash
$ cargo run -- test sample.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep test sample.txt`
Searching for test
In file sample.txt
```

很好，程序运行正常！我们需要的参数值被正确地保存到了变量中。稍后我们将添加一些错误处理来应对某些潜在的错误情况，比如用户没有提供参数；目前，我们将忽略这种情况，而是专注于添加文件读取功能。
