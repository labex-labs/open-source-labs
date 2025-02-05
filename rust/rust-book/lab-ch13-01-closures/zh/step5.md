# 从闭包中移出捕获的值与 `Fn` 特质

一旦闭包从其定义的环境中捕获了引用或获取了值的所有权（从而影响了有什么东西被移入闭包），闭包体中的代码就定义了在稍后对闭包求值时，这些引用或值会发生什么（从而影响有什么东西被移出闭包）。

闭包体可以执行以下任何操作：将捕获的值移出闭包、变异捕获的值、既不移出也不变异该值，或者一开始就不从环境中捕获任何东西。

闭包从环境中捕获和处理值的方式会影响闭包实现的特质，而特质是函数和结构体指定它们可以使用哪些类型的闭包的方式。闭包会根据其体处理值的方式，以累加的方式自动实现这些 `Fn` 特质中的一个、两个或全部三个：

- `FnOnce` 适用于只能被调用一次的闭包。所有闭包至少都实现这个特质，因为所有闭包都可以被调用。一个将捕获的值移出其体的闭包只会实现 `FnOnce`，而不会实现其他任何 `Fn` 特质，因为它只能被调用一次。
- `FnMut` 适用于不会将捕获的值移出其体，但可能会变异捕获的值的闭包。这些闭包可以被调用多次。
- `Fn` 适用于不会将捕获的值移出其体且不会变异捕获的值的闭包，以及不从其环境中捕获任何东西的闭包。这些闭包可以在不改变其环境的情况下被调用多次，这在诸如并发多次调用闭包的情况下很重要。

让我们看看清单13-1中使用的 `Option<T>` 上的 `unwrap_or_else` 方法的定义：

```rust
impl<T> Option<T> {
    pub fn unwrap_or_else<F>(self, f: F) -> T
    where
        F: FnOnce() -> T
    {
        match self {
            Some(x) => x,
            None => f(),
        }
    }
}
```

回想一下，`T` 是表示 `Option` 的 `Some` 变体中的值的类型的泛型类型。那个类型 `T` 也是 `unwrap_or_else` 函数的返回类型：例如，在 `Option<String>` 上调用 `unwrap_or_else` 的代码将得到一个 `String`。

接下来，注意 `unwrap_or_else` 函数有一个额外的泛型类型参数 `F`。`F` 类型是名为 `f` 的参数的类型，`f` 是我们在调用 `unwrap_or_else` 时提供的闭包。

在泛型类型 `F` 上指定的特质约束是 `FnOnce() -> T`，这意味着 `F` 必须能够被调用一次，不接受任何参数，并返回一个 `T`。在特质约束中使用 `FnOnce` 表达了 `unwrap_or_else` 最多只会调用 `f` 一次的约束。在 `unwrap_or_else` 的体中，我们可以看到如果 `Option` 是 `Some`，就不会调用 `f`。如果 `Option` 是 `None`，就会调用 `f` 一次。因为所有闭包都实现 `FnOnce`，所以 `unwrap_or_else` 接受种类最多的闭包，并且尽可能灵活。

> 注意：函数也可以实现所有三个 `Fn` 特质。如果我们想做的事情不需要从环境中捕获值，那么在我们需要实现其中一个 `Fn` 特质的地方，我们可以使用函数名而不是闭包。例如，在 `Option<Vec<T>>` 值上，如果值是 `None`，我们可以调用 `unwrap_or_else(Vec::new)` 来获取一个新的空向量。

现在让我们看看标准库在切片上定义的方法 `sort_by_key`，看看它与 `unwrap_or_else` 有何不同，以及为什么 `sort_by_key` 在特质约束中使用 `FnMut` 而不是 `FnOnce`。闭包以对正在考虑的切片中的当前项的引用的形式获取一个参数，并返回一个可排序的 `K` 类型的值。当你想根据每个项的特定属性对切片进行排序时，这个函数很有用。在清单13-7中，我们有一个 `Rectangle` 实例的列表，我们使用 `sort_by_key` 按它们的 `width` 属性从低到高对它们进行排序。

文件名：`src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 3, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    list.sort_by_key(|r| r.width);
    println!("{:#?}", list);
}
```

清单13-7：使用 `sort_by_key` 按宽度对矩形进行排序

这段代码打印：

    [
        Rectangle {
            width: 3,
            height: 5,
        },
        Rectangle {
            width: 7,
            height: 12,
        },
        Rectangle {
            width: 10,
            height: 1,
        },
    ]

`sort_by_key` 被定义为接受一个 `FnMut` 闭包的原因是它会多次调用该闭包：对切片中的每个项调用一次。闭包 `|r| r.width` 不会从其环境中捕获、变异或移出任何东西，所以它满足特质约束要求。

相比之下，清单13-8展示了一个只实现 `FnOnce` 特质的闭包的示例，因为它从环境中移出了一个值。编译器不会让我们将这个闭包与 `sort_by_key` 一起使用。

文件名：`src/main.rs`

```rust
--snip--

fn main() {
    let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 3, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    let mut sort_operations = vec![];
    let value = String::from("by key called");

    list.sort_by_key(|r| {
        sort_operations.push(value);
        r.width
    });
    println!("{:#?}", list);
}
```

清单13-8：尝试将 `FnOnce` 闭包与 `sort_by_key` 一起使用

这是一种人为设计的、复杂的（且不起作用的）尝试计算对 `list` 进行排序时 `sort_by_key` 被调用次数的方法。这段代码试图通过将 `value`（闭包环境中的一个 `String`）推入 `sort_operations` 向量来进行计数。闭包捕获 `value`，然后通过将 `value` 的所有权转移到 `sort_operations` 向量，将 `value` 移出闭包。这个闭包只能被调用一次；尝试第二次调用它将不起作用，因为 `value` 不再在环境中，无法再次被推入 `sort_operations`！因此，这个闭包只实现了 `FnOnce`。当我们尝试编译这段代码时，我们会得到一个错误，提示 `value` 不能从闭包中移出，因为闭包必须实现 `FnMut`：

```bash
error[E0507]: cannot move out of `value`, a captured variable in an `FnMut`
closure
  --> src/main.rs:18:30
   |
15 |       let value = String::from("by key called");
   |           ----- captured outer variable
16 |
17 |       list.sort_by_key(|r| {
   |  ______________________-
18 | |         sort_operations.push(value);
   | |                              ^^^^^ move occurs because `value` has
type `String`, which does not implement the `Copy` trait
19 | |         r.width
20 | |     });
   | |_____- captured by this `FnMut` closure
```

错误指向闭包体中移出 `value` 的那一行。要解决这个问题，我们需要更改闭包体，使其不从环境中移出值。在环境中保留一个计数器，并在闭包体中递增其值，是一种更直接的计算 `sort_by_key` 被调用次数的方法。清单13-9中的闭包可以与 `sort_by_key` 一起使用，因为它只捕获对 `num_sort_operations` 计数器的可变引用，因此可以被调用多次。

文件名：`src/main.rs`

```rust
--snip--

fn main() {
    --snip--

    let mut num_sort_operations = 0;
    list.sort_by_key(|r| {
        num_sort_operations += 1;
        r.width
    });
    println!(
        "{:#?}, sorted in {num_sort_operations} operations",
        list
    );
}
```

清单13-9：允许使用 `FnMut` 闭包与 `sort_by_key` 一起使用

在定义或使用利用闭包的函数或类型时，`Fn` 特质很重要。在下一节中，我们将讨论迭代器。许多迭代器方法都接受闭包参数，所以在我们继续学习时，请记住这些闭包的细节！
