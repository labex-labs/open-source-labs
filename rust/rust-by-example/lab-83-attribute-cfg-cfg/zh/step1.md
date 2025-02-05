# `cfg`

可以通过两种不同的运算符进行配置条件检查：

- `cfg` 属性：在属性位置使用 `#[cfg(...)]`
- `cfg!` 宏：在布尔表达式中使用 `cfg!(...)`

前者启用条件编译，而后者有条件地求值为 `true` 或 `false` 字面量，从而允许在运行时进行检查。两者都使用相同的参数语法。

与 `#[cfg]` 不同，`cfg!` 不会移除任何代码，只会求值为 `true` 或 `false`。例如，当在条件中使用 `cfg!` 时，`if/else` 表达式中的所有代码块都必须有效，无论 `cfg!` 的求值结果如何。

```rust
// 仅当目标操作系统是 linux 时，此函数才会被编译
#[cfg(target_os = "linux")]
fn are_you_on_linux() {
    println!("你正在运行 linux!");
}

// 仅当目标操作系统不是 linux 时，此函数才会被编译
#[cfg(not(target_os = "linux"))]
fn are_you_on_linux() {
    println!("你没有运行 linux!");
}

fn main() {
    are_you_on_linux();

    println!("你确定吗？");
    if cfg!(target_os = "linux") {
        println!("是的。肯定是 linux!");
    } else {
        println!("是的。肯定不是 linux!");
    }
}
```
