# `where` 子句

边界也可以使用紧跟在左花括号 `{` 之前的 `where` 子句来表达，而不是在类型首次出现时表达。此外，`where` 子句可以将边界应用于任意类型，而不仅仅是类型参数。

`where` 子句有用的一些情况：

- 当分别指定泛型类型和边界更清晰时：

```rust
impl <A: TraitB + TraitC, D: TraitE + TraitF> MyTrait<A, D> for YourType {}

// 使用 `where` 子句表达边界
impl <A, D> MyTrait<A, D> for YourType where
    A: TraitB + TraitC,
    D: TraitE + TraitF {}
```

- 当使用 `where` 子句比使用普通语法更具表现力时。在这个例子中，如果没有 `where` 子句，`impl` 无法直接表达：

```rust
use std::fmt::Debug;

trait PrintInOption {
    fn print_in_option(self);
}

// 因为否则我们将不得不表示为 `T: Debug` 或者
// 使用另一种间接方法，所以这需要一个 `where` 子句：
impl<T> PrintInOption for T where
    Option<T>: Debug {
    // 我们希望 `Option<T>: Debug` 作为我们的边界，因为这是要打印的内容。否则会使用错误的边界。
    fn print_in_option(self) {
        println!("{:?}", Some(self));
    }
}

fn main() {
    let vec = vec![1, 2, 3];

    vec.print_in_option();
}
```
