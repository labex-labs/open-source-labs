# 创建符合习惯用法的 `use` 路径

在清单 7-11 中，你可能想知道为什么我们指定了 `use crate::front_of_house::hosting`，然后在 `eat_at_restaurant` 中调用 `hosting::add_to_waitlist`，而不是像清单 7-13 那样一直将 `use` 路径指定到 `add_to_waitlist` 函数以达到相同的效果。

文件名：`src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting::add_to_waitlist;

pub fn eat_at_restaurant() {
    add_to_waitlist();
}
```

清单 7-13：使用 `use` 将 `add_to_waitlist` 函数引入作用域，这不符合习惯用法

虽然清单 7-11 和清单 7-13 都完成了相同的任务，但清单 7-11 是使用 `use` 将函数引入作用域的符合习惯用法的方式。使用 `use` 将函数的父模块引入作用域意味着我们在调用函数时必须指定父模块。在调用函数时指定父模块，既表明该函数不是在本地定义的，又能最大程度地减少完整路径的重复。清单 7-13 中的代码不清楚 `add_to_waitlist` 是在哪里定义的。

另一方面，当使用 `use` 引入结构体、枚举和其他项时，指定完整路径是符合习惯用法的。清单 7-14 展示了将标准库的 `HashMap` 结构体引入二进制 crate 作用域的符合习惯用法的方式。

文件名：`src/main.rs`

```rust
use std::collections::HashMap;

fn main() {
    let mut map = HashMap::new();
    map.insert(1, 2);
}
```

清单 7-14：以符合习惯用法的方式将 `HashMap` 引入作用域

这种习惯用法背后并没有什么特别强烈的原因：这只是逐渐形成的一种约定，大家也都习惯了以这种方式阅读和编写 Rust 代码。

这种习惯用法的一个例外情况是，如果我们使用 `use` 语句将两个同名的项引入作用域，因为 Rust 不允许这样做。清单 7-15 展示了如何将两个同名但父模块不同的 `Result` 类型引入作用域，以及如何引用它们。

文件名：`src/lib.rs`

```rust
use std::fmt;
use std::io;

fn function1() -> fmt::Result {
    --snip--
}

fn function2() -> io::Result<()> {
    --snip--
}
```

清单 7-15：将两个同名类型引入同一作用域时需要使用它们的父模块

如你所见，使用父模块可以区分这两个 `Result` 类型。如果我们改为指定 `use std::fmt::Result` 和 `use std::io::Result`，那么在同一作用域中就会有两个 `Result` 类型，当我们使用 `Result` 时，Rust 将不知道我们指的是哪一个。
