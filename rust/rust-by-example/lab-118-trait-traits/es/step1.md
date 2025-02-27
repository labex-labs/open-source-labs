# Rasgos

Un `rasgo` es una colección de métodos definidos para un tipo desconocido: `Self`. Pueden acceder a otros métodos declarados en el mismo rasgo.

Los rasgos se pueden implementar para cualquier tipo de datos. En el ejemplo siguiente, definimos `Animal`, un grupo de métodos. Luego, se implementa el rasgo `Animal` para el tipo de datos `Sheep`, lo que permite el uso de los métodos de `Animal` con una instancia de `Sheep`.

```rust
struct Sheep { naked: bool, name: &'static str }

trait Animal {
    // Firma de la función asociada; `Self` se refiere al tipo del implementador.
    fn new(name: &'static str) -> Self;

    // Firmas de los métodos; estos devolverán una cadena.
    fn name(&self) -> &'static str;
    fn noise(&self) -> &'static str;

    // Los rasgos pueden proporcionar definiciones predeterminadas de métodos.
    fn talk(&self) {
        println!("{} says {}", self.name(), self.noise());
    }
}

impl Sheep {
    fn is_naked(&self) -> bool {
        self.naked
    }

    fn shear(&mut self) {
        if self.is_naked() {
            // Los métodos del implementador pueden usar los métodos del rasgo del implementador.
            println!("{} is already naked...", self.name());
        } else {
            println!("{} gets a haircut!", self.name);

            self.naked = true;
        }
    }
}

// Implementa el rasgo `Animal` para `Sheep`.
impl Animal for Sheep {
    // `Self` es el tipo del implementador: `Sheep`.
    fn new(name: &'static str) -> Sheep {
        Sheep { name: name, naked: false }
    }

    fn name(&self) -> &'static str {
        self.name
    }

    fn noise(&self) -> &'static str {
        if self.is_naked() {
            "baaaaah?"
        } else {
            "baaaaah!"
        }
    }

    // Los métodos predeterminados del rasgo pueden ser sobrescritos.
    fn talk(&self) {
        // Por ejemplo, podemos agregar un poco de reflexión tranquila.
        println!("{} pauses briefly... {}", self.name, self.noise());
    }
}

fn main() {
    // La anotación de tipo es necesaria en este caso.
    let mut dolly: Sheep = Animal::new("Dolly");
    // TODO ^ Try removing the type annotations.

    dolly.talk();
    dolly.shear();
    dolly.talk();
}
```
