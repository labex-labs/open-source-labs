# 借用

大多数情况下，我们希望在不获取数据所有权的情况下访问它。为实现这一点，Rust 使用了一种**借用**机制。对象不是按值（`T`）传递，而是可以通过引用（`&T`）传递。

编译器通过其借用检查器静态地保证引用**始终**指向有效的对象。也就是说，在存在对某个对象的引用时，该对象不能被销毁。

```rust
// 此函数获取一个装箱的 i32 的所有权并销毁它
fn eat_box_i32(boxed_i32: Box<i32>) {
    println!("Destroying box that contains {}", boxed_i32);
}

// 此函数借用一个 i32
fn borrow_i32(borrowed_i32: &i32) {
    println!("This int is: {}", borrowed_i32);
}

fn main() {
    // 创建一个装箱的 i32 和一个栈上的 i32
    let boxed_i32 = Box::new(5_i32);
    let stacked_i32 = 6_i32;

    // 借用装箱内容。未获取所有权，
    // 因此内容可以再次被借用。
    borrow_i32(&boxed_i32);
    borrow_i32(&stacked_i32);

    {
        // 获取对装箱内数据的引用
        let _ref_to_i32: &i32 = &boxed_i32;

        // 错误！
        // 在作用域稍后部分内部值被借用时，不能销毁 `boxed_i32`。
        eat_box_i32(boxed_i32);
        // FIXME ^ 注释掉这一行

        // 在内部值被销毁后尝试借用 `_ref_to_i32`
        borrow_i32(_ref_to_i32);
        // `_ref_to_i32` 超出作用域，不再被借用。
    }

    // `boxed_i32` 现在可以将所有权交给 `eat_box` 并被销毁
    eat_box_i32(boxed_i32);
}
```
