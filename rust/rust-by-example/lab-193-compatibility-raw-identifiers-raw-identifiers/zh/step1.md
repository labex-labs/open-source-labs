# 原始标识符

和许多编程语言一样，Rust 也有 “关键字” 的概念。这些标识符对语言来说有特定含义，所以你不能在变量名、函数名等地方使用它们。原始标识符允许你在通常不允许使用关键字的地方使用关键字。当 Rust 引入新关键字，而使用旧版本 Rust 的库中有一个变量或函数与新版本中引入的关键字同名时，这一点特别有用。

例如，考虑一个用 2015 版 Rust 编译的名为 `foo` 的包，它导出了一个名为 `try` 的函数。这个关键字在 2018 版中被用于一个新特性，所以如果没有原始标识符，我们就无法给这个函数命名。

```rust
extern crate foo;

fn main() {
    foo::try();
}
```

你会得到如下错误：

```plaintext
error: expected identifier, found keyword `try`
 --> src/main.rs:4:4
  |
4 | foo::try();
  |      ^^^ expected identifier, found keyword
```

你可以使用原始标识符来这样写：

```rust
extern crate foo;

fn main() {
    foo::r#try();
}
```
