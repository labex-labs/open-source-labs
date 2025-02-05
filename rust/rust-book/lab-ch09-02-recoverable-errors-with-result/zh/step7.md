# `?` 运算符的使用位置

`?` 运算符只能在返回类型与 `?` 所作用的值兼容的函数中使用。这是因为 `?` 运算符被定义为以与我们在清单 9-6 中定义的 `match` 表达式相同的方式提前从函数中返回一个值。在清单 9-6 中，`match` 使用的是 `Result` 值，提前返回分支返回的是 `Err(e)` 值。函数的返回类型必须是 `Result`，这样才能与这个 `return` 兼容。

在清单 9-10 中，让我们看看如果在返回类型与我们对其使用 `?` 运算符的值的类型不兼容的 `main` 函数中使用 `?` 运算符会得到什么错误。

文件名：`src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt")?;
}
```

清单 9-10：在返回 `()` 的 `main` 函数中尝试使用 `?` 将无法编译。

这段代码打开一个文件，这可能会失败。`?` 运算符跟随 `File::open` 返回的 `Result` 值，但这个 `main` 函数的返回类型是 `()`，而不是 `Result`。当我们编译这段代码时，会得到以下错误信息：

```bash
error[E0277]: the `?` operator can only be used in a function that returns
`Result` or `Option` (or another type that implements `FromResidual`)
 --> src/main.rs:4:48
  |
3 | / fn main() {
4 | |     let greeting_file = File::open("hello.txt")?;
  | |                                                ^ cannot use the `?`
operator in a function that returns `()`
5 | | }
  | |_- this function should return `Result` or `Option` to accept `?`
  |
  = help: the trait `FromResidual<Result<Infallible, std::io::Error>>` is not
implemented for `()`
```

这个错误指出我们只被允许在返回 `Result`、`Option` 或另一个实现了 `FromResidual` 的类型的函数中使用 `?` 运算符。

要修复这个错误，你有两个选择。一个选择是将函数的返回类型更改为与你正在使用 `?` 运算符的值兼容，只要你没有阻止这样做的限制。另一个选择是使用 `match` 或 `Result<T, E>` 的方法之一以适当的方式处理 `Result<T, E>`。

错误信息还提到 `?` 也可以与 `Option<T>` 值一起使用。与对 `Result` 使用 `?` 一样，你只能在返回 `Option` 的函数中对 `Option` 使用 `?`。当对 `Option<T>` 调用 `?` 运算符时，其行为类似于对 `Result<T, E>` 调用时的行为：如果值是 `None`，则在该点从函数中提前返回 `None`。如果值是 `Some`，则 `Some` 内部的值是表达式的结果值，函数继续执行。清单 9-11 有一个函数的示例，该函数找到给定文本中第一行的最后一个字符。

```rust
fn last_char_of_first_line(text: &str) -> Option<char> {
    text.lines().next()?.chars().last()
}
```

清单 9-11：对 `Option<T>` 值使用 `?` 运算符

这个函数返回 `Option<char>`，因为那里可能有一个字符，但也可能没有。这段代码接受 `text` 字符串切片参数，并对其调用 `lines` 方法，该方法返回字符串中各行的迭代器。因为这个函数想要检查第一行，所以它对迭代器调用 `next` 以从迭代器中获取第一个值。如果 `text` 是空字符串，对 `next` 的这个调用将返回 `None`，在这种情况下，我们使用 `?` 来停止并从 `last_char_of_first_line` 返回 `None`。如果 `text` 不是空字符串，`next` 将返回一个包含 `text` 中第一行字符串切片的 `Some` 值。

`?` 提取字符串切片，我们可以对该字符串切片调用 `chars` 以获取其字符的迭代器。我们对第一行中的最后一个字符感兴趣，所以我们调用 `last` 以返回迭代器中的最后一项。这是一个 `Option`，因为第一行可能是空字符串；例如，如果 `text` 以空行开头但其他行有字符，如 `"\nhi"`。然而，如果第一行有最后一个字符，它将在 `Some` 变体中返回。中间的 `?` 运算符为我们提供了一种简洁的方式来表达这个逻辑，使我们能够在一行中实现这个函数。如果我们不能对 `Option` 使用 `?` 运算符，我们将不得不使用更多的方法调用或 `match` 表达式来实现这个逻辑。

请注意，你可以在返回 `Result` 的函数中对 `Result` 使用 `?` 运算符，并且可以在返回 `Option` 的函数中对 `Option` 使用 `?` 运算符，但不能混合使用。`?` 运算符不会自动将 `Result` 转换为 `Option`，反之亦然；在这些情况下，你可以使用 `Result` 上的 `ok` 方法或 `Option` 上的 `ok_or` 方法来显式进行转换。

到目前为止，我们使用的所有 `main` 函数都返回 `()`。`main` 函数很特殊，因为它是可执行程序的入口点和出口点，并且对于程序按预期运行，其返回类型有一些限制。

幸运的是，`main` 也可以返回 `Result<(), E>`。清单 9-12 有清单 9-10 中的代码，但我们将 `main` 的返回类型更改为 `Result<(), Box<dyn Error>>`，并在末尾添加了返回值 `Ok(())`。这段代码现在将编译通过。

文件名：`src/main.rs`

```rust
use std::error::Error;
use std::fs::File;

fn main() -> Result<(), Box<dyn Error>> {
    let greeting_file = File::open("hello.txt")?;

    Ok(())
}
```

清单 9-12：将 `main` 改为返回 `Result<(), E>` 允许在 `Result` 值上使用 `?` 运算符。

`Box<dyn Error>` 类型是一个** trait 对象**，我们将在“使用允许不同类型值的 trait 对象”中讨论它。目前，你可以将 `Box<dyn Error>` 理解为“任何类型的错误”。在返回类型为 `Box<dyn Error>` 的 `main` 函数中对 `Result` 值使用 `?` 是允许的，因为它允许任何 `Err` 值提前返回。即使这个 `main` 函数的主体只会返回 `std::io::Error` 类型的错误，但通过指定 `Box<dyn Error>`，即使在 `main` 函数主体中添加了返回其他错误的更多代码，这个签名仍然是正确的。

当一个 `main` 函数返回 `Result<(), E>` 时，如果 `main` 返回 `Ok(())`，可执行程序将以值 `0` 退出，如果 `main` 返回 `Err` 值，可执行程序将以非零值退出。用 C 编写的可执行程序在退出时返回整数：成功退出的程序返回整数 `0`，出错的程序返回除 `0` 以外的某个整数。Rust 也从可执行程序中返回整数以与这个约定兼容。

`main` 函数可以返回任何实现了 `std::process::Termination` trait 的类型，该 trait 包含一个返回 `ExitCode` 的函数 `report`。有关为你自己的类型实现 `Termination` trait 的更多信息，请查阅标准库文档。

既然我们已经讨论了调用 `panic!` 或返回 `Result` 的细节，现在让我们回到如何决定在哪些情况下使用哪种方式更合适的话题。
