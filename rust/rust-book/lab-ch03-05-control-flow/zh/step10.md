# 使用 `for` 循环遍历集合

你可以选择使用 `while` 结构来遍历集合中的元素，比如数组。例如，清单 3-4 中的循环打印了数组 `a` 中的每个元素。

文件名：`src/main.rs`

```rust
fn main() {
    let a = [10, 20, 30, 40, 50];
    let mut index = 0;

    while index < 5 {
        println!("值是：{}", a[index]);

        index += 1;
    }
}
```

清单 3-4：使用 `while` 循环遍历集合中的每个元素

在这里，代码按顺序遍历数组中的元素。它从索引 `0` 开始，然后循环直到到达数组中的最后一个索引（也就是说，当 `index < 5` 不再为 `true` 时）。运行这段代码将打印数组中的每个元素：

```bash
$ cargo run
   正在编译 loops v0.1.0 (file:///projects/loops)
    已完成开发 [未优化 + 调试信息] 目标，耗时 0.32 秒
     正在运行 `target/debug/loops`
值是: 10
值是: 20
值是: 30
值是: 40
值是: 50
```

正如预期的那样，所有五个数组值都出现在终端中。即使 `index` 在某个时候会达到值 `5`，循环也会在尝试从数组中获取第六个值之前停止执行。

然而，这种方法容易出错；如果索引值或测试条件不正确，我们可能会导致程序恐慌。例如，如果你将 `a` 数组的定义改为有四个元素，但忘记将条件更新为 `while index < 4`，代码就会恐慌。它也很慢，因为编译器会添加运行时代码，以便在每次循环迭代时执行索引是否在数组边界内的条件检查。

作为一种更简洁的替代方法，你可以使用 `for` 循环，并为集合中的每个项执行一些代码。`for` 循环看起来像清单 3-5 中的代码。

文件名：`src/main.rs`

```rust
fn main() {
    let a = [10, 20, 30, 40, 50];

    for element in a {
        println!("值是：{element}");
    }
}
```

清单 3-5：使用 `for` 循环遍历集合中的每个元素

当我们运行这段代码时，我们将看到与清单 3-4 相同的输出。更重要的是，我们现在提高了代码的安全性，并消除了因超出数组末尾或未遍历足够远而遗漏一些项可能导致的错误。

使用 `for` 循环，如果改变数组中的值的数量，你不需要像在清单 3-4 中使用的方法那样记住更改任何其他代码。

`for` 循环的安全性和简洁性使其成为 Rust 中最常用的循环结构。即使在你想要像清单 3-3 中使用 `while` 循环的倒计时示例那样运行某些代码特定次数的情况下，大多数 Rust 开发者也会使用 `for` 循环。实现方法是使用标准库提供的 `Range`，它会生成从一个数字开始并在另一个数字之前结束的所有连续数字。

下面是使用 `for` 循环和我们尚未讨论过的另一种方法 `rev` 来反转范围的倒计时代码：

文件名：`src/main.rs`

```rust
fn main() {
    for number in (1..4).rev() {
        println!("{number}!");
    }
    println!("发射！！！");
}
```

这段代码是不是更好一些？
