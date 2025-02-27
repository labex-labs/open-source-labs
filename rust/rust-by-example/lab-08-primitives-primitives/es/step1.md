# Primitivas

Rust ofrece acceso a una amplia variedad de `primitivas`. Un ejemplo incluye:

## Tipos Escalares

- Enteros firmados: `i8`, `i16`, `i32`, `i64`, `i128` y `isize` (tamaño del puntero)
- Enteros no firmados: `u8`, `u16`, `u32`, `u64`, `u128` y `usize` (tamaño del puntero)
- Punto flotante: `f32`, `f64`
- Valores escalares Unicode `char` como `'a'`, `'α'` y `'∞'` (4 bytes cada uno)
- `bool` que puede ser `true` o `false`
- El tipo unitario `()`, cuyo único valor posible es una tupla vacía: `()`

A pesar de que el valor de un tipo unitario sea una tupla, no se considera un tipo compuesto porque no contiene múltiples valores.

## Tipos Compuestos

- Arrays como `[1, 2, 3]`
- Tuplas como `(1, true)`

Las variables siempre pueden ser _anotadas con su tipo_. Los números también pueden ser anotados a través de un _sufijo_ o _por defecto_. Los enteros por defecto son `i32` y los flotantes son `f64`. Tenga en cuenta que Rust también puede inferir los tipos a partir del contexto.

```rust
fn main() {
    // Las variables pueden ser anotadas con su tipo.
    let lógico: bool = true;

    let un_flotante: f64 = 1.0;  // Anotación regular
    let un_entero   = 5i32; // Anotación con sufijo

    // O se usará el valor por defecto.
    let flotante_por_defecto   = 3.0; // `f64`
    let entero_por_defecto = 7;   // `i32`

    // Un tipo también puede ser inferido a partir del contexto.
    let mut tipo_inferido = 12; // Se infiere el tipo i64 a partir de otra línea.
    tipo_inferido = 4294967296i64;

    // El valor de una variable mutable puede ser cambiado.
    let mut mutable = 12; // `i32` mutable
    mutable = 21;

    // Error! El tipo de una variable no puede ser cambiado.
    mutable = true;

    // Las variables pueden ser sobrescritas con sombreado.
    let mutable = true;
}
```
