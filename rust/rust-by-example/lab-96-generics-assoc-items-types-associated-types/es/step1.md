# Tipos asociados

El uso de "Tipos asociados" mejora la legibilidad general del código al mover los tipos internos localmente a un trato como _tipos de salida_. La sintaxis para la definición del `trato` es la siguiente:

```rust
// `A` y `B` se definen en el trato a través de la palabra clave `type`.
// (Nota: `type` en este contexto es diferente de `type` cuando se utiliza
// para alias).
trait Contains {
    type A;
    type B;

    // Sintaxis actualizada para referirse a estos nuevos tipos de manera genérica.
    fn contains(&self, _: &Self::A, _: &Self::B) -> bool;
}
```

Tenga en cuenta que las funciones que usan el `trato` `Contains` ya no se requiere expresar `A` o `B` en absoluto:

```rust
// Sin usar tipos asociados
fn difference<A, B, C>(container: &C) -> i32 where
    C: Contains<A, B> {... }

// Usando tipos asociados
fn difference<C: Contains>(container: &C) -> i32 {... }
```

Vamos a reescribir el ejemplo de la sección anterior usando tipos asociados:

```rust
struct Container(i32, i32);

// Un trato que verifica si 2 elementos se almacenan dentro del contenedor.
// También recupera el primer o último valor.
trait Contains {
    // Defina tipos genéricos aquí que los métodos podrán utilizar.
    type A;
    type B;

    fn contains(&self, _: &Self::A, _: &Self::B) -> bool;
    fn first(&self) -> i32;
    fn last(&self) -> i32;
}

impl Contains for Container {
    // Especifique qué tipos son `A` y `B`. Si el tipo `input`
    // es `Container(i32, i32)`, los tipos `output` se determinan
    // como `i32` e `i32`.
    type A = i32;
    type B = i32;

    // `&Self::A` y `&Self::B` también son válidos aquí.
    fn contains(&self, number_1: &i32, number_2: &i32) -> bool {
        (&self.0 == number_1) && (&self.1 == number_2)
    }
    // Obtenga el primer número.
    fn first(&self) -> i32 { self.0 }

    // Obtenga el último número.
    fn last(&self) -> i32 { self.1 }
}

fn difference<C: Contains>(container: &C) -> i32 {
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
