# Personalizado

Algumas condicionais, como `target_os`, são implicitamente fornecidas pelo `rustc`, mas condicionais personalizadas devem ser passadas para o `rustc` usando a flag `--cfg`.

```rust
#[cfg(some_condition)]
fn conditional_function() {
    println!("condição atendida!");
}

fn main() {
    conditional_function();
}
```

Tente executar isso para ver o que acontece sem a flag `cfg` personalizada.

Com a flag `cfg` personalizada:

```shell
$ rustc --cfg some_condition custom.rs && ./custom
condição atendida!
```
