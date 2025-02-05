# 使用 `as` 关键字提供新名称

对于使用 `use` 将两个同名类型引入同一作用域的问题，还有另一种解决方案：在路径之后，我们可以指定 `as` 和该类型的一个新的本地名称，即 _别名_。清单 7-16 展示了通过使用 `as` 重命名两个 `Result` 类型之一，来编写清单 7-15 中的代码的另一种方式。

文件名：`src/lib.rs`

```rust
use std::fmt::Result;
use std::io::Result as IoResult;

fn function1() -> Result {
    --snip--
}

fn function2() -> IoResult<()> {
    --snip--
}
```

清单 7-16：使用 `as` 关键字将类型引入作用域时对其进行重命名

在第二条 `use` 语句中，我们为 `std::io::Result` 类型选择了新名称 `IoResult`，它不会与我们也引入到作用域中的 `std::fmt` 中的 `Result` 冲突。清单 7-15 和清单 7-16 都被认为是符合习惯用法的，所以选择权在你！
