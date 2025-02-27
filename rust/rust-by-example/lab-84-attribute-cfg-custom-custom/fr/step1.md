# Custom

Certaines conditions telles que `target_os` sont implicitement fournies par `rustc`, mais les conditions personnalisées doivent être passées à `rustc` à l'aide du drapeau `--cfg`.

```rust
#[cfg(some_condition)]
fn conditional_function() {
    println!("condition rencontrée!");
}

fn main() {
    conditional_function();
}
```

Essayez d'exécuter ceci pour voir ce qui se passe sans le drapeau `cfg` personnalisé.

Avec le drapeau `cfg` personnalisé :

```shell
$ rustc --cfg some_condition custom.rs && ./custom
condition rencontrée!
```
