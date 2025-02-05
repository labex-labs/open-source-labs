# 作为输出参数

闭包可以作为输入参数，那么将闭包作为输出参数返回也应该是可行的。然而，根据定义，匿名闭包类型是未知的，所以我们必须使用 `impl Trait` 来返回它们。

用于返回闭包的有效 trait 有：

- `Fn`
- `FnMut`
- `FnOnce`

除此之外，必须使用 `move` 关键字，这表明所有捕获都是按值进行的。这是必需的，因为一旦函数退出，任何通过引用的捕获都会被丢弃，从而在闭包中留下无效引用。

```rust
fn create_fn() -> impl Fn() {
    let text = "Fn".to_owned();

    move || println!("This is a: {}", text)
}

fn create_fnmut() -> impl FnMut() {
    let text = "FnMut".to_owned();

    move || println!("This is a: {}", text)
}

fn create_fnonce() -> impl FnOnce() {
    let text = "FnOnce".to_owned();

    move || println!("This is a: {}", text)
}

fn main() {
    let fn_plain = create_fn();
    let mut fn_mut = create_fnmut();
    let fn_once = create_fnonce();

    fn_plain();
    fn_mut();
    fn_once();
}
```
