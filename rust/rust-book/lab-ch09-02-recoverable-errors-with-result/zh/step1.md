# 使用 `Result` 处理可恢复错误

大多数错误并不严重到需要程序完全停止。有时，当一个函数失败时，原因是你可以轻松解释和应对的。例如，如果你尝试打开一个文件，但由于文件不存在而导致操作失败，你可能想要创建该文件，而不是终止进程。

回顾「使用 `Result` 处理潜在失败」，`Result` 枚举被定义为有两个变体，`Ok` 和 `Err`，如下所示：

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

`T` 和 `E` 是泛型类型参数：我们将在第 10 章更详细地讨论泛型。你现在需要知道的是，`T` 表示在 `Ok` 变体的成功情况下将返回的值的类型，而 `E` 表示在 `Err` 变体的失败情况下将返回的错误的类型。因为 `Result` 有这些泛型类型参数，所以我们可以在许多不同的情况下使用 `Result` 类型及其定义的函数，在这些情况下，我们想要返回的成功值和错误值可能不同。

让我们调用一个返回 `Result` 值的函数，因为该函数可能会失败。在清单 9-3 中，我们尝试打开一个文件。

文件名：`src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file_result = File::open("hello.txt");
}
```

清单 9-3：打开一个文件

`File::open` 的返回类型是 `Result<T, E>`。泛型参数 `T` 已由 `File::open` 的实现填充为成功值的类型 `std::fs::File`，它是一个文件句柄。错误值中使用的 `E` 的类型是 `std::io::Error`。这种返回类型意味着对 `File::open` 的调用可能成功并返回一个我们可以从中读取或写入的文件句柄。函数调用也可能失败：例如，文件可能不存在，或者我们可能没有权限访问该文件。`File::open` 函数需要有一种方法来告诉我们它是成功还是失败，同时给我们文件句柄或错误信息。这些信息正是 `Result` 枚举所传达的。

在 `File::open` 成功的情况下，变量 `greeting_file_result` 中的值将是一个包含文件句柄的 `Ok` 实例。在失败的情况下，`greeting_file_result` 中的值将是一个包含有关发生的错误类型的更多信息的 `Err` 实例。

我们需要在清单 9-3 的代码中添加内容，以便根据 `File::open` 返回的值采取不同的操作。清单 9-4 展示了一种使用基本工具 `match` 表达式来处理 `Result` 的方法，我们在第 6 章中讨论过这个表达式。

文件名：`src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => {
            panic!("Problem opening the file: {:?}", error);
        }
    };
}
```

清单 9-4：使用 `match` 表达式处理可能返回的 `Result` 变体

请注意，与 `Option` 枚举一样，`Result` 枚举及其变体已由 prelude 引入作用域，因此我们在 `match` 分支中不需要在 `Ok` 和 `Err` 变体之前指定 `Result::`。

当结果为 `Ok` 时，这段代码将从 `Ok` 变体中返回内部的 `file` 值，然后我们将该文件句柄值赋给变量 `greeting_file`。在 `match` 之后，我们可以使用该文件句柄进行读取或写入。

`match` 的另一个分支处理我们从 `File::open` 获得 `Err` 值的情况。在这个例子中，我们选择调用 `panic!` 宏。如果我们当前目录中没有名为 _hello.txt_ 的文件，并且我们运行这段代码，我们将从 `panic!` 宏中看到以下输出：

    thread'main' panicked at 'Problem opening the file: Os { code:
     2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:8:23

像往常一样，这个输出准确地告诉我们哪里出了问题。
