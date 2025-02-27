# Documentación

Usa `cargo doc` para generar documentación en `target/doc`.

Usa `cargo test` para ejecutar todas las pruebas (incluyendo las pruebas de documentación), y `cargo test --doc` para ejecutar solo las pruebas de documentación.

Estos comandos invocarán adecuadamente `rustdoc` (y `rustc`) según sea necesario.

## Comentarios de documentación

Los comentarios de documentación son muy útiles para los grandes proyectos que requieren documentación. Cuando se ejecuta `rustdoc`, estos son los comentarios que se compilan en documentación. Se denotan con un `///` y admiten \[Markdown\].

````rust
#![crate_name = "doc"]

/// Aquí se representa a una persona
pub struct Person {
    /// Una persona debe tener un nombre, sin importar lo mucho que Julieta lo odie
    name: String,
}

impl Person {
    /// Devuelve una persona con el nombre que se le dio
    ///
    /// # Argumentos
    ///
    /// * `name` - Una porción de cadena que contiene el nombre de la persona
    ///
    /// # Ejemplos
    ///
    /// ```
    /// // Puedes tener código de Rust entre los corchetes dentro de los comentarios
    /// // Si pasas --test a `rustdoc`, incluso lo probará por ti!
    /// use doc::Person;
    /// let person = Person::new("name");
    /// ```
    pub fn new(name: &str) -> Person {
        Person {
            name: name.to_string(),
        }
    }

    /// Da un saludo amigable!
    ///
    /// Dice "Hola, [name](Person::name)" a la `Person` en la que se llama.
    pub fn hello(& self) {
        println!("Hola, {}!", self.name);
    }
}

fn main() {
    let john = Person::new("John");

    john.hello();
}
````

Para ejecutar las pruebas, primero compila el código como una biblioteca, luego indica a `rustdoc` dónde encontrar la biblioteca para que pueda enlazarla en cada programa de prueba de documentación:

```shell
$ rustc doc.rs --crate-type lib
$ rustdoc --test --extern doc="libdoc.rlib" doc.rs
```

## Atributos de documentación

A continuación se presentan algunos ejemplos de los atributos `#[doc]` más comunes utilizados con `rustdoc`.

## `inline`

Se utiliza para insertar las documentaciones en línea, en lugar de enlazar a una página separada.

```rust
#[doc(inline)]
pub use bar::Bar;

/// documentación de bar
mod bar {
    /// las documentaciones de Bar
    pub struct Bar;
}
```

## `no_inline`

Se utiliza para evitar enlazar a una página separada o a cualquier lugar.

```rust
// Ejemplo de libcore/prelude
#[doc(no_inline)]
pub use crate::mem::drop;
```

## `hidden`

Usar esto le dice a `rustdoc` que no incluya esto en la documentación:

```rust
// Ejemplo de la biblioteca futures-rs
#[doc(hidden)]
pub use self::async_await::*;
```

Para la documentación, `rustdoc` es ampliamente utilizado por la comunidad. Es lo que se utiliza para generar la [documentación de la biblioteca estándar](https://doc.rust-lang.org/std/).
