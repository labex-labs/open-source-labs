# カスタム

`target_os` のような一部の条件は、`rustc` によって暗黙的に提供されますが、カスタム条件は `--cfg` フラグを使用して `rustc` に渡す必要があります。

```rust
#[cfg(some_condition)]
fn conditional_function() {
    println!("condition met!");
}

fn main() {
    conditional_function();
}
```

これを実行して、カスタム `cfg` フラグなしで何が起こるか見てみてください。

カスタム `cfg` フラグ付きで：

```shell
$ rustc --cfg some_condition custom.rs && ./custom
condition met!
```
