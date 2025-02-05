# 没有任何字段的类似单元的结构体

你还可以定义没有任何字段的结构体！这些被称为*类似单元的结构体*，因为它们的行为类似于我们在“元组类型”中提到的单元类型`()`。当你需要在某种类型上实现一个trait，但又没有任何想要存储在该类型本身的数据时，类似单元的结构体可能会很有用。我们将在第10章讨论trait。下面是一个声明并实例化一个名为`AlwaysEqual`的单元结构体的示例：

文件名：`src/main.rs`

```rust
struct AlwaysEqual;

fn main() {
    let subject = AlwaysEqual;
}
```

要定义`AlwaysEqual`，我们使用`struct`关键字、我们想要的名称，然后是一个分号。不需要花括号或圆括号！然后我们可以以类似的方式在`subject`变量中获取`AlwaysEqual`的一个实例：使用我们定义的名称，不需要任何花括号或圆括号。想象一下，稍后我们将为这个类型实现行为，使得`AlwaysEqual`的每个实例总是等于任何其他类型的每个实例，也许是为了在测试时有一个已知的结果。我们不需要任何数据来实现该行为！你将在第10章中看到如何定义trait并在任何类型上实现它们，包括类似单元的结构体。

> **结构体数据的所有权**
>
> 在清单5-1中的`User`结构体定义中，我们使用了拥有所有权的`String`类型，而不是`&str`字符串切片类型。这是一个有意的选择，因为我们希望这个结构体的每个实例都拥有其所有数据，并且只要整个结构体有效，该数据就有效。
>
> 结构体也可以存储对其他地方拥有的数据的引用，但这样做需要使用*生命周期*，这是Rust的一个特性，我们将在第10章讨论。生命周期确保结构体引用的数据在结构体存在期间一直有效。假设你尝试在结构体中存储一个引用而不指定生命周期，如下所示，在`src/main.rs`中：这是行不通的：
>
>     struct User {
>         active: bool,
>         username: &str,
>         email: &str,
>         sign_in_count: u64,
>     }
>
>     fn main() {
>         let user1 = User {
>             active: true,
>             username: "someusername123",
>             email: "someone@example.com",
>             sign_in_count: 1,
>         };
>     }
>
> 编译器会抱怨它需要生命周期说明符：
>
>     $ `cargo run`
>        Compiling structs v0.1.0 (file:///projects/structs)
>     error[E0106]: missing lifetime specifier
>      --> src/main.rs:3:15
>       |
>     3 |     username: &str,
>       |               ^ expected named lifetime parameter
>       |
>     help: consider introducing a named lifetime parameter
>       |
>     1 ~ struct User<'a> {
>     2 |     active: bool,
>     3 ~     username: &'a str,
>       |
>
>     error[E0106]: missing lifetime specifier
>      --> src/main.rs:4:12
>       |
>     4 |     email: &str,
>       |            ^ expected named lifetime parameter
>       |
>     help: consider introducing a named lifetime parameter
>       |
>     1 ~ struct User<'a> {
>     2 |     active: bool,
>     3 |     username: &str,
>     4 ~     email: &'a str,
>       |
>
> 在第10章中，我们将讨论如何修复这些错误，以便你可以在结构体中存储引用，但目前，我们将使用像`String`这样的拥有所有权的类型而不是像`&str`这样的引用来修复这些错误。
