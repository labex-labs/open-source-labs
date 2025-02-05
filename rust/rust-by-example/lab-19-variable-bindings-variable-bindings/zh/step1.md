# 变量绑定

Rust 通过静态类型检查提供类型安全。变量绑定在声明时可以进行类型注释。然而，在大多数情况下，编译器能够从上下文推断出变量的类型，从而大大减轻注释负担。

可以使用 `let` 绑定将值（如字面量）绑定到变量。

```rust
fn main() {
    let an_integer = 1u32;
    let a_boolean = true;
    let unit = ();

    // 将 `an_integer` 复制到 `copied_integer`
    let copied_integer = an_integer;

    println!("An integer: {:?}", copied_integer);
    println!("A boolean: {:?}", a_boolean);
    println!("Meet the unit value: {:?}", unit);

    // 编译器会对未使用的变量绑定发出警告；可以通过在变量名前加下划线来消除这些警告
    let _unused_variable = 3u32;

    let noisy_unused_variable = 2u32;
    // FIXME ^ 在前加下划线以抑制警告
    // 请注意，警告可能不会在浏览器中显示
}
```
