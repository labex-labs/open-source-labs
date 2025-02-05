# 函数签名中的生命周期标注

要在函数签名中使用生命周期标注，我们需要在函数名和参数列表之间的尖括号内声明泛型**生命周期**参数，就像我们对泛型**类型**参数所做的那样。

我们希望签名表达以下约束：只要两个参数都有效，返回的引用就将有效。这就是参数的生命周期与返回值之间的关系。我们将生命周期命名为 `'a`，然后将其添加到每个引用中，如清单 10-21 所示。

文件名：`src/main.rs`

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

清单 10-21：`longest` 函数定义，指定签名中的所有引用都必须具有相同的生命周期 `'a`

当我们将此代码与清单 10-19 中的 `main` 函数一起使用时，这段代码应该能够编译并产生我们想要的结果。

现在，函数签名告诉 Rust，对于某个生命周期 `'a`，该函数接受两个参数，这两个参数都是字符串切片，它们的存活时间至少与生命周期 `'a` 一样长。函数签名还告诉 Rust，从函数返回的字符串切片的存活时间至少与生命周期 `'a` 一样长。实际上，这意味着 `longest` 函数返回的引用的生命周期与函数参数所引用的值的生命周期中较小的那个相同。这些关系就是我们希望 Rust 在分析这段代码时使用的。

请记住，当我们在这个函数签名中指定生命周期参数时，我们并没有改变传入或返回的任何值的生命周期。相反，我们是在指定借用检查器应该拒绝任何不符合这些约束的值。请注意，`longest` 函数不需要确切知道 `x` 和 `y` 会存活多长时间，只需要知道可以用某个作用域来替换 `'a`，并且这个作用域能够满足这个签名。

在函数中注释生命周期时，注释要放在函数签名中，而不是函数体中。生命周期注释成为函数契约的一部分，就像签名中的类型一样。让函数签名包含生命周期契约意味着 Rust 编译器所做的分析可以更简单。如果函数的注释方式或调用方式有问题，编译器错误可以更精确地指向我们代码的部分以及约束条件。相反，如果 Rust 编译器对我们期望的生命周期关系进行更多推断，编译器可能只能指向离问题原因很远的代码使用处。

当我们将具体引用传递给 `longest` 时，替换 `'a` 的具体生命周期是 `x` 的作用域与 `y` 的作用域重叠的部分。换句话说，泛型生命周期 `'a` 将获得等于 `x` 和 `y` 的生命周期中较小者的具体生命周期。因为我们用相同的生命周期参数 `'a` 注释了返回的引用，所以返回的引用在 `x` 和 `y` 的生命周期中较小者的时长内也将是有效的。

让我们看看生命周期注释如何通过传入具有不同具体生命周期的引用限制 `longest` 函数。清单 10-22 是一个简单的示例。

文件名：`src/main.rs`

```rust
fn main() {
    let string1 = String::from("long string is long");

    {
        let string2 = String::from("xyz");
        let result = longest(string1.as_str(), string2.as_str());
        println!("The longest string is {result}");
    }
}
```

清单 10-22：对具有不同具体生命周期的 `String` 值的引用使用 `longest` 函数

在这个示例中，`string1` 在外层作用域结束之前都是有效的，`string2` 在内层作用域结束之前都是有效的，而 `result` 引用的内容在内层作用域结束之前都是有效的。运行这段代码，你会看到借用检查器通过了；它将编译并打印出 `The longest string is long string is long`。

接下来，让我们尝试一个示例，展示 `result` 中的引用的生命周期必须是两个参数中较小的那个生命周期。我们将把 `result` 变量的声明移到内层作用域之外，但将其值的赋值留在包含 `string2` 的作用域内。然后我们将使用 `result` 的 `println!` 移到内层作用域结束之后的外层作用域之外。清单 10-23 中的代码将无法编译。

文件名：`src/main.rs`

```rust
fn main() {
    let string1 = String::from("long string is long");
    let result;
    {
        let string2 = String::from("xyz");
        result = longest(string1.as_str(), string2.as_str());
    }
    println!("The longest string is {result}");
}
```

清单 10-23：在 `string2` 超出作用域后尝试使用 `result`

当我们尝试编译这段代码时，会得到以下错误：

```bash
error[E0597]: `string2` does not live long enough
 --> src/main.rs:6:44
  |
6 |         result = longest(string1.as_str(), string2.as_str());
  |                                            ^^^^^^^^^^^^^^^^ borrowed value
does not live long enough
7 |     }
  |     - `string2` dropped here while still borrowed
8 |     println!("The longest string is {result}");
  |                                      ------ borrow later used here
```

错误表明，为了使 `result` 对于 `println!` 语句有效，`string2` 需要在外层作用域结束之前都有效。Rust 知道这一点，因为我们使用相同的生命周期参数 `'a` 注释了函数参数和返回值的生命周期。

作为人类，我们可以查看这段代码并看到 `string1` 比 `string2` 长，因此，`result` 将包含对 `string1` 的引用。因为 `string1` 尚未超出作用域，所以对 `string1` 的引用对于 `println!` 语句仍然有效。然而，编译器在这种情况下无法看出该引用是有效的。我们已经告诉 Rust，`longest` 函数返回的引用的生命周期与传入的引用的生命周期中较小的那个相同。因此，借用检查器不允许清单 10-23 中的代码，因为它可能有一个无效的引用。

尝试设计更多实验，改变传递给 `longest` 函数的引用的值和生命周期，以及返回的引用的使用方式。在编译之前，先假设你的实验是否会通过借用检查器；然后检查看看你是否正确！
