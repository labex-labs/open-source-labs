# 测试用例：List

为一个其元素必须按顺序逐个处理的结构体实现 `fmt::Display` 特性是很棘手的。问题在于每个 `write!` 都会生成一个 `fmt::Result`。要正确处理这个问题，就需要处理所有的结果。Rust 为此提供了 `?` 运算符。

在 `write!` 上使用 `?` 看起来是这样的：

```rust
// 尝试使用 `write!` 看看是否出错。如果出错，返回
// 错误。否则继续。
write!(f, "{}", value)?;
```

有了 `?` 之后，为 `Vec` 实现 `fmt::Display` 就很简单了：

```rust
use std::fmt; // 导入 `fmt` 模块。

// 定义一个名为 `List` 的结构体，它包含一个 `Vec`。
struct List(Vec<i32>);

impl fmt::Display for List {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // 使用元组索引提取值，
        // 并创建一个指向 `vec` 的引用。
        let vec = &self.0;

        write!(f, "[")?;

        // 遍历 `vec` 中的 `v`，同时枚举迭代计数 `count`。
        for (count, v) in vec.iter().enumerate() {
            // 对于除第一个元素之外的每个元素，添加一个逗号。
            // 使用 `?` 运算符在出错时返回。
            if count!= 0 { write!(f, ", ")?; }
            write!(f, "{}", v)?;
        }

        // 关闭打开的方括号并返回一个 `fmt::Result` 值。
        write!(f, "]")
    }
}

fn main() {
    let v = List(vec![1, 2, 3]);
    println!("{}", v);
}
```

## 活动

尝试修改程序，使其还能打印向量中每个元素的索引。新的输出应该是这样的：

```rust
[0: 1, 1: 2, 2: 3]
```
