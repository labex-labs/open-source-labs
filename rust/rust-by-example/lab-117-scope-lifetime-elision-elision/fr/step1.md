# Elision

Certains modèles de durée de vie sont extrêmement courants, de sorte que le vérificateur d'emprunt vous permettra d'omettre ceux-ci pour économiser de la saisie et améliorer la lisibilité. Cela s'appelle l'élision. L'élision existe en Rust uniquement parce que ces modèles sont courants.

Le code suivant montre quelques exemples d'élision. Pour une description plus complète de l'élision, consultez la section sur l'élision de durée de vie dans le livre.

```rust
// `elided_input` et `annotated_input` ont essentiellement les mêmes signatures
// car la durée de vie de `elided_input` est inférée par le compilateur :
fn elided_input(x: &i32) {
    println!("`elided_input`: {}", x);
}

fn annotated_input<'a>(x: &'a i32) {
    println!("`annotated_input`: {}", x);
}

// De même, `elided_pass` et `annotated_pass` ont les mêmes signatures
// car la durée de vie est ajoutée implicitement à `elided_pass` :
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
