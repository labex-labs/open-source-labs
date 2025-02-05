# `From` 和 `Into`

[`From`](#from) 和 [`Into`](#into) 特征本质上是相互关联的，这实际上是其实现的一部分。如果你能够将类型 A 从类型 B 转换而来，那么很容易想到我们也应该能够将类型 B 转换为类型 A。

## `From`

[`From`](#from) 特征允许一个类型定义如何从另一个类型创建自身，从而为几种类型之间的转换提供了一种非常简单的机制。标准库中有许多针对基本类型和常见类型转换的此特征的实现。

例如，我们可以轻松地将 `str` 转换为 `String`

```rust
let my_str = "hello";
let my_string = String::from(my_str);
```

我们也可以为自己的类型定义类似的转换。

```rust
use std::convert::From;

#[derive(Debug)]
struct Number {
    value: i32,
}

impl From<i32> for Number {
    fn from(item: i32) -> Self {
        Number { value: item }
    }
}

fn main() {
    let num = Number::from(30);
    println!("My number is {:?}", num);
}
```

## `Into`

[`Into`](#into) 特征仅仅是 `From` 特征的反向。也就是说，如果你已经为你的类型实现了 `From` 特征，`Into` 将在必要时调用它。

使用 `Into` 特征通常需要指定要转换为的类型，因为编译器大多数时候无法确定这一点。然而，考虑到我们免费获得了该功能，这只是一个小的权衡。

```rust
use std::convert::Into;

#[derive(Debug)]
struct Number {
    value: i32,
}

impl Into<Number> for i32 {
    fn into(self) -> Number {
        Number { value: self }
    }
}

fn main() {
    let int = 5;
    // 尝试移除类型标注
    let num: Number = int.into();
    println!("My number is {:?}", num);
}
```
