# 迭代器 trait 与 next 方法

所有迭代器都实现了一个在标准库中定义的名为 `Iterator` 的 trait。该 trait 的定义如下：

```rust
pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;

    // 省略了具有默认实现的方法
}
```

注意，这个定义使用了一些新语法：`type Item` 和 `Self::Item`，它们正在为这个 trait 定义一个「关联类型」。我们将在第 19 章深入讨论关联类型。目前，你只需要知道这段代码表明实现 `Iterator` trait 需要你也定义一个 `Item` 类型，并且这个 `Item` 类型用于 `next` 方法的返回类型。换句话说，`Item` 类型将是迭代器返回的类型。

`Iterator` trait 只要求实现者定义一个方法：`next` 方法，它一次返回迭代器的一个项目，包装在 `Some` 中，并且在迭代结束时返回 `None`。

我们可以直接在迭代器上调用 `next` 方法；清单 13-12 展示了对从向量创建的迭代器重复调用 `next` 时返回的值。

文件名：`src/lib.rs`

```rust
#[test]
fn iterator_demonstration() {
    let v1 = vec![1, 2, 3];

    let mut v1_iter = v1.iter();

    assert_eq!(v1_iter.next(), Some(&1));
    assert_eq!(v1_iter.next(), Some(&2));
    assert_eq!(v1_iter.next(), Some(&3));
    assert_eq!(v1_iter.next(), None);
}
```

清单 13-12：在迭代器上调用 `next` 方法

注意，我们需要使 `v1_iter` 可变：在迭代器上调用 `next` 方法会改变迭代器用于跟踪其在序列中位置的内部状态。换句话说，这段代码「消耗」或用完了迭代器。每次调用 `next` 都会从迭代器中消耗一个项目。当我们使用 `for` 循环时，不需要使 `v1_iter` 可变，因为循环获取了 `v1_iter` 的所有权并在幕后使其可变。

还要注意，我们从调用 `next` 中得到的值是对向量中值的不可变引用。`iter` 方法产生一个针对不可变引用的迭代器。如果我们想创建一个获取 `v1` 的所有权并返回拥有值的迭代器，我们可以调用 `into_iter` 而不是 `iter`。同样，如果我们想遍历可变引用，我们可以调用 `iter_mut` 而不是 `iter`。
