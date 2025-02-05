# 结构体

结构体中生命周期的标注与函数类似：

```rust
// 一个名为 `Borrowed` 的类型，它存储了一个指向 `i32` 的引用。
// 指向 `i32` 的引用的生命周期必须长于 `Borrowed`。
#[derive(Debug)]
struct Borrowed<'a>(&'a i32);

// 同样地，这里的两个引用的生命周期都必须长于这个结构体。
#[derive(Debug)]
struct NamedBorrowed<'a> {
    x: &'a i32,
    y: &'a i32,
}

// 一个枚举，它可以是一个 `i32` 或者是一个指向 `i32` 的引用。
#[derive(Debug)]
enum Either<'a> {
    Num(i32),
    Ref(&'a i32),
}

fn main() {
    let x = 18;
    let y = 15;

    let single = Borrowed(&x);
    let double = NamedBorrowed { x: &x, y: &y };
    let reference = Either::Ref(&x);
    let number    = Either::Num(y);

    println!("x 在 {:?} 中被借用", single);
    println!("x 和 y 在 {:?} 中被借用", double);
    println!("x 在 {:?} 中被借用", reference);
    println!("y 在 {:?} 中 *未* 被借用", number);
}
```
