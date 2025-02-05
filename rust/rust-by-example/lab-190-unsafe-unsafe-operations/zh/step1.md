# 不安全操作

作为本节的引言，引用官方文档的说法，“应该尽量减少代码库中不安全代码的数量”。牢记这一点，让我们开始吧！Rust中的不安全注释用于绕过编译器设置的保护；具体来说，不安全主要用于以下四件事：

- 解引用原始指针
- 调用 `unsafe` 的函数或方法（包括通过外部函数接口调用函数，见本书的前一章）
- 访问或修改静态可变变量
- 实现不安全特性

## 原始指针

原始指针 `*` 和引用 `&T` 的功能类似，但引用总是安全的，因为借用检查器保证它们指向有效数据。解引用原始指针只能通过不安全块来完成。

```rust
fn main() {
    let raw_p: *const u32 = &10;

    unsafe {
        assert!(*raw_p == 10);
    }
}
```

## 调用不安全函数

有些函数可以声明为 `unsafe`，这意味着程序员有责任确保其正确性，而不是由编译器来确保。一个例子是 `std::slice::from_raw_parts`，它在给定指向第一个元素的指针和长度的情况下创建一个切片。

```rust
use std::slice;

fn main() {
    let some_vector = vec![1, 2, 3, 4];

    let pointer = some_vector.as_ptr();
    let length = some_vector.len();

    unsafe {
        let my_slice: &[u32] = slice::from_raw_parts(pointer, length);

        assert_eq!(some_vector.as_slice(), my_slice);
    }
}
```

对于 `slice::from_raw_parts`，必须坚持的一个假设是传入的指针指向有效内存，并且指向的内存具有正确的类型。如果这些不变量不成立，那么程序的行为就是未定义的，而且不知道会发生什么。
