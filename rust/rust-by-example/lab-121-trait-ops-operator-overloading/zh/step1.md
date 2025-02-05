# 运算符重载

在 Rust 中，许多运算符都可以通过 trait 进行重载。也就是说，某些运算符可以根据其输入参数来完成不同的任务。这是可行的，因为运算符是方法调用的语法糖。例如，`a + b` 中的 `+` 运算符会调用 `add` 方法（就像 `a.add(b)` 一样）。这个 `add` 方法是 `Add` trait 的一部分。因此，任何实现了 `Add` trait 的类型都可以使用 `+` 运算符。

在 `core::ops` 中可以找到一系列用于重载运算符的 trait，比如 `Add`。

```rust
use std::ops;

struct Foo;
struct Bar;

#[derive(Debug)]
struct FooBar;

#[derive(Debug)]
struct BarFoo;

// `std::ops::Add` trait 用于指定 `+` 的功能。
// 这里，我们定义 `Add<Bar>` - 表示与右侧类型为 `Bar` 的加法操作的 trait。
// 以下代码块实现了该操作：Foo + Bar = FooBar
impl ops::Add<Bar> for Foo {
    type Output = FooBar;

    fn add(self, _rhs: Bar) -> FooBar {
        println!("> Foo.add(Bar) was called");

        FooBar
    }
}

// 通过颠倒类型，我们实现了非交换加法。
// 这里，我们定义 `Add<Foo>` - 表示与右侧类型为 `Foo` 的加法操作的 trait。
// 此代码块实现了该操作：Bar + Foo = BarFoo
impl ops::Add<Foo> for Bar {
    type Output = BarFoo;

    fn add(self, _rhs: Foo) -> BarFoo {
        println!("> Bar.add(Foo) was called");

        BarFoo
    }
}

fn main() {
    println!("Foo + Bar = {:?}", Foo + Bar);
    println!("Bar + Foo = {:?}", Bar + Foo);
}
```
