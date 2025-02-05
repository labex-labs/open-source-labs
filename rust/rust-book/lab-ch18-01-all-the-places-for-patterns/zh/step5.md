# `for` 循环

在 `for` 循环中，紧跟在关键字 `for` 后面的值是一个模式。例如，在 `for x in y` 中，`x` 就是模式。清单 18-3 展示了如何在 `for` 循环中使用模式来进行 _解构_，也就是将一个元组拆开，作为 `for` 循环的一部分。

文件名：`src/main.rs`

```rust
let v = vec!['a', 'b', 'c'];

for (index, value) in v.iter().enumerate() {
    println!("{value} is at index {index}");
}
```

清单 18-3：在 `for` 循环中使用模式解构元组

清单 18-3 中的代码将打印以下内容：

```
a is at index 0
b is at index 1
c is at index 2
```

我们使用 `enumerate` 方法来适配一个迭代器，使其产生一个值以及该值的索引，并将它们放入一个元组中。产生的第一个值是元组 `(0, 'a')`。当这个值与模式 `(index, value)` 匹配时，`index` 将是 `0`，`value` 将是 `'a'`，从而打印出输出的第一行。
