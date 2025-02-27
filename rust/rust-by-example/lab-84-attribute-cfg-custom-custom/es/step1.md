# Personalizado

Algunas condiciones, como `target_os`, se proporcionan implícitamente por `rustc`, pero las condiciones personalizadas deben pasarse a `rustc` utilizando la bandera `--cfg`.

```rust
#[cfg(some_condition)]
fn conditional_function() {
    println!("condition met!");
}

fn main() {
    conditional_function();
}
```

Intenta ejecutar esto para ver qué pasa sin la bandera `cfg` personalizada.

Con la bandera `cfg` personalizada:

```shell
$ rustc --cfg some_condition custom.rs && ./custom
condition met!
```
