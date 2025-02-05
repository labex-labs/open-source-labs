# 隐藏实现细节的封装

另一个通常与面向对象编程相关联的方面是「封装」的概念，这意味着使用对象的代码无法访问该对象的实现细节。因此，与对象进行交互的唯一方式是通过其公共 API；使用该对象的代码不应能够深入到对象的内部并直接更改数据或行为。这使程序员能够在无需更改使用该对象的代码的情况下，更改和重构对象的内部实现。

我们在第 7 章讨论了如何控制封装：我们可以使用 `pub` 关键字来决定代码中的哪些模块、类型、函数和方法应该是公共的，默认情况下其他所有内容都是私有的。例如，我们可以定义一个结构体 `AveragedCollection`，它有一个字段包含 `i32` 值的向量。该结构体还可以有一个字段包含向量中值的平均值，这意味着不必在每次有人需要时按需计算平均值。换句话说，`AveragedCollection` 将为我们缓存计算出的平均值。清单 17-1 展示了 `AveragedCollection` 结构体的定义。

文件名：`src/lib.rs`

```rust
pub struct AveragedCollection {
    list: Vec<i32>,
    average: f64,
}
```

清单 17-1：一个 `AveragedCollection` 结构体，它维护一个整数列表以及该列表中元素的平均值

该结构体被标记为 `pub`，以便其他代码可以使用它，但结构体中的字段仍然是私有的。在这种情况下这很重要，因为我们希望确保每当向列表中添加或删除一个值时，平均值也会更新。我们通过在结构体上实现 `add`、`remove` 和 `average` 方法来做到这一点，如清单 17-2 所示。

文件名：`src/lib.rs`

```rust
impl AveragedCollection {
    pub fn add(&mut self, value: i32) {
        self.list.push(value);
        self.update_average();
    }

    pub fn remove(&mut self) -> Option<i32> {
        let result = self.list.pop();
        match result {
            Some(value) => {
                self.update_average();
                Some(value)
            }
            None => None,
        }
    }

    pub fn average(&self) -> f64 {
        self.average
    }

    fn update_average(&mut self) {
        let total: i32 = self.list.iter().sum();
        self.average = total as f64 / self.list.len() as f64;
    }
}
```

清单 17-2：`AveragedCollection` 上公共方法 `add`、`remove` 和 `average` 的实现

公共方法 `add`、`remove` 和 `average` 是访问或修改 `AveragedCollection` 实例中数据的唯一方式。当使用 `add` 方法向 `list` 中添加一个元素或使用 `remove` 方法删除一个元素时，每个方法的实现都会调用私有的 `update_average` 方法，该方法负责处理更新 `average` 字段。

我们将 `list` 和 `average` 字段设为私有，这样外部代码就无法直接向 `list` 字段中添加或删除元素；否则，当 `list` 发生变化时，`average` 字段可能会不同步。`average` 方法返回 `average` 字段中的值，允许外部代码读取 `average` 但不能修改它。

因为我们已经封装了 `AveragedCollection` 结构体的实现细节，所以将来我们可以轻松地更改一些方面，比如数据结构。例如，我们可以将 `list` 字段的 `Vec<i32>` 换成 `HashSet<i32>`。只要 `add`、`remove` 和 `average` 公共方法的签名保持不变，使用 `AveragedCollection` 的代码就无需更改。如果我们将 `list` 设为公共的，情况就不一定如此了：`HashSet<i32>` 和 `Vec<i32>` 有不同的添加和删除元素的方法，所以如果外部代码直接修改 `list`，很可能需要更改。

如果封装是一门语言被视为面向对象所需的一个方面，那么 Rust 满足这一要求。对代码的不同部分使用或不使用 `pub` 的选项能够实现对实现细节的封装。
