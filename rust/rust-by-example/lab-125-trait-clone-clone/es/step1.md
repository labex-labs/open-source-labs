# Clone

Cuando se tratan de recursos, el comportamiento predeterminado es transferirlos durante las asignaciones o las llamadas a funciones. Sin embargo, a veces también necesitamos hacer una copia del recurso.

El trato `Clone` nos ayuda a hacer exactamente esto. En la mayoría de los casos, podemos usar el método `.clone()` definido por el trato `Clone`.

```rust
// Un struct unitario sin recursos
#[derive(Debug, Clone, Copy)]
struct Unit;

// Un struct tupla con recursos que implementa el trato `Clone`
#[derive(Clone, Debug)]
struct Pair(Box<i32>, Box<i32>);

fn main() {
    // Instanciar `Unit`
    let unit = Unit;
    // Copiar `Unit`, no hay recursos que mover
    let copied_unit = unit;

    // Ambos `Unit` se pueden usar de forma independiente
    println!("original: {:?}", unit);
    println!("copia: {:?}", copied_unit);

    // Instanciar `Pair`
    let pair = Pair(Box::new(1), Box::new(2));
    println!("original: {:?}", pair);

    // Mover `pair` a `moved_pair`, mueve los recursos
    let moved_pair = pair;
    println!("movido: {:?}", moved_pair);

    // Error! `pair` ha perdido sus recursos
    //println!("original: {:?}", pair);
    // TODO ^ Intenta descomentar esta línea

    // Clonar `moved_pair` en `cloned_pair` (los recursos se incluyen)
    let cloned_pair = moved_pair.clone();
    // Eliminar el par original usando std::mem::drop
    drop(moved_pair);

    // Error! `moved_pair` ha sido eliminado
    //println!("copia: {:?}", moved_pair);
    // TODO ^ Intenta descomentar esta línea

    // El resultado de.clone() todavía se puede usar!
    println!("clon: {:?}", cloned_pair);
}
```
