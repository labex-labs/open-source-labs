# Préstamo

En la mayoría de los casos, queremos acceder a datos sin tomar posesión de ellos. Para lograr esto, Rust utiliza un mecanismo de _préstamo_. En lugar de pasar objetos por valor (`T`), los objetos se pueden pasar por referencia (`&T`).

El compilador garantiza en forma estática (a través de su verificador de préstamos) que las referencias _siempre_ apunten a objetos válidos. Es decir, mientras existan referencias a un objeto, el objeto no puede ser destruido.

```rust
// Esta función toma posesión de una caja y la destruye
fn eat_box_i32(boxed_i32: Box<i32>) {
    println!("Destruyendo caja que contiene {}", boxed_i32);
}

// Esta función presta un i32
fn borrow_i32(borrowed_i32: &i32) {
    println!("Este entero es: {}", borrowed_i32);
}

fn main() {
    // Crea una caja con un i32, y un i32 en la pila
    let boxed_i32 = Box::new(5_i32);
    let stacked_i32 = 6_i32;

    // Presta el contenido de la caja. No se toma posesión,
    // por lo que el contenido se puede prestar nuevamente.
    borrow_i32(&boxed_i32);
    borrow_i32(&stacked_i32);

    {
        // Toma una referencia al dato contenido dentro de la caja
        let _ref_to_i32: &i32 = &boxed_i32;

        // Error!
        // No se puede destruir `boxed_i32` mientras el valor interno esté prestado más adelante en el ámbito.
        eat_box_i32(boxed_i32);
        // FIXME ^ Comenta esta línea

        // Intenta prestar `_ref_to_i32` después de que el valor interno sea destruido
        borrow_i32(_ref_to_i32);
        // `_ref_to_i32` sale del ámbito y ya no está prestado.
    }

    // `boxed_i32` ahora puede entregar la posesión a `eat_box` y ser destruido
    eat_box_i32(boxed_i32);
}
```
