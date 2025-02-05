# 作为输入参数

虽然 Rust 大多在没有类型注释的情况下动态选择如何捕获变量，但在编写函数时不允许这种模糊性。当以闭包作为输入参数时，必须使用几个 `trait` 之一来注释闭包的完整类型，这些 `trait` 由闭包对捕获值的处理方式决定。按照限制程度从高到低的顺序，它们是：

- `Fn`：闭包通过引用（`&T`）使用捕获的值
- `FnMut`：闭包通过可变引用（`&mut T`）使用捕获的值
- `FnOnce`：闭包通过值（`T`）使用捕获的值

在逐个变量的基础上，编译器将以尽可能宽松的方式捕获变量。

例如，考虑一个注释为 `FnOnce` 的参数。这指定闭包 _可以_ 通过 `&T`、`&mut T` 或 `T` 进行捕获，但编译器最终会根据捕获的变量在闭包中的使用方式来选择。

这是因为如果可以进行移动，那么任何类型的借用也应该是可能的。请注意，反之则不成立。如果参数注释为 `Fn`，那么不允许通过 `&mut T` 或 `T` 捕获变量。但是，允许通过 `&T` 捕获。

在以下示例中，尝试交换 `Fn`、`FnMut` 和 `FnOnce` 的用法，看看会发生什么：

```rust
// 一个接受闭包作为参数并调用它的函数。
// <F> 表示 F 是一个“泛型类型参数”
fn apply<F>(f: F) where
    // 闭包不接受输入且不返回任何值。
    F: FnOnce() {
    // ^ TODO：尝试将此改为 `Fn` 或 `FnMut`。

    f();
}

// 一个接受闭包并返回 `i32` 的函数。
fn apply_to_3<F>(f: F) -> i32 where
    // 闭包接受一个 `i32` 并返回一个 `i32`。
    F: Fn(i32) -> i32 {

    f(3)
}

fn main() {
    use std::mem;

    let greeting = "hello";
    // 一个非复制类型。
    // `to_owned` 从借用的数据创建拥有的数据
    let mut farewell = "goodbye".to_owned();

    // 捕获两个变量：通过引用捕获 `greeting` 并
    // 通过值捕获 `farewell`。
    let diary = || {
        // `greeting` 是通过引用：需要 `Fn`。
        println!("I said {}.", greeting);

        // 变异迫使 `farewell` 通过
        // 可变引用捕获。现在需要 `FnMut`。
        farewell.push_str("!!!");
        println!("Then I screamed {}.", farewell);
        println!("Now I can sleep. zzzzz");

        // 手动调用 drop 迫使 `farewell` 通过
        // 值捕获。现在需要 `FnOnce`。
        mem::drop(farewell);
    };

    // 调用应用闭包的函数。
    apply(diary);

    // `double` 满足 `apply_to_3` 的 trait 约束
    let double = |x| 2 * x;

    println!("3 doubled: {}", apply_to_3(double));
}
```
