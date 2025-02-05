# 使用 `pub` 关键字暴露路径

让我们回到清单 7-4 中的错误，它告诉我们 `hosting` 模块是私有的。我们希望父模块中的 `eat_at_restaurant` 函数能够访问子模块中的 `add_to_waitlist` 函数，所以我们用 `pub` 关键字标记 `hosting` 模块，如清单 7-5 所示。

文件名：`src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        fn add_to_waitlist() {}
    }
}

--snip--
```

清单 7-5：将 `hosting` 模块声明为 `pub` 以便从 `eat_at_restaurant` 中使用它

不幸的是，清单 7-5 中的代码仍然会导致编译器错误，如清单 7-6 所示。

```bash
$ cargo build
   Compiling restaurant v0.1.0 (file:///projects/restaurant)
error[E0603]: function `add_to_waitlist` is private
 --> src/lib.rs:9:37
  |
9 |     crate::front_of_house::hosting::add_to_waitlist();
  |                                     ^^^^^^^^^^^^^^^ private function
  |
note: the function `add_to_waitlist` is defined here
 --> src/lib.rs:3:9
  |
3 |         fn add_to_waitlist() {}
  |         ^^^^^^^^^^^^^^^^^^^^

error[E0603]: function `add_to_waitlist` is private
  --> src/lib.rs:12:30
   |
12 |     front_of_house::hosting::add_to_waitlist();
   |                              ^^^^^^^^^^^^^^^ private function
   |
note: the function `add_to_waitlist` is defined here
  --> src/lib.rs:3:9
   |
3  |         fn add_to_waitlist() {}
   |         ^^^^^^^^^^^^^^^^^^^^
```

清单 7-6：构建清单 7-5 中的代码时的编译器错误

发生了什么？在 `mod hosting` 前面添加 `pub` 关键字会使模块变为公共的。有了这个更改，如果我们可以访问 `front_of_house`，我们就可以访问 `hosting`。但是 `hosting` 的**内容**仍然是私有的；使模块变为公共的并不会使其内容也变为公共的。模块上的 `pub` 关键字只允许其祖先模块中的代码引用它，而不能访问其内部代码。因为模块是容器，仅使模块变为公共的我们能做的不多；我们需要进一步选择使模块内的一个或多个项也变为公共的。

清单 7-6 中的错误表明 `add_to_waitlist` 函数是私有的。隐私规则适用于结构体、枚举、函数、方法以及模块。

让我们也通过在 `add_to_waitlist` 函数定义之前添加 `pub` 关键字来使其变为公共的，如清单 7-7 所示。

文件名：`src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

--snip--
```

清单 7-7：在 `mod hosting` 和 `fn add_to_waitlist` 上添加 `pub` 关键字后，我们就可以从 `eat_at_restaurant` 中调用该函数了。

现在代码将编译通过！为了理解为什么添加 `pub` 关键字能让我们在 `add_to_waitlist` 中使用这些路径，让我们来看一下绝对路径和相对路径。

在绝对路径中，我们从 `crate` 开始，它是我们 crate 模块树的根。`front_of_house` 模块是在 crate 根中定义的。虽然 `front_of_house` 不是公共的，但由于 `eat_at_restaurant` 函数与 `front_of_house` 在同一个模块中定义（也就是说，`eat_at_restaurant` 和 `front_of_house` 是同级的），我们可以从 `eat_at_restaurant` 中引用 `front_of_house`。接下来是用 `pub` 标记的 `hosting` 模块。我们可以访问 `hosting` 的父模块，所以我们可以访问 `hosting`。最后，`add_to_waitlist` 函数用 `pub` 标记，我们可以访问它的父模块，所以这个函数调用是可行的！

在相对路径中，逻辑与绝对路径相同，只是第一步不同：路径不是从 crate 根开始，而是从 `front_of_house` 开始。`front_of_house` 模块是在与 `eat_at_restaurant` 同一个模块中定义的，所以从定义 `eat_at_restaurant` 的模块开始的相对路径是可行的。然后，因为 `hosting` 和 `add_to_waitlist` 用 `pub` 标记，路径的其余部分是可行的，这个函数调用是有效的！

如果你打算共享你的库 crate，以便其他项目可以使用你的代码，那么你的公共 API 就是你与 crate 用户的契约，它决定了他们如何与你的代码进行交互。围绕管理公共 API 的更改有很多需要考虑的因素，以便人们更容易依赖你的 crate。这些考虑超出了本书的范围；如果你对这个主题感兴趣，请查看 Rust API 指南：*https://rust-lang.github.io/api-guidelines*。

> **带有二进制文件和库的包的最佳实践**
>
> 我们提到过一个包可以同时包含 `src/main.rs` 二进制 crate 根和 `src/lib.rs` 库 crate 根，并且默认情况下两个 crate 都会有包名。通常，具有这种同时包含库和二进制 crate 模式的包，在二进制 crate 中只会有足够的代码来启动一个可执行文件，该可执行文件调用库 crate 中的代码。这使得其他项目能够从该包提供的最多功能中受益，因为库 crate 的代码可以被共享。
>
> 模块树应该在 `src/lib.rs` 中定义。然后，任何公共项都可以通过以包名开头的路径在二进制 crate 中使用。二进制 crate 就像一个完全外部的 crate 使用库 crate 一样，成为库 crate 的用户：它只能使用公共 API。这有助于你设计一个好的 API；你不仅是作者，也是客户端！
>
> 在第 12 章中，我们将通过一个包含二进制 crate 和库 crate 的命令行程序来演示这种组织实践。
