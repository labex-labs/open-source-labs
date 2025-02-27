# Tipos de Punto Flotante

Rust también tiene dos tipos primitivos para _números de punto flotante_, que son números con puntos decimales. Los tipos de punto flotante de Rust son `f32` y `f64`, que tienen un tamaño de 32 bits y 64 bits, respectivamente. El tipo predeterminado es `f64` porque en las CPUs modernas, tiene aproximadamente la misma velocidad que `f32` pero es capaz de mayor precisión. Todos los tipos de punto flotante son con signo.

Crea un nuevo proyecto llamado `data-types`:

```bash
cargo new data-types
cd data-types
```

Aquí hay un ejemplo que muestra números de punto flotante en acción:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let x = 2.0; // f64

    let y: f32 = 3.0; // f32
}
```

Los números de punto flotante se representan de acuerdo con el estándar IEEE-754. El tipo `f32` es un flotante de precisión simple, y `f64` tiene doble precisión.
