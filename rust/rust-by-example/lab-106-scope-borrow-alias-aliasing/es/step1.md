# Alias

Los datos pueden ser prestados inmutablemente cualquier número de veces, pero mientras están prestados inmutablemente, los datos originales no pueden ser prestados mutablesmente. Por otro lado, solo se permite _una_ préstamo mutable a la vez. Los datos originales solo pueden ser prestados nuevamente _después_ de que la referencia mutable haya sido usada por última vez.

```rust
struct Point { x: i32, y: i32, z: i32 }

fn main() {
    let mut point = Point { x: 0, y: 0, z: 0 };

    let borrowed_point = &point;
    let another_borrow = &point;

    // Los datos se pueden acceder a través de las referencias y el propietario original
    println!("Point has coordinates: ({}, {}, {})",
                borrowed_point.x, another_borrow.y, point.z);

    // Error! No se puede prestar `point` como mutable porque actualmente
    // está prestado como inmutable.
    // let mutable_borrow = &mut point;
    // TODO ^ Intenta descomentar esta línea

    // Los valores prestados se usan nuevamente aquí
    println!("Point has coordinates: ({}, {}, {})",
                borrowed_point.x, another_borrow.y, point.z);

    // Las referencias inmutables ya no se usan para el resto del código, por lo que
    // es posible prestar de nuevo con una referencia mutable.
    let mutable_borrow = &mut point;

    // Cambiar datos a través de la referencia mutable
    mutable_borrow.x = 5;
    mutable_borrow.y = 2;
    mutable_borrow.z = 1;

    // Error! No se puede prestar `point` como inmutable porque actualmente
    // está prestado como mutable.
    // let y = &point.y;
    // TODO ^ Intenta descomentar esta línea

    // Error! No se puede imprimir porque `println!` toma una referencia inmutable.
    // println!("Point Z coordinate is {}", point.z);
    // TODO ^ Intenta descomentar esta línea

    // Ok! Las referencias mutables se pueden pasar como inmutables a `println!`
    println!("Point has coordinates: ({}, {}, {})",
                mutable_borrow.x, mutable_borrow.y, mutable_borrow.z);

    // La referencia mutable ya no se usa para el resto del código, por lo que
    // es posible prestar de nuevo
    let new_borrowed_point = &point;
    println!("Point now has coordinates: ({}, {}, {})",
             new_borrowed_point.x, new_borrowed_point.y, new_borrowed_point.z);
}
```
