# 函数

忽略[省略规则]，带有生命周期的函数签名有一些限制：

- 任何引用**必须**带有注释生命周期。
- 任何返回的引用**必须**与输入具有相同的生命周期，或者是 `static`。

此外，请注意，如果返回没有输入的引用会导致返回对无效数据的引用，则是被禁止的。以下示例展示了一些带有生命周期的函数的有效形式：

```rust
// 带有生命周期 `'a` 的一个输入引用，其生命周期必须至少与函数一样长。
fn print_one<'a>(x: &'a i32) {
    println!("`print_one`: x is {}", x);
}

// 带有生命周期的可变引用也是可能的。
fn add_one<'a>(x: &'a mut i32) {
    *x += 1;
}

// 具有不同生命周期的多个元素。在这种情况下，两者具有相同的生命周期 `'a` 是可以的，但在更复杂的情况下，可能需要不同的生命周期。
fn print_multi<'a, 'b>(x: &'a i32, y: &'b i32) {
    println!("`print_multi`: x is {}, y is {}", x, y);
}

// 返回传入的引用是可以接受的。但是，必须返回正确的生命周期。
fn pass_x<'a, 'b>(x: &'a i32, _: &'b i32) -> &'a i32 { x }

//fn invalid_output<'a>() -> &'a String { &String::from("foo") }
// 上面的代码是无效的：`'a` 必须比函数的生命周期长。在这里，`&String::from("foo")` 会创建一个 `String`，然后是一个引用。然后在退出作用域时数据会被丢弃，留下一个对无效数据的引用以供返回。

fn main() {
    let x = 7;
    let y = 9;

    print_one(&x);
    print_multi(&x, &y);

    let z = pass_x(&x, &y);
    print_one(z);

    let mut t = 3;
    add_one(&mut t);
    print_one(&t);
}
```
