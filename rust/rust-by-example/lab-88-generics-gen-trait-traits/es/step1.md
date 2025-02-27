# Tratos

Por supuesto, los `tratos` también pueden ser genéricos. Aquí definimos uno que reimplementa el `trato` `Drop` como un método genérico para desecharse a sí mismo y una entrada.

```rust
// Tipos no copiables.
struct Empty;
struct Null;

// Un trato genérico sobre `T`.
trait DoubleDrop<T> {
    // Defina un método en el tipo del llamador que toma un
    // parámetro único adicional `T` y no hace nada con él.
    fn double_drop(self, _: T);
}

// Implemente `DoubleDrop<T>` para cualquier parámetro genérico `T` y
// llamador `U`.
impl<T, U> DoubleDrop<T> for U {
    // Este método toma la propiedad de ambos argumentos pasados,
    // desasignando ambos.
    fn double_drop(self, _: T) {}
}

fn main() {
    let empty = Empty;
    let null  = Null;

    // Desasigna `empty` y `null`.
    empty.double_drop(null);

    //empty;
    //null;
    // ^ TODO: Intente descomentar estas líneas.
}
```
