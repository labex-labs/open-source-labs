# 文档测试

记录 Rust 项目的主要方式是通过注释源代码。文档注释是用 CommonMark Markdown 规范编写的，并且支持其中的代码块。Rust 会确保正确性，因此这些代码块会被编译并用作文档测试。

````rust
/// 第一行是描述函数的简短摘要。
///
/// 接下来的几行是详细的文档。代码块以三个反引号开头，内部有隐式的 `fn main()`
/// 以及 `extern crate <cratename>`。假设我们正在测试 `doccomments` 包：
///
/// ```
/// let result = doccomments::add(2, 3);
/// assert_eq!(result, 5);
/// ```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

/// 通常文档注释可能包括 “示例”、“恐慌” 和 “失败” 部分。
///
/// 接下来的函数用于两个数相除。
///
/// # 示例
///
/// ```
/// let result = doccomments::div(10, 2);
/// assert_eq!(result, 5);
/// ```
///
/// # 恐慌
///
/// 如果第二个参数为零，该函数会恐慌。
///
/// ```rust
/// // 除以零会恐慌
/// doccomments::div(10, 0);
/// ```
pub fn div(a: i32, b: i32) -> i32 {
    if b == 0 {
        panic!("Divide-by-zero error");
    }

    a / b
}
````

在运行常规的 `cargo test` 命令时，文档中的代码块会自动进行测试：

```shell

```

## 文档测试背后的动机

文档测试的主要目的是作为展示功能的示例，这是最重要的准则之一。它允许将文档中的示例用作完整的代码片段。但是使用 `?` 会使编译失败，因为 `main` 返回 `unit`。隐藏文档中的某些源代码行的功能就派上用场了：可以编写 `fn try_main() -> Result<(), ErrorType>`，将其隐藏起来，并在隐藏的 `main` 中对其进行 `unwrap`。听起来很复杂？这里有一个示例：

````rust
/// 在文档测试中使用隐藏的 `try_main`。
///
/// ```
/// # // 隐藏的行以 `#` 符号开头，但它们仍然是可编译的！
/// # fn try_main() -> Result<(), String> { // 包装文档中显示的主体的行
/// let res = doccomments::try_div(10, 2)?;
/// # Ok(()) // 从 try_main 返回
/// # }
/// # fn main() { // 开始会调用 unwrap() 的 main
/// #    try_main().unwrap(); // 调用 try_main 并展开
/// #                         // 以便在出错时测试会恐慌
/// # }
/// ```
pub fn try_div(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        Err(String::from("Divide-by-zero"))
    } else {
        Ok(a / b)
    }
}
````
