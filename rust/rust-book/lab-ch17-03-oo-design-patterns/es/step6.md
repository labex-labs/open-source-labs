# Agregar aprobar para Cambiar el Comportamiento de content

El método `aprobar` será similar al método `request_review`: establecerá `state` en el valor que el estado actual dice que debe tener cuando ese estado es aprobado, como se muestra en la Lista 17-16.

Nombre de archivo: `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn approve(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.approve())
        }
    }
}

trait State {
    fn request_review(self: Box<Self>) -> Box<dyn State>;
    fn approve(self: Box<Self>) -> Box<dyn State>;
}

struct Draft {}

impl State for Draft {
    --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
      1 self
    }
}

struct PendingReview {}

impl State for PendingReview {
    --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
      2 Box::new(Published {})
    }
}

struct Published {}

impl State for Published {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        self
    }

    fn approve(self: Box<Self>) -> Box<dyn State> {
        self
    }
}
```

Lista 17-16: Implementando el método `approve` en `Post` y el trato `State`

Agregamos el método `approve` al trato `State` y agregamos una nueva estructura que implementa `State`, el estado `Published`.

Similar a la forma en que funciona `request_review` en `PendingReview`, si llamamos al método `approve` en un `Draft`, no tendrá ningún efecto porque `approve` devolverá `self` \[1\]. Cuando llamamos a `approve` en `PendingReview`, devuelve una nueva instancia empaquetada de la estructura `Published` \[2\]. La estructura `Published` implementa el trato `State`, y para ambos métodos `request_review` y `approve`, devuelve a sí misma porque la publicación debería permanecer en el estado `Published` en esos casos.

Ahora necesitamos actualizar el método `content` en `Post`. Queremos que el valor devuelto por `content` dependa del estado actual de `Post`, por lo que vamos a hacer que `Post` delegue a un método `content` definido en su `state`, como se muestra en la Lista 17-17.

Nombre de archivo: `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn content(&self) -> &str {
        self.state.as_ref().unwrap().content(self)
    }
    --snip--
}
```

Lista 17-17: Actualizando el método `content` en `Post` para delegar a un método `content` en `State`

Debido a que el objetivo es mantener todas estas reglas dentro de las estructuras que implementan `State`, llamamos a un método `content` en el valor en `state` y pasamos la instancia de la publicación (es decir, `self`) como argumento. Luego devolvemos el valor que se devuelve al usar el método `content` en el valor de `state`.

Llamamos al método `as_ref` en el `Option` porque queremos una referencia al valor dentro del `Option` en lugar de la posesión del valor. Debido a que `state` es un `Option<Box<dyn State>>`, cuando llamamos a `as_ref`, se devuelve un `Option<&Box<dyn State>>`. Si no llamáramos a `as_ref`, obtendríamos un error porque no podemos mover `state` fuera del `&self` prestado del parámetro de la función.

Luego llamamos al método `unwrap`, que sabemos que nunca causará un panic porque sabemos que los métodos en `Post` aseguran que `state` siempre contendrá un valor `Some` cuando esos métodos se completen. Este es uno de los casos que mencionamos en "Casos en los que Tienes Más Información que el Compilador" cuando sabemos que un valor `None` nunca es posible, aunque el compilador no sea capaz de entenderlo.

En este momento, cuando llamamos a `content` en el `&Box<dyn State>`, la coerción de dereferencia entrará en efecto en el `&` y el `Box` para que el método `content` finalmente se llame en el tipo que implementa el trato `State`. Eso significa que necesitamos agregar `content` a la definición del trato `State`, y ahí es donde pondremos la lógica de qué contenido devolver según el estado que tengamos, como se muestra en la Lista 17-18.

Nombre de archivo: `src/lib.rs`

```rust
trait State {
    --snip--
    fn content<'a>(&self, post: &'a Post) -> &'a str {
      1 ""
    }
}

--snip--
struct Published {}

impl State for Published {
    --snip--
    fn content<'a>(&self, post: &'a Post) -> &'a str {
      2 &post.content
    }
}
```

Lista 17-18: Agregando el método `content` al trato `State`

Agregamos una implementación predeterminada para el método `content` que devuelve una porción de cadena vacía \[1\]. Eso significa que no necesitamos implementar `content` en las estructuras `Draft` y `PendingReview`. La estructura `Published` sobrescribirá el método `content` y devolverá el valor en `post.content` \[2\].

Tenga en cuenta que necesitamos anotaciones de tiempo de vida en este método, como discutimos en el Capítulo 10. Estamos tomando una referencia a un `post` como argumento y devolviendo una referencia a una parte de ese `post`, por lo que el tiempo de vida de la referencia devuelta está relacionado con el tiempo de vida del argumento `post`.

Y ya terminamos: todo lo de la Lista 17-11 ahora funciona. Hemos implementado el patrón de estado con las reglas del flujo de trabajo de la publicación de blog. La lógica relacionada con las reglas reside en los objetos de estado en lugar de estar dispersa en todo `Post`.

> **¿Por qué No Un Enum?**
>
> Es posible que hayas estado preguntándote por qué no usamos un `enum` con los diferentes posibles estados de publicación como variantes. Esa ciertamente es una solución posible; pruébalo y compara los resultados finales para ver cuál prefieres. Una desventaja de usar un enum es que cada lugar que verifica el valor del enum necesitará una expresión `match` o similar para manejar cada posible variante. Esto podría ser más repetitivo que esta solución de objeto de trato.
