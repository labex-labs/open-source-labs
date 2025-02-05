# 所有权与函数

将一个值传递给函数的机制与将值赋给变量时的机制类似。将一个变量传递给函数时，它会被移动或复制，就像赋值时一样。清单 4-3 有一个示例，并带有一些注释，展示了变量何时进入和离开作用域。

    // src/main.rs
    fn main() {
        let s = String::from("hello");  // s 进入作用域

        takes_ownership(s);             // s 的值被移动到函数中……
                                        // …… 所以在这里它不再有效

        let x = 5;                      // x 进入作用域

        makes_copy(x);                  // x 会被移动到函数中，
                                        // 但 i32 实现了 Copy，所以之后仍然可以使用 x

    } // 在这里，x 离开作用域，然后是 s。然而，因为 s 的值被移动了，
      // 所以不会发生什么特别的事情

    fn takes_ownership(some_string: String) { // some_string 进入作用域
        println!("{some_string}");
    } // 在这里，some_string 离开作用域，并且调用 `drop`。底层
      // 内存被释放

    fn makes_copy(some_integer: i32) { // some_integer 进入作用域
        println!("{some_integer}");
    } // 在这里，some_integer 离开作用域。不会发生什么特别的事情

清单 4-3：带有所有权和作用域注释的函数

如果我们在调用 `takes_ownership` 之后尝试使用 `s`，Rust 会抛出一个编译时错误。这些静态检查可以保护我们避免犯错。尝试在 `main` 中添加使用 `s` 和 `x` 的代码，看看你可以在哪里使用它们，以及所有权规则在哪里会阻止你这样做。
