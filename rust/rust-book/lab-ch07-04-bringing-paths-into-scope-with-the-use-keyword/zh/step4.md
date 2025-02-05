# 使用 `pub use` 重新导出名称

当我们使用 `use` 关键字将一个名称引入作用域时，在新作用域中可用的名称是私有的。为了使调用我们代码的代码能够像在该代码的作用域中定义的那样引用该名称，我们可以将 `pub` 和 `use` 结合使用。这种技术被称为 _重新导出_，因为我们将一个项引入作用域，但同时也使该项可供其他代码引入到它们的作用域中。

清单 7-17 展示了将清单 7-11 中根模块里的 `use` 改为 `pub use` 后的代码。

文件名：`src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

清单 7-17：使用 `pub use` 使一个名称在新作用域中可供任何代码使用

在进行此更改之前，外部代码必须使用路径 `restaurant::front_of_house::hosting::add_to_waitlist()` 来调用 `add_to_waitlist` 函数。现在，由于这个 `pub use` 从根模块重新导出了 `hosting` 模块，外部代码可以改为使用路径 `restaurant::hosting::add_to_waitlist()`。

当你的代码的内部结构与调用你代码的程序员对领域的思考方式不同时，重新导出会很有用。例如，在这个餐厅的比喻中，经营餐厅的人会考虑“前台”和“后台”。但是去餐厅就餐的顾客可能不会用这些术语来考虑餐厅的各个部分。通过 `pub use`，我们可以用一种结构编写代码，但暴露另一种结构。这样做能使我们的库对于编写库的程序员和调用库的程序员来说都组织良好。我们将在“使用 `pub use` 导出方便的公共 API”中查看 `pub use` 的另一个示例以及它如何影响你的 crate 的文档。
