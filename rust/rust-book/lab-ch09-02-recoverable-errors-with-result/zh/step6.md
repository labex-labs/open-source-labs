# 传播错误的快捷方式：问号运算符（? 运算符）

清单 9-7 展示了 `read_username_from_file` 的另一种实现，它与清单 9-6 具有相同的功能，但此实现使用了 `?` 运算符。

文件名：`src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?;
    let mut username = String::new();
    username_file.read_to_string(&mut username)?;
    Ok(username)
}
```

清单 9-7：使用 `?` 运算符将错误返回给调用代码的函数

放在 `Result` 值之后的 `?` 运算符，其定义的工作方式与我们在清单 9-6 中定义的用于处理 `Result` 值的 `match` 表达式几乎相同。如果 `Result` 的值是 `Ok`，则 `Ok` 内部的值将从这个表达式返回，程序将继续执行。如果值是 `Err`，则 `Err` 将从整个函数返回，就好像我们使用了 `return` 关键字一样，这样错误值就会传播到调用代码。

清单 9-6 中的 `match` 表达式与 `?` 运算符的作用存在一个区别：对其调用 `?` 运算符的错误值会通过标准库中 `From` trait 定义的 `from` 函数，该函数用于将值从一种类型转换为另一种类型。当 `?` 运算符调用 `from` 函数时，接收到的错误类型会被转换为当前函数返回类型中定义的错误类型。这在一个函数返回一种错误类型以表示函数可能失败的所有方式时非常有用，即使部分操作可能因许多不同原因而失败。

例如，我们可以将清单 9-7 中的 `read_username_from_file` 函数修改为返回我们定义的名为 `OurError` 的自定义错误类型。如果我们还定义了 `impl From<io::Error> for OurError` 以从 `io::Error` 构造 `OurError` 的实例，那么 `read_username_from_file` 函数体中的 `?` 运算符调用将调用 `from` 并转换错误类型，而无需向函数添加更多代码。

在清单 9-7 的上下文中，`File::open` 调用末尾的 `?` 会将 `Ok` 内部的值返回给变量 `username_file`。如果发生错误，`?` 运算符将提前从整个函数返回，并将任何 `Err` 值提供给调用代码。`read_to_string` 调用末尾的 `?` 也是如此。

`?` 运算符消除了大量样板代码，使这个函数的实现更简单。我们甚至可以通过在 `?` 之后立即链接方法调用，进一步缩短这段代码，如清单 9-8 所示。

文件名：`src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username = String::new();

    File::open("hello.txt")?.read_to_string(&mut username)?;

    Ok(username)
}
```

清单 9-8：在 `?` 运算符之后链接方法调用

我们将在 `username` 中创建新 `String` 的操作移到了函数开头；这部分没有变化。我们没有创建变量 `username_file`，而是直接将对 `read_to_string` 的调用链接到 `File::open("hello.txt")?` 的结果上。在 `read_to_string` 调用的末尾我们仍然有一个 `?`，并且当 `File::open` 和 `read_to_string` 都成功时，我们仍然返回一个包含 `username` 的 `Ok` 值，而不是返回错误。功能再次与清单 9-6 和清单 9-7 相同；这只是一种不同的、更符合人体工程学的编写方式。

清单 9-9 展示了一种使用 `fs::read_to_string` 使代码更简短的方法。

文件名：`src/main.rs`

```rust
use std::fs;
use std::io;

fn read_username_from_file() -> Result<String, io::Error> {
    fs::read_to_string("hello.txt")
}
```

清单 9-9：使用 `fs::read_to_string` 而不是先打开文件然后读取

将文件读取为字符串是一个相当常见的操作，所以标准库提供了方便的 `fs::read_to_string` 函数，它会打开文件、创建一个新的 `String`、读取文件内容、将内容放入该 `String` 并返回它。当然，使用 `fs::read_to_string` 没有给我们机会解释所有的错误处理，所以我们先采用了较长的方式。
