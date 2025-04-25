# 省略规则

某些生命周期模式极为常见，因此借用检查器会允许你省略它们，以节省输入量并提高可读性。这被称为省略规则。Rust 中存在省略规则纯粹是因为这些模式很常见。

以下代码展示了一些省略规则的示例。有关省略规则更全面的描述，请参阅书中的生命周期省略规则。

```rust
// `elided_input` 和 `annotated_input` 的签名本质上是相同的
// 因为 `elided_input` 的生命周期是由编译器推断出来的：
fn elided_input(x: &i32) {
    println!("`elided_input`: {}", x);
}

fn annotated_input<'a>(x: &'a i32) {
    println!("`annotated_input`: {}", x);
}

// 同样，`elided_pass` 和 `annotated_pass` 具有相同的签名
// 因为生命周期被隐式地添加到了 `elided_pass` 中：
fn elided_pass(x: &i32) -> &i32 { x }

fn annotated_pass<'a>(x: &'a i32) -> &'a i32 { x }

fn main() {
    let x = 3;

    elided_input(&x);
    annotated_input(&x);

    println!("`elided_pass`: {}", elided_pass(&x));
    println!("`annotated_pass`: {}", annotated_pass(&x));
}
```
