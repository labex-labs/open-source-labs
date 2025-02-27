# Codificar Estados y Comportamiento como Tipos

Te mostraremos cómo repensar el patrón de estado para obtener un conjunto diferente de ventajas y desventajas. En lugar de encapsular completamente los estados y las transiciones para que el código externo no tenga conocimiento de ellos, codificaremos los estados en diferentes tipos. En consecuencia, el sistema de comprobación de tipos de Rust evitará intentos de usar publicaciones en borrador donde solo se permiten publicaciones publicadas emitiendo un error del compilador.

Consideremos la primera parte de `main` en la Lista 17-11:

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let mut post = Post::new();

    post.add_text("I ate a salad for lunch today");
    assert_eq!("", post.content());
}
```

Todavía habilitamos la creación de nuevas publicaciones en el estado de borrador usando `Post::new` y la capacidad de agregar texto al contenido de la publicación. Pero en lugar de tener un método `content` en una publicación en borrador que devuelva una cadena vacía, haremos que las publicaciones en borrador no tengan el método `content` en absoluto. De esa manera, si intentamos obtener el contenido de una publicación en borrador, obtendremos un error del compilador que nos dice que el método no existe. Como resultado, será imposible para nosotros mostrar accidentalmente el contenido de una publicación en borrador en producción porque ese código ni siquiera se compilará. La Lista 17-19 muestra la definición de una estructura `Post` y una estructura `DraftPost`, así como los métodos en cada una.

Nombre de archivo: `src/lib.rs`

```rust
pub struct Post {
    content: String,
}

pub struct DraftPost {
    content: String,
}

impl Post {
  1 pub fn new() -> DraftPost {
        DraftPost {
            content: String::new(),
        }
    }

  2 pub fn content(&self) -> &str {
        &self.content
    }
}

impl DraftPost {
  3 pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }
}
```

Lista 17-19: Una `Post` con un método `content` y una `DraftPost` sin un método `content`

Tanto la estructura `Post` como la estructura `DraftPost` tienen un campo privado `content` que almacena el texto de la publicación del blog. Las estructuras ya no tienen el campo `state` porque estamos moviendo la codificación del estado a los tipos de las estructuras. La estructura `Post` representará una publicación publicada y tiene un método `content` que devuelve el `content` \[2\].

Todavía tenemos una función `Post::new`, pero en lugar de devolver una instancia de `Post`, devuelve una instancia de `DraftPost` \[1\]. Debido a que `content` es privado y no hay ninguna función que devuelva `Post`, no es posible crear una instancia de `Post` en este momento.

La estructura `DraftPost` tiene un método `add_text`, por lo que podemos agregar texto a `content` como antes \[3\], pero tenga en cuenta que `DraftPost` no tiene un método `content` definido. Entonces, ahora el programa asegura que todas las publicaciones empiecen como publicaciones en borrador y que las publicaciones en borrador no tienen su contenido disponible para mostrar. Cualquier intento de circunvenir estas restricciones resultará en un error del compilador.
