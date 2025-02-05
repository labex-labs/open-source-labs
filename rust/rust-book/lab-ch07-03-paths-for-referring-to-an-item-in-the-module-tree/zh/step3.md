# 使用 `super` 开始相对路径

我们可以通过在路径开头使用 `super` 来构建从父模块开始的相对路径，而不是从当前模块或 crate 根开始。这类似于在文件系统路径中使用 `..` 语法。使用 `super` 使我们能够引用我们知道在父模块中的项，当模块与父模块密切相关，但父模块可能有一天会被移动到模块树的其他位置时，这可以使重新排列模块树更容易。

考虑清单 7-8 中的代码，它模拟了厨师纠正错误订单并亲自将其送到顾客手中的情况。在 `back_of_house` 模块中定义的 `fix_incorrect_order` 函数通过指定从 `super` 开始的 `deliver_order` 路径来调用父模块中定义的 `deliver_order` 函数。

文件名：`src/lib.rs`

```rust
fn deliver_order() {}

mod back_of_house {
    fn fix_incorrect_order() {
        cook_order();
        super::deliver_order();
    }

    fn cook_order() {}
}
```

清单 7-8：使用以 `super` 开头的相对路径调用函数

`fix_incorrect_order` 函数在 `back_of_house` 模块中，所以我们可以使用 `super` 进入 `back_of_house` 的父模块，在这种情况下是 `crate`，即根模块。从那里，我们查找 `deliver_order` 并找到了它。成功！我们认为 `back_of_house` 模块和 `deliver_order` 函数可能会保持彼此之间的相同关系，并且如果我们决定重新组织 crate 的模块树，它们会一起移动。因此，我们使用了 `super`，这样如果这段代码被移动到不同的模块，我们将来需要更新代码的地方就会更少。
