# 悬垂引用

在有指针的语言中，很容易错误地创建一个悬垂指针（dangling pointer）——一个指向可能已被分配给其他人的内存位置的指针，方法是在保留指向该内存的指针的同时释放一些内存。相比之下，在 Rust 中，编译器会确保引用永远不会是悬垂引用：如果你有一个指向某些数据的引用，编译器会确保在对该数据的引用超出作用域之前，该数据不会超出作用域。

让我们尝试创建一个悬垂引用，看看 Rust 如何通过编译时错误来防止它们：

文件名：`src/main.rs`

```rust
fn main() {
    let reference_to_nothing = dangle();
}

fn dangle() -> &String {
    let s = String::from("hello");

    &s
}
```

这里是错误信息：

```bash
error[E0106]: missing lifetime specifier
 --> src/main.rs:5:16
  |
5 | fn dangle() -> &String {
  |                ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value,
but there is no value for it to be borrowed from
help: consider using the `'static` lifetime
  |
5 | fn dangle() -> &'static String {
  |                ~~~~~~~~
```

这个错误信息提到了一个我们还没有涉及的特性：生命周期。我们将在第 10 章详细讨论生命周期。但是，如果你忽略关于生命周期的部分，这个信息确实包含了为什么这段代码有问题的关键：

```rust
this function's return type contains a borrowed value, but there
is no value for it to be borrowed from
```

让我们仔细看看在 `dangle` 代码的每个阶段到底发生了什么：

    // src/main.rs
    fn dangle() -> &String { // dangle 返回一个指向 String 的引用

        let s = String::from("hello"); // s 是一个新的 String

        &s // 我们返回对 String，即 s 的引用
    } // 在这里，s 超出作用域并被释放，所以它的内存也消失了
      // 危险！

因为 `s` 是在 `dangle` 内部创建的，当 `dangle` 的代码结束时，`s` 将被释放。但我们试图返回一个指向它的引用。这意味着这个引用将指向一个无效的 `String`。这可不行！Rust 不会让我们这样做。

这里的解决方案是直接返回 `String`：

```rust
fn no_dangle() -> String {
    let s = String::from("hello");

    s
}
```

这样就可以正常工作，不会有任何问题。所有权被转移出去，并且没有任何东西被释放。
