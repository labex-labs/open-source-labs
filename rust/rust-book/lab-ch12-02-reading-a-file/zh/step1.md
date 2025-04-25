# 读取文件

现在我们将添加功能来读取 `file_path` 参数中指定的文件。首先，我们需要一个示例文件来进行测试：我们将使用一个包含少量多行文本且有一些重复单词的文件。清单 12-3 中的一首艾米莉·狄金森的诗就很合适！在项目的根目录下创建一个名为 _poem.txt_ 的文件，并输入这首诗“我是无名之辈！你是谁？”

文件名：poem.txt

    我是无名之辈！你是谁？
    你也是无名之辈？
    那咱俩就成了一对——别声张！
    你知道，他们会把咱俩流放。

    当个大人物多没劲！
    多招摇，像只青蛙
    对着仰慕的泥沼
    整日把自己的名字宣扬！

清单 12-3：艾米莉·狄金森的一首诗是个很好的测试用例。

有了这段文本后，编辑 `src/main.rs` 并添加读取文件的代码，如清单 12-4 所示。

文件名：`src/main.rs`

```rust
use std::env;
1 use std::fs;

fn main() {
    --snip--
    println!("In file {}", file_path);

  2 let contents = fs::read_to_string(file_path)
       .expect("Should have been able to read the file");

  3 println!("With text:\n{contents}");
}
```

清单 12-4：读取第二个参数指定的文件的内容

首先，我们使用 `use` 语句引入标准库的相关部分：我们需要 `std::fs` 来处理文件\[1\]。

在 `main` 函数中，新语句 `fs::read_to_string` 接受 `file_path`，打开该文件，并返回文件内容的 `std::io::Result<String>`\[2\]。

之后，我们再次添加一个临时的 `println!` 语句，在读取文件后打印 `contents` 的值，这样我们就可以检查到目前为止程序是否正常工作\[3\]。

让我们使用任意字符串作为第一个命令行参数（因为我们还没有实现搜索部分），并将 _poem.txt_ 文件作为第二个参数来运行这段代码：

```bash
$ cargo run -- the poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep the poem.txt`
Searching for the
In file poem.txt
With text:
我是无名之辈！你是谁？
你也是无名之辈？
那咱俩就成了一对——别声张！
你知道，他们会把咱俩流放。

当个大人物多没劲！
多招摇，像只青蛙
对着仰慕的泥沼
整日把自己的名字宣扬！
```

太棒了！代码读取并打印了文件的内容。但这段代码有一些缺陷。目前，`main` 函数有多个职责：一般来说，如果每个函数只负责一个功能，函数会更清晰且易于维护。另一个问题是我们没有尽可能好地处理错误。程序目前还很小，所以这些缺陷不是大问题，但随着程序的增长，要干净利落地修复它们会更困难。在开发程序时尽早开始重构是个好习惯，因为重构少量代码要容易得多。接下来我们就这么做。
