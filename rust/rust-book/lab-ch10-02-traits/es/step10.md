# Usando Límites de Trait para Implementar Métodos Condicionalmente

Al usar un límite de trait con un bloque `impl` que utiliza parámetros de tipo genéricos, podemos implementar métodos condicionalmente para los tipos que implementan los traits especificados. Por ejemplo, el tipo `Pair<T>` en la Lista 10-15 siempre implementa la función `new` para devolver una nueva instancia de `Pair<T>` (recuerde de "Definiendo Métodos" que `Self` es un alias de tipo para el tipo del bloque `impl`, que en este caso es `Pair<T>`). Pero en el siguiente bloque `impl`, `Pair<T>` solo implementa el método `cmp_display` si su tipo interno `T` implementa el trait `PartialOrd` que habilita la comparación _y_ el trait `Display` que habilita la impresión.

Nombre de archivo: `src/lib.rs`

```rust
use std::fmt::Display;

struct Pair<T> {
    x: T,
    y: T,
}

impl<T> Pair<T> {
    fn new(x: T, y: T) -> Self {
        Self { x, y }
    }
}

impl<T: Display + PartialOrd> Pair<T> {
    fn cmp_display(&self) {
        if self.x >= self.y {
            println!("The largest member is x = {}", self.x);
        } else {
            println!("The largest member is y = {}", self.y);
        }
    }
}
```

Lista 10-15: Implementando métodos condicionalmente en un tipo genérico dependiendo de los límites de trait

También podemos implementar un trait condicionalmente para cualquier tipo que implemente otro trait. Las implementaciones de un trait en cualquier tipo que satisfaga los límites de trait se llaman _implementaciones generalizadas_ y se utilizan ampliamente en la biblioteca estándar de Rust. Por ejemplo, la biblioteca estándar implementa el trait `ToString` en cualquier tipo que implemente el trait `Display`. El bloque `impl` en la biblioteca estándar se parece a este código:

```rust
impl<T: Display> ToString for T {
    --snip--
}
```

Debido a que la biblioteca estándar tiene esta implementación generalizada, podemos llamar al método `to_string` definido por el trait `ToString` en cualquier tipo que implemente el trait `Display`. Por ejemplo, podemos convertir enteros en sus valores `String` correspondientes de la siguiente manera porque los enteros implementan `Display`:

```rust
let s = 3.to_string();
```

Las implementaciones generalizadas aparecen en la documentación del trait en la sección "Implementadores".

Los traits y los límites de trait nos permiten escribir código que utiliza parámetros de tipo genéricos para reducir la duplicación, pero también especificar al compilador que queremos que el tipo genérico tenga un comportamiento particular. El compilador puede entonces utilizar la información de los límites de trait para comprobar que todos los tipos concretos utilizados con nuestro código proporcionan el comportamiento correcto. En los lenguajes de tipado dinámico, obtendríamos un error en tiempo de ejecución si llamáramos a un método en un tipo que no definiera el método. Pero Rust mueve estos errores a tiempo de compilación para que sepamos corregir los problemas antes de que nuestro código pueda ejecutarse. Además, no tenemos que escribir código que compruebe el comportamiento en tiempo de ejecución porque ya lo hemos comprobado en tiempo de compilación. Hacer esto mejora el rendimiento sin tener que renunciar a la flexibilidad de los genéricos.
