# 强制转换

较长的生命周期可以被强制转换为较短的生命周期，以便在其通常无法工作的作用域内正常工作。这有两种形式：一种是由Rust编译器推断的强制转换，另一种是通过声明生命周期差异来实现：

```rust
// 在这里，Rust推断出一个尽可能短的生命周期。
// 然后将这两个引用强制转换为该生命周期。
fn multiply<'a>(first: &'a i32, second: &'a i32) -> i32 {
    first * second
}

// `<'a: 'b, 'b>` 表示生命周期 `'a` 至少与 `'b` 一样长。
// 在这里，我们接受一个 `&'a i32` 并通过强制转换返回一个 `&'b i32`。
fn choose_first<'a: 'b, 'b>(first: &'a i32, _: &'b i32) -> &'b i32 {
    first
}

fn main() {
    let first = 2; // 较长的生命周期

    {
        let second = 3; // 较短的生命周期

        println!("The product is {}", multiply(&first, &second));
        println!("{} is the first", choose_first(&first, &second));
    };
}
```
