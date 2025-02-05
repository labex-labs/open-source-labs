# 自定义

像 `target_os` 这样的一些条件是由 `rustc` 隐式提供的，但自定义条件必须使用 `--cfg` 标志传递给 `rustc`。

```rust
#[cfg(some_condition)]
fn conditional_function() {
    println!("condition met!");
}

fn main() {
    conditional_function();
}
```

尝试在不使用自定义 `cfg` 标志的情况下运行此代码，看看会发生什么。

使用自定义 `cfg` 标志时：

```shell
$ rustc --cfg some_condition custom.rs && ./custom
condition met!
```
