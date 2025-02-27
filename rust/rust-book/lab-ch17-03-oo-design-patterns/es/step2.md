# Definiendo Post y Creando una Nueva Instancia en el Estado Borrador

Comencemos con la implementación de la biblioteca. Sabemos que necesitamos una estructura pública `Post` que almacene algún contenido, así que comenzaremos con la definición de la estructura y una función pública asociada `new` para crear una instancia de `Post`, como se muestra en la Lista 17-12. También crearemos un trato privado `State` que definirá el comportamiento que todos los objetos de estado de un `Post` deben tener.

Luego, `Post` contendrá un objeto de trato de `Box<dyn State>` dentro de un `Option<T>` en un campo privado llamado `state` para almacenar el objeto de estado. Verás por qué es necesario el `Option<T>` en un momento.

Nombre de archivo: `src/lib.rs`

```rust
pub struct Post {
    state: Option<Box<dyn State>>,
    content: String,
}

impl Post {
    pub fn new() -> Post {
        Post {
          1 state: Some(Box::new(Draft {})),
          2 content: String::new(),
        }
    }
}

trait State {}

struct Draft {}

impl State for Draft {}
```

Lista 17-12: Definición de una estructura `Post` y una función `new` que crea una nueva instancia de `Post`, un trato `State` y una estructura `Draft`

El trato `State` define el comportamiento compartido por diferentes estados de publicación. Los objetos de estado son `Draft`, `PendingReview` y `Published`, y todos ellos implementarán el trato `State`. Por ahora, el trato no tiene ningún método, y comenzaremos definiendo solo el estado `Draft` porque ese es el estado en el que queremos que comience una publicación.

Cuando creamos una nueva instancia de `Post`, establecemos su campo `state` en un valor `Some` que contiene un `Box` \[1\]. Este `Box` apunta a una nueva instancia de la estructura `Draft`. Esto garantiza que cada vez que creemos una nueva instancia de `Post`, comenzará como un borrador. Debido a que el campo `state` de `Post` es privado, no hay forma de crear un `Post` en cualquier otro estado. En la función `Post::new`, establecemos el campo `content` en una `String` nueva y vacía \[2\].
