# 调试

所有想要使用 `std::fmt` 格式化特性的类型都需要有一个可打印的实现。只有像 `std` 库中的类型才会提供自动实现。其他所有类型都必须以某种方式手动实现。

`fmt::Debug` 特性使这变得非常简单。所有类型都可以派生（自动创建）`fmt::Debug` 实现。但 `fmt::Display` 并非如此，它必须手动实现。

```rust
// 这个结构体既不能用 `fmt::Display` 打印，也不能用 `fmt::Debug` 打印。
struct UnPrintable(i32);

// `derive` 属性会自动创建使这个结构体能用 `fmt::Debug` 打印所需的实现。
#[derive(Debug)]
struct DebugPrintable(i32);
```

所有 `std` 库类型也都可以用 `{:?}` 自动打印：

```rust
// 为 `Structure` 派生 `fmt::Debug` 实现。`Structure` 是一个包含单个 `i32` 的结构体。
#[derive(Debug)]
struct Structure(i32);

// 将一个 `Structure` 放入 `Deep` 结构体中。也使其可打印。
#[derive(Debug)]
struct Deep(Structure);

fn main() {
    // 用 `{:?}` 打印类似于用 `{}` 打印。
    println!("{:?} months in a year.", 12);
    println!("{1:?} {0:?} is the {actor:?} name.",
             "Slater",
             "Christian",
             actor="actor's");

    // `Structure` 是可打印的！
    println!("Now {:?} will print!", Structure(3));

    // `derive` 的问题在于无法控制结果的样子。要是我只想让它显示一个 `7` 呢？
    println!("Now {:?} will print!", Deep(Structure(7)));
}
```

所以 `fmt::Debug` 肯定能让其可打印，但牺牲了一些优雅性。Rust 还提供了用 `{:#?}` 进行“漂亮打印”。

```rust
#[derive(Debug)]
struct Person<'a> {
    name: &'a str,
    age: u8
}

fn main() {
    let name = "Peter";
    let age = 27;
    let peter = Person { name, age };

    // 漂亮打印
    println!("{:#?}", peter);
}
```

可以手动实现 `fmt::Display` 来控制显示。
