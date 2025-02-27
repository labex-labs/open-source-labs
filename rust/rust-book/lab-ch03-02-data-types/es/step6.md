# El Tipo Booleano

Como en la mayoría de los otros lenguajes de programación, un tipo booleano en Rust tiene dos valores posibles: `true` y `false`. Los booleanos tienen un tamaño de un byte. El tipo booleano en Rust se especifica usando `bool`. Por ejemplo:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let t = true;

    let f: bool = false; // con anotación de tipo explícita
}
```

La principal forma de usar valores booleanos es a través de condicionales, como una expresión `if`. Veremos cómo funcionan las expresiones `if` en Rust en "Control Flow".
