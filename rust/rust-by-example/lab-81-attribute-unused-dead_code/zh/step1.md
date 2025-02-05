# `dead_code`

编译器提供了一个 `dead_code` 检查（lint），它会对未使用的函数发出警告。可以使用一个属性（attribute）来禁用该检查。

```rust
fn used_function() {}

// `#[allow(dead_code)]` 是一个用于禁用 `dead_code` 检查的属性
#[allow(dead_code)]
fn unused_function() {}

fn noisy_unused_function() {}
// FIXME ^ 添加一个属性以抑制警告

fn main() {
    used_function();
}
```

请注意，在实际程序中，你应该消除死代码。在这些示例中，由于示例的交互性质，我们会在某些地方允许存在死代码。
