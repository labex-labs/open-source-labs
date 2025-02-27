# Devolviendo traits con `dyn`

El compilador de Rust necesita saber cuánto espacio requiere el tipo de retorno de cada función. Esto significa que todas sus funciones deben devolver un tipo concreto. A diferencia de otros lenguajes, si tiene un trait como `Animal`, no puede escribir una función que devuelva `Animal`, porque sus diferentes implementaciones requerirán diferentes cantidades de memoria.

Sin embargo, hay una solución fácil. En lugar de devolver directamente un objeto de trait, nuestras funciones devuelven un `Box` que _contiene_ algún `Animal`. Un `box` es simplemente una referencia a alguna memoria en el montón. Debido a que una referencia tiene un tamaño conocido en tiempo de compilación y el compilador puede garantizar que apunta a un `Animal` asignado en el montón, ¡podemos devolver un trait desde nuestra función!

Rust intenta ser lo más explícito posible siempre que asigna memoria en el montón. Entonces, si su función devuelve un puntero a trait en el montón de esta manera, debe escribir el tipo de retorno con la palabra clave `dyn`, por ejemplo `Box<dyn Animal>`.

```rust
struct Oveja {}
struct Vaca {}

trait Animal {
    // Firma del método de instancia
    fn noise(&self) -> &'static str;
}

// Implemente el trait `Animal` para `Sheep`.
impl Animal for Oveja {
    fn noise(&self) -> &'static str {
        "baaaaah!"
    }
}

// Implemente el trait `Animal` para `Cow`.
impl Animal for Vaca {
    fn noise(&self) -> &'static str {
        "moooooo!"
    }
}

// Devuelve alguna struct que implementa Animal, pero no sabemos cuál en tiempo de compilación.
fn animal_aleatorio(random_number: f64) -> Box<dyn Animal> {
    if random_number < 0.5 {
        Box::new(Oveja {})
    } else {
        Box::new(Vaca {})
    }
}

fn main() {
    let random_number = 0.234;
    let animal = animal_aleatorio(random_number);
    println!("Has elegido al azar un animal, y dice {}", animal.noise());
}
```
