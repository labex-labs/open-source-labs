# 使用 `use` 关键字将路径引入作用域

每次都要完整写出调用函数的路径会让人觉得很不方便且重复。在清单 7-7 中，无论我们选择的是到 `add_to_waitlist` 函数的绝对路径还是相对路径，每次想要调用 `add_to_waitlist` 时，都必须同时指定 `front_of_house` 和 `hosting`。幸运的是，有一种方法可以简化这个过程：我们可以使用 `use` 关键字为路径创建一个快捷方式，这样在作用域的其他地方就可以使用更短的名称。

在清单 7-11 中，我们将 `crate::front_of_house::hosting` 模块引入到 `eat_at_restaurant` 函数的作用域中，这样在 `eat_at_restaurant` 中调用 `add_to_waitlist` 函数时，只需要指定 `hosting::add_to_waitlist` 即可。

文件名：`src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

清单 7-11：使用 `use` 将模块引入作用域

在作用域中添加 `use` 和一个路径类似于在文件系统中创建一个符号链接。通过在 crate 根目录中添加 `use crate::front_of_house::hosting`，`hosting` 现在在该作用域中是一个有效的名称，就好像 `hosting` 模块是在 crate 根目录中定义的一样。使用 `use` 引入作用域的路径也会像其他任何路径一样检查隐私性。

请注意，`use` 仅为 `use` 所在的特定作用域创建快捷方式。清单 7-12 将 `eat_at_restaurant` 函数移动到一个名为 `customer` 的新子模块中，该子模块与 `use` 语句所在的作用域不同，因此函数体将无法编译。

文件名：`src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

mod customer {
    pub fn eat_at_restaurant() {
        hosting::add_to_waitlist();
    }
}
```

清单 7-12：`use` 语句仅在其所在的作用域内适用

编译器错误表明，在 `customer` 模块中，快捷方式不再适用：

```bash
error[E0433]: failed to resolve: use of undeclared crate or module `hosting`
  --> src/lib.rs:11:9
   |
11 |         hosting::add_to_waitlist();
   |         ^^^^^^^ use of undeclared crate or module `hosting`

warning: unused import: `crate::front_of_house::hosting`
 --> src/lib.rs:7:5
  |
7 | use crate::front_of_house::hosting;
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  |
  = note: `#[warn(unused_imports)]` on by default
```

请注意，还有一个警告，表明 `use` 在其作用域中不再被使用！要解决这个问题，可以将 `use` 也移动到 `customer` 模块中，或者在子模块 `customer` 中使用 `super::hosting` 来引用父模块中的快捷方式。
