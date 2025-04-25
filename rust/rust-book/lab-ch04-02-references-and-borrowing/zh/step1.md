# 引用与借用

清单 4-5 中的元组代码存在的问题是，我们必须将 `String` 返回给调用函数，这样在调用 `calculate_length` 之后我们仍然可以使用该 `String`，因为 `String` 被移动到了 `calculate_length` 中。相反，我们可以提供对 `String` 值的引用。引用类似于指针，它是一个地址，我们可以通过它来访问存储在该地址的数据；该数据由其他某个变量拥有。与指针不同的是，在引用的生命周期内，引用保证指向特定类型的有效值。

下面是如何定义和使用一个 `calculate_length` 函数，该函数将对象的引用作为参数，而不是获取值的所有权：

文件名：`src/main.rs`

```rust
fn main() {
    let s1 = String::from("hello");

    let len = calculate_length(&s1);

    println!("The length of '{s1}' is {len}.");
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

首先，注意变量声明和函数返回值中的所有元组代码都不见了。其次，注意我们将 `&s1` 传递给 `calculate_length`，并且在其定义中，我们使用 `&String` 而不是 `String`。这些 `&` 符号表示引用，它们允许你引用某个值而不获取其所有权。图 4-5 展示了这个概念。

图 4-5：`&String s` 指向 `String s1` 的示意图

> 注意：使用 `&` 进行引用的相反操作是解引用，它是通过解引用运算符 `*` 来完成的。我们将在第 8 章中看到解引用运算符的一些用法，并在第 15 章中讨论解引用的细节。

让我们仔细看看这里的函数调用：

```rust
let s1 = String::from("hello");

let len = calculate_length(&s1);
```

`&s1` 语法让我们创建一个引用，该引用指向 `s1` 的值，但不拥有它。因为它不拥有该值，所以当引用不再使用时，它所指向的值不会被释放。

同样，函数的签名使用 `&` 来表明参数 `s` 的类型是一个引用。让我们添加一些解释性注释：

```rust
fn calculate_length(s: &String) -> usize { // s 是对 String 的引用
    s.len()
} // 这里，s 超出了作用域。但因为它不拥有它所指向的内容，
  // 所以 String 不会被释放
```

变量 `s` 有效的作用域与任何函数参数的作用域相同，但是当 `s` 不再使用时，引用所指向的值不会被释放，因为 `s` 不拥有所有权。当函数使用引用作为参数而不是实际值时，我们不需要返回值来归还所有权，因为我们从未拥有过所有权。

我们将创建引用的行为称为借用。就像在现实生活中一样，如果一个人拥有某样东西，你可以向他们借用。当你用完后，你必须归还。你并不拥有它。

那么，如果我们试图修改我们正在借用的东西会发生什么呢？试试清单 4-6 中的代码。剧透警告：它不起作用！

文件名：`src/main.rs`

```rust
fn main() {
    let s = String::from("hello");

    change(&s);
}

fn change(some_string: &String) {
    some_string.push_str(", world");
}
```

清单 4-6：尝试修改借用的值

这里是错误信息：

```bash
error[E0596]: cannot borrow `*some_string` as mutable, as it is behind a `&`
reference
 --> src/main.rs:8:5
  |
7 | fn change(some_string: &String) {
  |                        ------- help: consider changing this to be a mutable
reference: `&mut String`
8 |     some_string.push_str(", world");
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ `some_string` is a `&` reference, so
the data it refers to cannot be borrowed as mutable
```

就像变量默认是不可变的一样，引用也是如此。我们不允许修改我们拥有引用的东西。
