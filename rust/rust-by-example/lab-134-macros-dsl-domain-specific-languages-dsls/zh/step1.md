# 领域特定语言（DSL）

DSL 是一种嵌入在 Rust 宏中的小型“语言”。它完全是有效的 Rust 代码，因为宏系统会扩展为普通的 Rust 结构，但它看起来像一种小型语言。这使你能够为某些特殊功能（在一定范围内）定义简洁或直观的语法。

假设我想定义一个小型计算器 API。我希望提供一个表达式，并将输出打印到控制台。

```rust
macro_rules! calculate {
    (eval $e:expr) => {
        {
            let val: usize = $e; // 强制类型为整数
            println!("{} = {}", stringify!{$e}, val);
        }
    };
}

fn main() {
    calculate! {
        eval 1 + 2 // 嘿嘿，`eval` 不是 Rust 关键字！
    }

    calculate! {
        eval (1 + 2) * (3 / 4)
    }
}
```

输出：

```txt
1 + 2 = 3
(1 + 2) * (3 / 4) = 0
```

这是一个非常简单的示例。

另外，请注意宏中的两对花括号。除了 `()` 或 `[]` 之外，外部的花括号是 `macro_rules!` 语法的一部分。
