# 字符串切片

字符串切片是对 `String` 一部分的引用，它看起来像这样：

```rust
let s = String::from("hello world");

let hello = &s[0..5];
let world = &s[6..11];
```

`hello` 不是对整个 `String` 的引用，而是对 `String` 一部分的引用，由额外的 `[0..5]` 部分指定。我们通过在方括号内指定一个范围 `[起始索引..结束索引]` 来创建切片，其中 `起始索引` 是切片中的第一个位置，`结束索引` 比切片中的最后一个位置大1。在内部，切片数据结构存储起始位置和切片的长度，这对应于 `结束索引` 减去 `起始索引`。所以，对于 `let world = &s[6..11];`，`world` 将是一个切片，它包含一个指向 `s` 中索引6处字节的指针，长度值为 `5`。

图4-6用图表展示了这一点。

图4-6：指向 `String` 一部分的字符串切片

使用 Rust 的 `..` 范围语法，如果你想从索引0开始，可以省略两个点之前的值。换句话说，这些是等效的：

```rust
let s = String::from("hello");

let slice = &s[0..2];
let slice = &s[..2];
```

同样，如果你的切片包含 `String` 的最后一个字节，可以省略尾随数字。这意味着这些是等效的：

```rust
let s = String::from("hello");

let len = s.len();

let slice = &s[3..len];
let slice = &s[3..];
```

你也可以省略两个值以获取整个字符串的切片。所以这些是等效的：

```rust
let s = String::from("hello");

let len = s.len();

let slice = &s[0..len];
let slice = &s[..];
```

> 注意：字符串切片范围索引必须出现在有效的 UTF-8 字符边界处。如果你试图在多字节字符中间创建字符串切片，你的程序将以错误退出。为了介绍字符串切片，在本节中我们假设只使用 ASCII；关于 UTF-8 处理的更全面讨论在“使用字符串存储 UTF-8 编码的文本”中。

记住所有这些信息后，让我们重写 `first_word` 以返回一个切片。表示“字符串切片”的类型写作 `&str`：

文件名：`src/main.rs`

```rust
fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}
```

我们通过查找第一个出现的空格来获取单词结束的索引，方式与清单4-7中相同。当我们找到一个空格时，我们使用字符串的起始位置和空格的索引作为起始和结束索引来返回一个字符串切片。

现在当我们调用 `first_word` 时，我们得到一个与底层数据相关联的单一值。该值由切片起始点的引用和切片中的元素数量组成。

返回一个切片对于 `second_word` 函数也适用：

```rust
fn second_word(s: &String) -> &str {
```

我们现在有了一个简单直接的 API，更难出错，因为编译器会确保对 `String` 的引用保持有效。还记得清单4-8中的程序中的错误吗？当时我们得到了第一个单词结束的索引，但随后清空了字符串，所以我们的索引变得无效。那段代码在逻辑上是不正确的，但没有立即显示任何错误。如果我们继续尝试对一个已清空的字符串使用第一个单词的索引，问题会在后面出现。切片使这个错误不可能发生，并让我们更早地知道代码有问题。使用 `first_word` 的切片版本会抛出一个编译时错误：

文件名：`src/main.rs`

```rust
fn main() {
    let mut s = String::from("hello world");

    let word = first_word(&s);

    s.clear(); // 错误！

    println!("the first word is: {word}");
}
```

这是编译器错误：

```bash
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as
immutable
  --> src/main.rs:18:5
   |
16 |     let word = first_word(&s);
   |                           -- immutable borrow occurs here
17 |
18 |     s.clear(); // error!
   |     ^^^^^^^^^ mutable borrow occurs here
19 |
20 |     println!("the first word is: {word}");
   |                                   ---- immutable borrow later used here
```

回顾借用规则，如果我们对某个东西有一个不可变引用，我们就不能再获取一个可变引用。因为 `clear` 需要截断 `String`，它需要获取一个可变引用。对 `clear` 的调用之后的 `println!` 使用了 `word` 中的引用，所以在那个时候不可变引用必须仍然有效。Rust 不允许 `clear` 中的可变引用和 `word` 中的不可变引用同时存在，编译失败。Rust 不仅使我们的 API 更易于使用，还在编译时消除了一整类错误！
