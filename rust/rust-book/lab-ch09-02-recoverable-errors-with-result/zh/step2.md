# 匹配不同的错误

无论 `File::open` 为何失败，清单 9-4 中的代码都会调用 `panic!`。然而，我们希望针对不同的失败原因采取不同的操作。如果 `File::open` 因为文件不存在而失败，我们想要创建该文件并返回新文件的句柄。如果 `File::open` 因为任何其他原因失败 —— 例如，因为我们没有权限打开该文件 —— 我们仍然希望代码像清单 9-4 中那样调用 `panic!`。为此，我们添加了一个内部的 `match` 表达式，如清单 9-5 所示。

文件名：`src/main.rs`

```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => {
                match File::create("hello.txt") {
                    Ok(fc) => fc,
                    Err(e) => panic!(
                        "Problem creating the file: {:?}",
                        e
                    ),
                }
            }
            other_error => {
                panic!(
                    "Problem opening the file: {:?}",
                    other_error
                );
            }
        },
    };
}
```

清单 9-5：以不同方式处理不同类型的错误

`File::open` 在 `Err` 变体中返回的值的类型是 `io::Error`，它是标准库提供的一个结构体。这个结构体有一个方法 `kind`，我们可以调用它来获取一个 `io::ErrorKind` 值。枚举 `io::ErrorKind` 由标准库提供，它有一些变体，表示 `io` 操作可能导致的不同类型的错误。我们想要使用的变体是 `ErrorKind::NotFound`，它表示我们试图打开的文件尚不存在。所以我们对 `greeting_file_result` 进行匹配，但我们也对 `error.kind()` 进行了内部匹配。

我们想要在内部匹配中检查的条件是 `error.kind()` 返回的值是否是 `ErrorKind` 枚举的 `NotFound` 变体。如果是，我们尝试用 `File::create` 创建文件。然而，因为 `File::create` 也可能失败，所以我们在内部 `match` 表达式中需要第二个分支。当文件无法创建时，会打印不同的错误消息。外部 `match` 的第二个分支保持不变，所以除了文件缺失错误之外的任何错误都会使程序调用 `panic!`。
