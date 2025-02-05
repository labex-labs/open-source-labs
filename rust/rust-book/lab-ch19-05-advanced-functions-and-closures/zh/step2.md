# 函数指针

我们已经讨论过如何将闭包传递给函数；你也可以将普通函数传递给函数！当你想要传递一个已经定义好的函数，而不是定义一个新的闭包时，这种技术很有用。函数会被强制转换为 `fn` 类型（小写的 `f`），不要与 `Fn` 闭包 trait 混淆。`fn` 类型被称为*函数指针*。使用函数指针传递函数将允许你把函数用作其他函数的参数。

指定一个参数为函数指针的语法与闭包的语法类似，如清单 19-27 所示，我们定义了一个函数 `add_one`，它将其参数加 1。函数 `do_twice` 有两个参数：一个指向任何接受 `i32` 参数并返回 `i32` 的函数的函数指针，以及一个 `i32` 值。`do_twice` 函数调用函数 `f` 两次，将 `arg` 值传递给它，然后将两个函数调用结果相加。`main` 函数使用参数 `add_one` 和 `5` 调用 `do_twice`。

文件名：`src/main.rs`

```rust
fn add_one(x: i32) -> i32 {
    x + 1
}

fn do_twice(f: fn(i32) -> i32, arg: i32) -> i32 {
    f(arg) + f(arg)
}

fn main() {
    let answer = do_twice(add_one, 5);

    println!("The answer is: {answer}");
}
```

清单 19-27：使用 `fn` 类型接受函数指针作为参数

这段代码打印出 `The answer is: 12`。我们指定 `do_twice` 中的参数 `f` 是一个 `fn`，它接受一个 `i32` 类型的参数并返回一个 `i32`。然后我们可以在 `do_twice` 的主体中调用 `f`。在 `main` 中，我们可以将函数名 `add_one` 作为第一个参数传递给 `do_twice`。

与闭包不同，`fn` 是一种类型而不是 trait，所以我们直接将 `fn` 指定为参数类型，而不是使用 `Fn` trait 之一作为 trait 约束来声明一个泛型类型参数。

函数指针实现了所有三个闭包 trait（`Fn`、`FnMut` 和 `FnOnce`），这意味着你总是可以将函数指针作为参数传递给期望闭包的函数。最好使用泛型类型和闭包 trait 之一来编写函数，这样你的函数就可以接受函数或闭包。

也就是说，你只想接受 `fn` 而不接受闭包的一个例子是，当与没有闭包的外部代码交互时：C 函数可以接受函数作为参数，但 C 没有闭包。

作为一个可以使用内联定义的闭包或命名函数的例子，让我们看看标准库中 `Iterator` trait 提供的 `map` 方法的用法。要使用 `map` 函数将一个数字向量转换为一个字符串向量，我们可以使用一个闭包，如下所示：

```rust
let list_of_numbers = vec![1, 2, 3];
let list_of_strings: Vec<String> = list_of_numbers
 .iter()
 .map(|i| i.to_string())
 .collect();
```

或者我们可以将一个命名函数作为 `map` 的参数，而不是闭包，如下所示：

```rust
let list_of_numbers = vec![1, 2, 3];
let list_of_strings: Vec<String> = list_of_numbers
 .iter()
 .map(ToString::to_string)
 .collect();
```

请注意，我们必须使用在“高级 trait”中讨论过的完全限定语法，因为有多个名为 `to_string` 的函数可用。

在这里，我们使用 `ToString` trait 中定义的 `to_string` 函数，标准库已经为任何实现 `Display` 的类型实现了该 trait。

从“枚举值”中回忆起，我们定义的每个枚举变体的名称也会成为一个初始化函数。我们可以将这些初始化函数用作实现闭包 trait 的函数指针，这意味着我们可以将初始化函数指定为接受闭包的方法的参数，如下所示：

```rust
enum Status {
    Value(u32),
    Stop,
}

let list_of_statuses: Vec<Status> = (0u32..20)
 .map(Status::Value)
 .collect();
```

在这里，我们通过使用 `Status::Value` 的初始化函数，为 `map` 调用的范围内的每个 `u32` 值创建 `Status::Value` 实例。有些人喜欢这种风格，有些人喜欢使用闭包。它们编译成相同的代码，所以使用对你来说更清晰的任何一种风格。
