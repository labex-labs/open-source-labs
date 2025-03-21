# 宏与函数的区别

从根本上讲，宏是一种编写代码的方式，它可以编写其他代码，这被称为**元编程**。在附录 C 中，我们讨论了 `derive` 属性，它会为你生成各种 trait 的实现。在本书中，我们还使用了 `println!` 和 `vec!` 宏。所有这些宏都会**展开**，生成比你手动编写的代码更多的代码。

元编程有助于减少你需要编写和维护的代码量，这也是函数的作用之一。然而，宏具有一些函数所没有的额外功能。

函数签名必须声明函数所具有的参数数量和类型。另一方面，宏可以接受可变数量的参数：我们可以使用一个参数调用 `println!("hello")`，或者使用两个参数调用 `println!("hello {}", name)`。此外，宏在编译器解释代码含义之前就会展开，因此例如，宏可以在给定类型上实现一个 trait。函数则不能，因为它是在运行时被调用的，而 trait 需要在编译时实现。

使用宏而不是函数的缺点是，宏定义比函数定义更复杂，因为你编写的是生成 Rust 代码的 Rust 代码。由于这种间接性，宏定义通常比函数定义更难阅读、理解和维护。

宏和函数之间的另一个重要区别是，在文件中调用宏之前，你必须先定义宏或将其引入作用域，这与函数不同，函数可以在任何地方定义并在任何地方调用。
