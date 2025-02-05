# 类函数宏

类函数宏定义的宏看起来像函数调用。与 `macro_rules!` 宏类似，它们比函数更灵活；例如，它们可以接受数量不定的参数。然而，`macro_rules!` 宏只能使用我们在“使用 `macro_rules!` 的声明式宏进行通用元编程”中讨论的类似 `match` 的语法来定义。类函数宏接受一个 `TokenStream` 参数，并且它们的定义像其他两种过程宏一样，使用 Rust 代码来操作该 `TokenStream`。一个类函数宏的示例是 `sql!` 宏，它可能会像这样被调用：

```rust
let sql = sql!(SELECT * FROM posts WHERE id=1);
```

这个宏会解析其中的 SQL 语句并检查其语法是否正确，这是一个比 `macro_rules!` 宏能做的复杂得多的处理过程。`sql!` 宏会像这样定义：

```rust
#[proc_macro]
pub fn sql(input: TokenStream) -> TokenStream {
```

这个定义类似于自定义 `derive` 宏的签名：我们接收括号内的标记并返回我们想要生成的代码。
