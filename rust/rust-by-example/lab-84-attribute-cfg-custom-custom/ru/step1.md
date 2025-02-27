# Пользовательское

Некоторые условия, такие как `target_os`, неявно предоставляются `rustc`, но пользовательские условия должны быть переданы `rustc` с использованием флага `--cfg`.

```rust
#[cfg(some_condition)]
fn conditional_function() {
    println!("условие выполнено!");
}

fn main() {
    conditional_function();
}
```

Попробуйте запустить это, чтобы увидеть, что произойдет без пользовательского флага `cfg`.

С пользовательским флагом `cfg`:

```shell
$ rustc --cfg some_condition custom.rs && ./custom
условие выполнено!
```
