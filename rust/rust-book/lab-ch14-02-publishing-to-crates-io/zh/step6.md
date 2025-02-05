# 使用 `pub use` 导出便捷的公共 API

发布 crate 时，公共 API 的结构是一个主要考虑因素。使用你 crate 的人不像你那样熟悉其结构，如果你的 crate 有很大的模块层次结构，他们可能很难找到他们想要使用的部分。

在第7章中，我们介绍了如何使用 `pub` 关键字使项公开，以及如何使用 `use` 关键字将项引入作用域。然而，在开发 crate 时对你有意义的结构，对你的用户来说可能并不方便。你可能希望将结构体组织成包含多个层次的层次结构，但随后想要使用你在层次结构深处定义的类型的人可能很难发现该类型的存在。他们可能也会因必须输入 `use my_crate::some_module::another_module::UsefulType;` 而不是 `use my_crate::UsefulType;` 而感到恼火。

好消息是，如果该结构对其他库的使用者来说 **不方便** 使用，你不必重新安排内部组织：相反，你可以使用 `pub use` 重新导出项，以创建一个与私有结构不同的公共结构。**重新导出** 会在一个位置获取一个公共项，并在另一个位置使其公开，就好像它是在另一个位置定义的一样。

例如，假设我们创建了一个名为 `art` 的库来对艺术概念进行建模。在这个库中有两个模块：一个 `kinds` 模块，包含两个名为 `PrimaryColor` 和 `SecondaryColor` 的枚举；以及一个 `utils` 模块，包含一个名为 `mix` 的函数，如清单14-3所示。

文件名：`src/lib.rs`

```rust
//! # 艺术
//!
//! 一个用于对艺术概念进行建模的库。

pub mod kinds {
    /// 根据 RYB 颜色模型的原色。
    pub enum PrimaryColor {
        Red,
        Yellow,
        Blue,
    }

    /// 根据 RYB 颜色模型的间色。
    pub enum SecondaryColor {
        Orange,
        Green,
        Purple,
    }
}

pub mod utils {
    use crate::kinds::*;

    /// 将两种等量的原色混合以创建一种间色。
    pub fn mix(
        c1: PrimaryColor,
        c2: PrimaryColor,
    ) -> SecondaryColor {
        --snip--
    }
}
```

清单14-3：一个将项组织到 `kinds` 和 `utils` 模块中的 `art` 库

图14-3展示了由 `cargo doc` 生成的此 crate 文档的首页样子。

图14-3：列出 `kinds` 和 `utils` 模块的 `art` 文档首页

请注意，`PrimaryColor` 和 `SecondaryColor` 类型以及 `mix` 函数都没有列在首页上。我们必须点击 `kinds` 和 `utils` 才能看到它们。

另一个依赖此库的 crate 需要使用 `use` 语句将 `art` 中的项引入作用域，并指定当前定义的模块结构。清单14-4展示了一个使用 `art` crate 中的 `PrimaryColor` 和 `mix` 项的 crate 示例。

文件名：`src/main.rs`

```rust
use art::kinds::PrimaryColor;
use art::utils::mix;

fn main() {
    let red = PrimaryColor::Red;
    let yellow = PrimaryColor::Yellow;
    mix(red, yellow);
}
```

清单14-4：一个使用 `art` crate 内部结构导出的项的 crate

清单14-4中使用 `art` crate 的代码作者必须弄清楚 `PrimaryColor` 在 `kinds` 模块中，而 `mix` 在 `utils` 模块中。`art` crate 的模块结构对在 `art` crate 上工作的开发者来说比使用它的人更相关。内部结构对于试图理解如何使用 `art` crate 的人来说没有任何有用信息，反而会造成困惑，因为使用它的开发者必须弄清楚在哪里查找，并且必须在 `use` 语句中指定模块名称。

为了从公共 API 中去除内部组织，我们可以修改清单14-3中的 `art` crate 代码，添加 `pub use` 语句以在顶层重新导出项，如清单14-5所示。

文件名：`src/lib.rs`

```rust
//! # 艺术
//!
//! 一个用于对艺术概念进行建模的库。

pub use self::kinds::PrimaryColor;
pub use self::kinds::SecondaryColor;
pub use self::utils::mix;

pub mod kinds {
    --snip--
}

pub mod utils {
    --snip--
}
```

清单14-5：添加 `pub use` 语句以重新导出项

现在，`cargo doc` 为此 crate 生成的 API 文档将在首页列出并链接重新导出的项，如图14-4所示，这使得 `PrimaryColor` 和 `SecondaryColor` 类型以及 `mix` 函数更容易找到。

图14-4：列出重新导出项的 `art` 文档首页

`art` crate 的用户仍然可以像清单14-4中那样看到并使用清单14-3中的内部结构，或者他们也可以使用清单14-5中更方便的结构，如清单14-6所示。

文件名：`src/main.rs`

```rust
use art::mix;
use art::PrimaryColor;

fn main() {
    --snip--
}
```

清单14-6：一个使用 `art` crate 重新导出项的程序

在有许多嵌套模块的情况下，使用 `pub use` 在顶层重新导出类型会对使用该 crate 的人的体验产生显著影响。`pub use` 的另一个常见用途是在当前 crate 中重新导出依赖项的定义，以使该 crate 的定义成为你 crate 公共 API 的一部分。

创建一个有用的公共 API 结构更多的是一门艺术而非科学，你可以反复尝试以找到最适合你用户的 API。选择 `pub use` 会让你在内部构建 crate 的方式上具有灵活性，并将内部结构与呈现给用户的结构解耦。看看你安装的一些 crate 的代码，看看它们的内部结构是否与公共 API 不同。
