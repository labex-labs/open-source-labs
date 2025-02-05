# 定义我们自己的智能指针

让我们构建一个类似于标准库提供的 `Box<T>` 类型的智能指针，以体验智能指针在默认情况下与引用的行为有何不同。然后我们将看看如何添加使用解引用运算符的能力。

`Box<T>` 类型最终被定义为一个带有一个元素的元组结构体，所以清单15-8以相同的方式定义了一个 `MyBox<T>` 类型。我们还将定义一个 `new` 函数，以匹配在 `Box<T>` 上定义的 `new` 函数。

文件名：`src/main.rs`

```rust
 1 struct MyBox<T>(T);

impl<T> MyBox<T> {
  2 fn new(x: T) -> MyBox<T> {
      3 MyBox(x)
    }
}
```

清单15-8：定义一个 `MyBox<T>` 类型

我们定义了一个名为 `MyBox` 的结构体，并声明了一个泛型参数 `T` （第1行），因为我们希望我们的类型能够持有任何类型的值。`MyBox` 类型是一个带有一个 `T` 类型元素的元组结构体。`MyBox::new` 函数接受一个 `T` 类型的参数（第2行），并返回一个持有传入值的 `MyBox` 实例（第3行）。

让我们尝试将清单15-7中的 `main` 函数添加到清单15-8中，并将其修改为使用我们定义的 `MyBox<T>` 类型而不是 `Box<T>`。清单15-9中的代码不会编译，因为 Rust 不知道如何对 `MyBox` 进行解引用。

文件名：`src/main.rs`

```rust
fn main() {
    let x = 5;
    let y = MyBox::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);
}
```

清单15-9：尝试以使用引用和 `Box<T>` 的相同方式使用 `MyBox<T>`

这是产生的编译错误：

```bash
error[E0614]: type `MyBox<{integer}>` cannot be dereferenced
  --> src/main.rs:14:19
   |
14 |     assert_eq!(5, *y);
   |                   ^^
```

我们的 `MyBox<T>` 类型不能被解引用，因为我们还没有在我们的类型上实现这种能力。为了能够使用 `*` 运算符进行解引用，我们需要实现 `Deref` 特性。
