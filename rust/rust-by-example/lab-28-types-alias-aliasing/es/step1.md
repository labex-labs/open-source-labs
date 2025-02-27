# Aliasing

La declaración `type` se puede utilizar para dar un nuevo nombre a un tipo existente. Los tipos deben tener nombres en `UpperCamelCase`, o el compilador emitirá una advertencia. La excepción a esta regla son los tipos primitivos: `usize`, `f32`, etc.

```rust
// `NanoSecond`, `Inch` y `U64` son nuevos nombres para `u64`.
type NanoSecond = u64;
type Inch = u64;
type U64 = u64;

fn main() {
    // `NanoSecond` = `Inch` = `U64` = `u64`.
    let nanoseconds: NanoSecond = 5 as U64;
    let inches: Inch = 2 as U64;

    // Tenga en cuenta que los alias de tipo *no* proporcionan ninguna seguridad adicional de tipo, porque
    // los alias *no* son nuevos tipos
    println!("{} nanosegundos + {} pulgadas = {} unidad?",
             nanoseconds,
             inches,
             nanoseconds + inches);
}
```

La principal utilización de los alias es reducir el código repetitivo; por ejemplo, el tipo `io::Result<T>` es un alias para el tipo `Result<T, io::Error>`.
