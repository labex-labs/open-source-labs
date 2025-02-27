# Implementar Transiciones como Transformaciones en Diferentes Tipos

Entonces, ¿cómo obtenemos una publicación publicada? Queremos imponer la regla de que una publicación en borrador debe ser revisada y aprobada antes de poder ser publicada. Una publicación en el estado de revisión pendiente todavía no debe mostrar ningún contenido. Vamos a implementar estas restricciones agregando otra estructura, `PendingReviewPost`, definiendo el método `request_review` en `DraftPost` para devolver un `PendingReviewPost` y definiendo un método `approve` en `PendingReviewPost` para devolver una `Post`, como se muestra en la Lista 17-20.

Nombre de archivo: `src/lib.rs`

```rust
impl DraftPost {
    --snip--
    pub fn request_review(self) -> PendingReviewPost {
        PendingReviewPost {
            content: self.content,
        }
    }
}

pub struct PendingReviewPost {
    content: String,
}

impl PendingReviewPost {
    pub fn approve(self) -> Post {
        Post {
            content: self.content,
        }
    }
}
```

Lista 17-20: Un `PendingReviewPost` que se crea llamando a `request_review` en `DraftPost` y un método `approve` que convierte un `PendingReviewPost` en una `Post` publicada

Los métodos `request_review` y `approve` toman la posesión de `self`, consumiendo así las instancias `DraftPost` y `PendingReviewPost` y transformándolas en una `PendingReviewPost` y una `Post` publicada, respectivamente. De esta manera, no tendremos ninguna instancia de `DraftPost` pendiente después de haber llamado a `request_review` en ellas, y así sucesivamente. La estructura `PendingReviewPost` no tiene un método `content` definido en ella, por lo que intentar leer su contenido resulta en un error del compilador, como con `DraftPost`. Debido a que la única forma de obtener una instancia de `Post` publicada que tenga un método `content` definido es llamar al método `approve` en un `PendingReviewPost`, y la única forma de obtener un `PendingReviewPost` es llamar al método `request_review` en un `DraftPost`, ahora hemos codificado el flujo de trabajo de la publicación del blog en el sistema de tipos.

Pero también tenemos que hacer algunos pequeños cambios a `main`. Los métodos `request_review` y `approve` devuelven nuevas instancias en lugar de modificar la estructura en la que se llaman, por lo que necesitamos agregar más asignaciones de sombreado `let post =` para guardar las instancias devueltas. Tampoco podemos tener las afirmaciones de que los contenidos de las publicaciones en borrador y en revisión pendiente son cadenas vacías, ni las necesitamos: ya no podemos compilar el código que intenta usar el contenido de las publicaciones en esos estados. El código actualizado en `main` se muestra en la Lista 17-21.

Nombre de archivo: `src/main.rs`

```rust
use blog::Post;

fn main() {
    let mut post = Post::new();

    post.add_text("I ate a salad for lunch today");

    let post = post.request_review();

    let post = post.approve();

    assert_eq!("I ate a salad for lunch today", post.content());
}
```

Lista 17-21: Modificaciones a `main` para usar la nueva implementación del flujo de trabajo de la publicación del blog

Los cambios que tuvimos que hacer a `main` para reasignar `post` significa que esta implementación ya no sigue exactamente el patrón de estado orientado a objetos: las transformaciones entre los estados ya no están encapsuladas por completo dentro de la implementación de `Post`. Sin embargo, nuestra ganancia es que los estados inválidos ahora son imposibles debido al sistema de tipos y la comprobación de tipos que se realiza en tiempo de compilación. Esto garantiza que ciertos errores, como la visualización del contenido de una publicación no publicada, se descubrirán antes de llegar a producción.

Prueba las tareas sugeridas al principio de esta sección en el crat `blog` tal como está después de la Lista 17-21 para ver qué opinas sobre el diseño de esta versión del código. Tenga en cuenta que algunas de las tareas pueden estar ya completadas en este diseño.

Hemos visto que aunque Rust es capaz de implementar patrones de diseño orientados a objetos, otros patrones, como codificar el estado en el sistema de tipos, también están disponibles en Rust. Estos patrones tienen diferentes ventajas y desventajas. Aunque es posible que estés muy familiarizado con los patrones orientados a objetos, repensar el problema para aprovechar las características de Rust puede proporcionar beneficios, como prevenir algunos errores en tiempo de compilación. Los patrones orientados a objetos no siempre serán la mejor solución en Rust debido a ciertas características, como la propiedad, que los lenguajes orientados a objetos no tienen.
