# Implementando un Patrón de Diseño Orientado a Objetos

El _patrón de estado_ es un patrón de diseño orientado a objetos. El eje del patrón es que definimos un conjunto de estados que un valor puede tener internamente. Los estados se representan por un conjunto de _objetos de estado_, y el comportamiento del valor cambia según su estado. Vamos a trabajar en un ejemplo de una estructura de publicación de blog que tiene un campo para almacenar su estado, que será un objeto de estado del conjunto "borrador", "revisión" o "publicado".

Los objetos de estado comparten funcionalidad: en Rust, por supuesto, usamos structs y traits en lugar de objetos e herencia. Cada objeto de estado es responsable de su propio comportamiento y de gobernar cuándo debe cambiar a otro estado. El valor que contiene un objeto de estado no sabe nada sobre el comportamiento diferente de los estados ni cuándo hacer la transición entre estados.

La ventaja de usar el patrón de estado es que, cuando los requisitos comerciales del programa cambien, no tendremos que cambiar el código del valor que contiene el estado ni el código que usa el valor. Solo tendremos que actualizar el código dentro de uno de los objetos de estado para cambiar sus reglas o quizás agregar más objetos de estado.

Primero implementaremos el patrón de estado de una manera más tradicional orientada a objetos, luego usaremos un enfoque que es un poco más natural en Rust. Vamos a profundizar para implementar incrementalmente un flujo de trabajo de publicación de blog usando el patrón de estado.

La funcionalidad final se verá así:

1.  Una publicación de blog comienza como un borrador vacío.
2.  Cuando el borrador está listo, se solicita una revisión de la publicación.
3.  Cuando la publicación es aprobada, se publica.
4.  Solo las publicaciones de blog publicadas devuelven contenido para imprimir, por lo que las publicaciones no aprobadas no se pueden publicar accidentalmente.

Cualquier otro cambio intentado en una publicación no debería tener ningún efecto. Por ejemplo, si intentamos aprobar una publicación de blog en borrador antes de haber solicitado una revisión, la publicación debería permanecer como un borrador no publicado.

La Lista 17-11 muestra este flujo de trabajo en forma de código: este es un ejemplo de uso de la API que implementaremos en un crat de biblioteca llamado `blog`. Esto todavía no se compilará porque no hemos implementado el crat `blog`.

Nombre de archivo: `src/main.rs`

```rust
use blog::Post;

fn main() {
  1 let mut post = Post::new();

  2 post.add_text("I ate a salad for lunch today");
  3 assert_eq!("", post.content());

  4 post.request_review();
  5 assert_eq!("", post.content());

  6 post.approve();
  7 assert_eq!("I ate a salad for lunch today", post.content());
}
```

Lista 17-11: Código que demuestra el comportamiento deseado que queremos que tenga nuestro crat `blog`

Queremos permitir que el usuario cree una nueva publicación de blog en borrador con `Post::new` \[1\]. Queremos permitir que se agregue texto a la publicación de blog \[2\]. Si intentamos obtener el contenido de la publicación inmediatamente, antes de la aprobación, no deberíamos obtener ningún texto porque la publicación todavía es un borrador. Hemos agregado `assert_eq!` en el código con fines de demostración \[3\]. Una excelente prueba unitaria para esto sería afirmar que una publicación de blog en borrador devuelve una cadena vacía del método `content`, pero no vamos a escribir pruebas para este ejemplo.

Luego, queremos habilitar una solicitud de revisión de la publicación \[4\], y queremos que `content` devuelva una cadena vacía mientras se espera la revisión \[5\]. Cuando la publicación recibe la aprobación \[6\], debería publicarse, lo que significa que el texto de la publicación se devolverá cuando se llame a `content` \[7\].

Tenga en cuenta que el único tipo con el que estamos interactuando del crat es el tipo `Post`. Este tipo usará el patrón de estado y contendrá un valor que será uno de tres objetos de estado que representan los diferentes estados en los que puede estar una publicación: borrador, revisión o publicada. El cambio de un estado a otro se gestionará internamente dentro del tipo `Post`. Los estados cambian en respuesta a los métodos llamados por los usuarios de nuestra biblioteca en la instancia `Post`, pero no tienen que gestionar directamente los cambios de estado. Además, los usuarios no pueden cometer un error con los estados, como publicar una publicación antes de que se revise.
