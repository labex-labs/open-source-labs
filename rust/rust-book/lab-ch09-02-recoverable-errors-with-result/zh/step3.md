# 替代使用 `match` 处理 `Result<T, E>` 的方法

这么多 `match` 表达式啊！`match` 表达式非常有用，但也是一种非常原始的方式。在第 13 章中，你将学习闭包，它们会与许多在 `Result<T, E>` 上定义的方法一起使用。当你在代码中处理 `Result<T, E>` 值时，这些方法可能比使用 `match` 更简洁。

例如，这是另一种编写与清单 9-5 中相同逻辑的方式，这次使用闭包和 `unwrap_or_else` 方法：

    // src/main.rs
    use std::fs::File;
    use std::io::ErrorKind;

    fn main() {
        let greeting_file = File::open("hello.txt").unwrap_or_else(|error| {
            if error.kind() == ErrorKind::NotFound {
                File::create("hello.txt").unwrap_or_else(|error| {
                    panic!("Problem creating the file: {:?}", error);
                })
            } else {
                panic!("Problem opening the file: {:?}", error);
            }
        });
    }

虽然这段代码的行为与清单 9-5 相同，但它不包含任何 `match` 表达式，并且阅读起来更简洁。在你读完第 13 章后再回到这个例子，并在标准库文档中查找 `unwrap_or_else` 方法。当你处理错误时，还有更多这样的方法可以清理庞大的嵌套 `match` 表达式。
