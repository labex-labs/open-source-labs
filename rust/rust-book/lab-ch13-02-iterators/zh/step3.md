# 消耗迭代器的方法

`Iterator` trait 有许多由标准库提供默认实现的不同方法；你可以通过查看 `Iterator` trait 的标准库 API 文档来了解这些方法。其中一些方法在其定义中调用了 `next` 方法，这就是为什么在实现 `Iterator` trait 时需要实现 `next` 方法。

调用 `next` 的方法被称为「消耗适配器」，因为调用它们会用完迭代器。一个例子是 `sum` 方法，它获取迭代器的所有权，并通过重复调用 `next` 来遍历项目，从而消耗迭代器。在遍历过程中，它将每个项目加到一个运行总和中，并在迭代完成时返回总和。清单 13-13 有一个测试说明了 `sum` 方法的使用。

文件名：`src/lib.rs`

```rust
#[test]
fn iterator_sum() {
    let v1 = vec![1, 2, 3];

    let v1_iter = v1.iter();

    let total: i32 = v1_iter.sum();

    assert_eq!(total, 6);
}
```

清单 13-13：调用 `sum` 方法以获取迭代器中所有项目的总和

在调用 `sum` 之后，我们不能再使用 `v1_iter`，因为 `sum` 获取了我们在其上调用它的迭代器的所有权。
