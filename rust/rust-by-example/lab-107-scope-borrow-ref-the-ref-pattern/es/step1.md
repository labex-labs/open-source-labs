# El patrón `ref`

Al hacer coincidencia de patrones o desestructuración a través de la vinculación `let`, la palabra clave `ref` se puede utilizar para tomar referencias a los campos de un struct/tupla. El siguiente ejemplo muestra algunos casos en los que esto puede ser útil:

```rust
#[derive(Clone, Copy)]
struct Point { x: i32, y: i32 }

fn main() {
    let c = 'Q';

    // Un préstamo `ref` en el lado izquierdo de una asignación es equivalente a
    // un préstamo `&` en el lado derecho.
    let ref ref_c1 = c;
    let ref_c2 = &c;

    println!("ref_c1 es igual a ref_c2: {}", *ref_c1 == *ref_c2);

    let point = Point { x: 0, y: 0 };

    // `ref` también es válido cuando se desestructura un struct.
    let _copy_of_x = {
        // `ref_to_x` es una referencia al campo `x` de `point`.
        let Point { x: ref ref_to_x, y: _ } = point;

        // Devuelve una copia del campo `x` de `point`.
        *ref_to_x
    };

    // Una copia mutable de `point`
    let mut mutable_point = point;

    {
        // `ref` se puede combinar con `mut` para tomar referencias mutables.
        let Point { x: _, y: ref mut mut_ref_to_y } = mutable_point;

        // Modifica el campo `y` de `mutable_point` a través de una referencia mutable.
        *mut_ref_to_y = 1;
    }

    println!("point es ({}, {})", point.x, point.y);
    println!("mutable_point es ({}, {})", mutable_point.x, mutable_point.y);

    // Una tupla mutable que incluye un puntero
    let mut mutable_tuple = (Box::new(5u32), 3u32);

    {
        // Desestructura `mutable_tuple` para cambiar el valor de `last`.
        let (_, ref mut last) = mutable_tuple;
        *last = 2u32;
    }

    println!("tupla es {:?}", mutable_tuple);
}
```
