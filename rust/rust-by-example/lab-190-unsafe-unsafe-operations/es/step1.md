# Operaciones no seguras

Como introducción a esta sección, para citar las documentaciones oficiales, "uno debe tratar de minimizar la cantidad de código no seguro en una base de código". Con eso en mente, ¡empecemos! Las anotaciones no seguras en Rust se utilizan para evitar las protecciones establecidas por el compilador; específicamente, hay cuatro cosas principales para las que se utiliza lo no seguro:

- Desreferenciar punteros crudos
- Llamar a funciones o métodos que son `unsafe` (incluyendo llamar a una función a través de FFI, ver [un capítulo anterior del libro)
- Acceder o modificar variables estáticas mutables
- Implementar rasgos no seguros

## Punteros crudos

Los punteros crudos `*` y las referencias `&T` funcionan de manera similar, pero las referencias siempre son seguras porque se garantiza que apunten a datos válidos debido al verificador de préstamos. La desreferencia de un puntero crudo solo se puede hacer a través de un bloque no seguro.

```rust
fn main() {
    let raw_p: *const u32 = &10;

    unsafe {
        assert!(*raw_p == 10);
    }
}
```

## Llamar a funciones no seguras

Algunas funciones se pueden declarar como `unsafe`, lo que significa que es responsabilidad del programador garantizar la corrección en lugar de la del compilador. Un ejemplo de esto es \[`std::slice::from_raw_parts`\] que creará un segmento dado un puntero al primer elemento y una longitud.

```rust
use std::slice;

fn main() {
    let some_vector = vec![1, 2, 3, 4];

    let pointer = some_vector.as_ptr();
    let length = some_vector.len();

    unsafe {
        let my_slice: &[u32] = slice::from_raw_parts(pointer, length);

        assert_eq!(some_vector.as_slice(), my_slice);
    }
}
```

Para `slice::from_raw_parts`, una de las suposiciones que _debe_ mantenerse es que el puntero pasado apunte a una memoria válida y que la memoria apuntada sea del tipo correcto. Si estas invariantes no se mantienen, entonces el comportamiento del programa es indefinido y no se sabe lo que pasará.
