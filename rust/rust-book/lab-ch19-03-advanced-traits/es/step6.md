# Usando el Patrón newtype para Implementar Traits Externos

En "Implementando un Trait en un Tipo", mencionamos la regla de huérfano que establece que solo se nos permite implementar un trait en un tipo si el trait o el tipo, o ambos, son locales a nuestro crate. Es posible circunvenir esta restricción usando el _patrón newtype_, que implica crear un nuevo tipo en una struct tupla. (Cubrimos las structs tupla en "Usando Structs Tupla Sin Campos con Nombre para Crear Diferentes Tipos".) La struct tupla tendrá un solo campo y será un envoltorio delgado del tipo para el cual queremos implementar un trait. Luego, el tipo envoltorio es local a nuestro crate, y podemos implementar el trait en el envoltorio. _Newtype_ es un término que proviene del lenguaje de programación Haskell. No hay penalización de rendimiento en tiempo de ejecución al usar este patrón, y el tipo envoltorio se omite en tiempo de compilación.

Como ejemplo, digamos que queremos implementar `Display` en `Vec<T>`, lo cual la regla de huérfano nos impide hacer directamente porque el trait `Display` y el tipo `Vec<T>` se definen fuera de nuestro crate. Podemos crear una struct `Wrapper` que contiene una instancia de `Vec<T>`; luego podemos implementar `Display` en `Wrapper` y usar el valor de `Vec<T>`, como se muestra en la Lista 19-23.

Nombre de archivo: `src/main.rs`

```rust
use std::fmt;

struct Wrapper(Vec<String>);

impl fmt::Display for Wrapper {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "[{}]", self.0.join(", "))
    }
}

fn main() {
    let w = Wrapper(vec![
        String::from("hello"),
        String::from("world"),
    ]);
    println!("w = {w}");
}
```

Lista 19-23: Creando un tipo `Wrapper` alrededor de `Vec<String>` para implementar `Display`

La implementación de `Display` usa `self.0` para acceder a la `Vec<T>` interna porque `Wrapper` es una struct tupla y `Vec<T>` es el elemento en el índice 0 de la tupla. Luego podemos usar la funcionalidad del tipo `Display` en `Wrapper`.

La desventaja de usar esta técnica es que `Wrapper` es un nuevo tipo, por lo que no tiene los métodos del valor que está conteniendo. Tendríamos que implementar todos los métodos de `Vec<T>` directamente en `Wrapper` de modo que los métodos deleguen en `self.0`, lo que nos permitiría tratar a `Wrapper` exactamente como una `Vec<T>`. Si quisiéramos que el nuevo tipo tuviera todos los métodos que tiene el tipo interno, implementar el trait `Deref` en `Wrapper` para devolver el tipo interno sería una solución (discutimos la implementación del trait `Deref` en "Tratando Punteros Inteligentes Como Referencias Normales con Deref"). Si no quisiéramos que el tipo `Wrapper` tuviera todos los métodos del tipo interno -por ejemplo, para restringir el comportamiento del tipo `Wrapper`- tendríamos que implementar solo los métodos que realmente queremos manualmente.

Este patrón newtype también es útil incluso cuando no se involucran traits. Cambiemos de enfoque y veamos algunas maneras avanzadas de interactuar con el sistema de tipos de Rust.
