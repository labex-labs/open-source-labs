# Elisión

Algunos patrones de tiempo de vida son abrumadoramente comunes, por lo que el verificador de préstamos te permitirá omitirlos para ahorrar tiempo de escritura y mejorar la legibilidad. Esto se conoce como elisión. La elisión existe en Rust solo porque estos patrones son comunes.

El siguiente código muestra algunos ejemplos de elisión. Para una descripción más completa de la elisión, consulte la elisión de tiempo de vida en el libro.

```rust
// `elided_input` y `annotated_input` esencialmente tienen firmas idénticas
// porque el tiempo de vida de `elided_input` es inferido por el compilador:
fn elided_input(x: &i32) {
    println!("`elided_input`: {}", x);
}

fn annotated_input<'a>(x: &'a i32) {
    println!("`annotated_input`: {}", x);
}

// Del mismo modo, `elided_pass` y `annotated_pass` tienen firmas idénticas
// porque el tiempo de vida se agrega implícitamente a `elided_pass`:
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
