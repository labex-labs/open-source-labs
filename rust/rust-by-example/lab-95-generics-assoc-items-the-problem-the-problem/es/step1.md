# El problema

Un `trait` que es genérico sobre su tipo de contenedor tiene requisitos de especificación de tipos: los usuarios del `trait` _deben_ especificar todos sus tipos genéricos.

En el ejemplo siguiente, el `trait` `Contains` permite el uso de los tipos genéricos `A` y `B`. Luego, el `trait` se implementa para el tipo `Container`, especificando `i32` para `A` y `B` para que se pueda usar con `fn difference()`.

Debido a que `Contains` es genérico, estamos obligados a declarar _todos_ los tipos genéricos para `fn difference()`. En la práctica, queremos una forma de expresar que `A` y `B` se determinan por la `C` de _entrada_. Como verá en la siguiente sección, los tipos asociados ofrecen exactamente esa capacidad.

```rust
struct Container(i32, i32);

// Un trait que verifica si 2 elementos están almacenados dentro del contenedor.
// También recupera el primer o último valor.
trait Contains<A, B> {
    fn contains(&self, _: &A, _: &B) -> bool; // Requiere explícitamente `A` y `B`.
    fn first(&self) -> i32; // No requiere explícitamente `A` o `B`.
    fn last(&self) -> i32;  // No requiere explícitamente `A` o `B`.
}

impl Contains<i32, i32> for Container {
    // Verdadero si los números almacenados son iguales.
    fn contains(&self, number_1: &i32, number_2: &i32) -> bool {
        (&self.0 == number_1) && (&self.1 == number_2)
    }

    // Obtiene el primer número.
    fn first(&self) -> i32 { self.0 }

    // Obtiene el último número.
    fn last(&self) -> i32 { self.1 }
}

// `C` contiene `A` y `B`. A la luz de eso, tener que expresar `A` y
// `B` nuevamente es un fastidio.
fn difference<A, B, C>(container: &C) -> i32 where
    C: Contains<A, B> {
    container.last() - container.first()
}

fn main() {
    let number_1 = 3;
    let number_2 = 10;

    let container = Container(number_1, number_2);

    println!("¿Contiene el contenedor {} y {}: {}",
        &number_1, &number_2,
        container.contains(&number_1, &number_2));
    println!("Primer número: {}", container.first());
    println!("Último número: {}", container.last());

    println!("La diferencia es: {}", difference(&container));
}
```
