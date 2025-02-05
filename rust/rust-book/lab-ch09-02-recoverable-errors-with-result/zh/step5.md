# 传播错误

当一个函数的实现调用了可能失败的操作时，你可以将错误返回给调用代码，而不是在函数内部处理错误，这样调用代码就能决定如何处理。这被称为**传播**错误，它能给调用代码更多控制权，因为在调用代码的上下文中，可能有更多信息或逻辑来决定如何处理错误，而不仅仅是你在自己代码中所拥有的。

例如，清单 9-6 展示了一个从文件中读取用户名的函数。如果文件不存在或无法读取，这个函数会将这些错误返回给调用该函数的代码。

文件名：`src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

1 fn read_username_from_file() -> Result<String, io::Error> {
  2 let username_file_result = File::open("hello.txt");

  3 let mut username_file = match username_file_result {
      4 Ok(file) => file,
      5 Err(e) => return Err(e),
    };

  6 let mut username = String::new();

  7 match username_file.read_to_string(&mut username) {
      8 Ok(_) => Ok(username),
      9 Err(e) => Err(e),
    }
}
```

清单 9-6：使用 `match` 将错误返回给调用代码的函数

这个函数可以用更简短的方式编写，但为了探索错误处理，我们先手动完成很多步骤；最后，我们会展示更简短的方式。让我们先看看函数的返回类型：`Result<String, io::Error>` \[1\]。这意味着函数返回一个 `Result<T, E>` 类型的值，其中泛型参数 `T` 被具体类型 `String` 填充，泛型类型 `E` 被具体类型 `io::Error` 填充。

如果这个函数成功且没有任何问题，调用这个函数的代码将收到一个包含 `String` 的 `Ok` 值 —— 即这个函数从文件中读取的 `username` \[8\]。如果这个函数遇到任何问题，调用代码将收到一个包含 `io::Error` 实例的 `Err` 值，该实例包含有关问题的更多信息。我们选择 `io::Error` 作为这个函数的返回类型，是因为这恰好是这个函数体中调用的两个可能失败的操作返回的错误值的类型：`File::open` 函数 \[2\] 和 `read_to_string` 方法 \[7\]。

函数体首先调用 `File::open` 函数 \[2\]。然后我们使用类似于清单 9-4 中的 `match` 来处理 `Result` 值。如果 `File::open` 成功，模式变量 `file` 中的文件句柄 \[4\] 成为可变变量 `username_file` 中的值 \[3\]，函数继续执行。在 `Err` 情况下，我们不调用 `panic!`，而是使用 `return` 关键字提前完全退出函数，并将 `File::open` 的错误值（现在在模式变量 `e` 中）作为这个函数的错误值返回给调用代码 \[5\]。

所以，如果 `username_file` 中有一个文件句柄，函数然后在变量 `username` 中创建一个新的 `String` \[6\]，并对 `username_file` 中的文件句柄调用 `read_to_string` 方法，将文件内容读入 `username` \[7\]。`read_to_string` 方法也返回一个 `Result`，因为它可能失败，即使 `File::open` 成功了。所以我们需要另一个 `match` 来处理那个 `Result`：如果 `read_to_string` 成功，那么我们的函数就成功了，我们返回文件中的用户名（现在在 `username` 中），并包装在一个 `Ok` 中。如果 `read_to_string` 失败，我们以与处理 `File::open` 返回值的 `match` 中返回错误值相同的方式返回错误值。不过，我们不需要明确写 `return`，因为这是函数中的最后一个表达式 \[9\]。

调用这段代码的代码然后将处理获取到的包含用户名的 `Ok` 值或包含 `io::Error` 的 `Err` 值。由调用代码决定如何处理这些值。如果调用代码得到一个 `Err` 值，它可以调用 `panic!` 并使程序崩溃，使用默认用户名，或者从文件以外的其他地方查找用户名，例如。我们没有足够的信息了解调用代码实际要做什么，所以我们向上传播所有的成功或错误信息，以便它能适当地处理。

这种传播错误的模式在 Rust 中非常常见，以至于 Rust 提供了问号运算符 `?` 来简化这个过程。
