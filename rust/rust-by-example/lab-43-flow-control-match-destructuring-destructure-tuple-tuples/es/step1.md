# tuplas

Las tuplas se pueden desestructurar en una declaración `match` de la siguiente manera:

```rust
fn main() {
    let triple = (0, -2, 3);
    // TODO ^ Prueba diferentes valores para `triple`

    println!("Dime algo sobre {:?}", triple);
    // Se puede utilizar `match` para desestructurar una tupla
    match triple {
        // Desestructura el segundo y el tercer elemento
        (0, y, z) => println!("El primero es `0`, `y` es {:?} y `z` es {:?}", y, z),
        (1,..)  => println!("El primero es `1` y el resto no importa"),
        (.., 2)  => println!("El último es `2` y el resto no importa"),
        (3,.., 4)  => println!("El primero es `3`, el último es `4` y el resto no importa"),
        // `..` se puede utilizar para ignorar el resto de la tupla
        _      => println!("No importa lo que sean"),
        // `_` significa no enlazar el valor a una variable
    }
}
```
