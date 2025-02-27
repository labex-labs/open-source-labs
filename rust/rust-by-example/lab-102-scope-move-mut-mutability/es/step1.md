# Mutabilidad

La mutabilidad de los datos puede cambiar cuando se transfiere la propiedad.

```rust
fn main() {
    let immutable_box = Box::new(5u32);

    println!("immutable_box contiene {}", immutable_box);

    // Error de mutabilidad
    //*immutable_box = 4;

    // *Mueva* la caja, cambiando la propiedad (y la mutabilidad)
    let mut mutable_box = immutable_box;

    println!("mutable_box contiene {}", mutable_box);

    // Modifique el contenido de la caja
    *mutable_box = 4;

    println!("mutable_box ahora contiene {}", mutable_box);
}
```
