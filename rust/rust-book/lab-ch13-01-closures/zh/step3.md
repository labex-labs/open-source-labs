# 闭包类型推断与标注

函数和闭包之间还有更多区别。闭包通常不像 `fn` 函数那样要求你标注参数和返回值的类型。函数需要进行类型标注，因为类型是暴露给用户的显式接口的一部分。严格定义这个接口对于确保每个人都就函数使用和返回的数值类型达成一致很重要。另一方面，闭包并不用于这样的公开接口：它们存储在变量中，使用时无需命名并暴露给库的用户。

闭包通常很短，并且只在有限的上下文中相关，而不是在任何任意场景中。在这些有限的上下文中，编译器可以推断参数的类型和返回类型，类似于它能够推断大多数变量的类型（在极少数情况下，编译器也需要闭包类型标注）。

与变量一样，如果我们想以比严格必要时更冗长为代价来增加显式性和清晰度，就可以添加类型标注。为闭包标注类型看起来会像清单 13-2 中所示的定义。在这个例子中，我们定义一个闭包并将其存储在变量中，而不是像在清单 13-1 中那样在作为参数传递闭包的地方定义它。

文件名：`src/main.rs`

```rust
let expensive_closure = |num: u32| -> u32 {
    println!("calculating slowly...");
    thread::sleep(Duration::from_secs(2));
    num
};
```

清单 13-2：在闭包中添加参数和返回值类型的可选类型标注

添加类型标注后，闭包的语法看起来更类似于函数的语法。这里，为了进行比较，我们定义了一个将其参数加 1 的函数和一个具有相同行为的闭包。我们添加了一些空格以使相关部分对齐。这说明了闭包语法与函数语法的相似之处，除了使用管道以及可选语法的数量：

```rust
fn  add_one_v1   (x: u32) -> u32 { x + 1 }
let add_one_v2 = |x: u32| -> u32 { x + 1 };
let add_one_v3 = |x|             { x + 1 };
let add_one_v4 = |x|               x + 1  ;
```

第一行展示了一个函数定义，第二行展示了一个完全标注的闭包定义。在第三行，我们从闭包定义中移除了类型标注。在第四行，我们移除了花括号，因为闭包体只有一个表达式，所以花括号是可选的。这些都是有效的定义，调用时会产生相同的行为。`add_one_v3` 和 `add_one_v4` 这两行要求闭包被求值才能编译，因为类型将从它们的使用中推断出来。这类似于 `let v = Vec::new();` 需要类型标注或者向 `Vec` 中插入某种类型的值，Rust 才能推断出类型。

对于闭包定义，编译器会为其每个参数和返回值推断出一个具体类型。例如，清单 13-3 展示了一个简短闭包的定义，它只返回作为参数接收的值。除了这个例子的目的外，这个闭包不是很有用。注意我们在定义中没有添加任何类型标注。因为没有类型标注，我们可以用任何类型调用这个闭包，这里我们第一次用 `String` 调用。如果我们随后尝试用整数调用 `example_closure`，就会得到一个错误。

文件名：`src/main.rs`

```rust
let example_closure = |x| x;

let s = example_closure(String::from("hello"));
let n = example_closure(5);
```

清单 13-3：尝试用两种不同类型调用类型被推断的闭包

编译器给我们这个错误：

```bash
error[E0308]: mismatched types
 --> src/main.rs:5:29
  |
5 |     let n = example_closure(5);
  |                             ^- help: try using a conversion method:
`.to_string()`
  |                             |
  |                             expected struct `String`, found integer
```

我们第一次用 `String` 值调用 `example_closure` 时，编译器推断出 `x` 的类型和闭包的返回类型为 `String`。然后这些类型被锁定在 `example_closure` 中的闭包中，当我们下次尝试用不同类型与同一个闭包一起使用时，就会得到一个类型错误。
