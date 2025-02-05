# 类属性宏

类属性宏类似于自定义 `derive` 宏，但它们不是为 `derive` 属性生成代码，而是允许你创建新的属性。它们也更灵活：`derive` 仅适用于结构体和枚举；属性还可以应用于其他项，例如函数。下面是一个使用类属性宏的示例。假设你有一个名为 `route` 的属性，用于在使用 Web 应用程序框架时注释函数：

```rust
#[route(GET, "/")]
fn index() {
```

这个 `#[route]` 属性将由框架定义为一个过程宏。宏定义函数的签名如下所示：

    #[proc_macro_attribute]
    pub fn route(
        attr: TokenStream,
        item: TokenStream
    ) -> TokenStream {

在这里，我们有两个 `TokenStream` 类型的参数。第一个用于属性的内容：即 `GET, "/"` 部分。第二个是属性所附加到的项的主体：在这种情况下，是 `fn index() {}` 以及函数主体的其余部分。

除此之外，类属性宏的工作方式与自定义 `derive` 宏相同：你创建一个具有 `proc-macro` crate 类型的 crate，并实现一个生成你想要的代码的函数！
