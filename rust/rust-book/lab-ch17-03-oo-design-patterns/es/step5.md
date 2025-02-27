# Solicitar una Revisión Cambia el Estado de la Publicación

A continuación, necesitamos agregar funcionalidad para solicitar una revisión de una publicación, lo que debería cambiar su estado de `Draft` a `PendingReview`. La Lista 17-15 muestra este código.

Nombre de archivo: `src/lib.rs`

```rust
impl Post {
    --snip--
  1 pub fn request_review(&mut self) {
      2 if let Some(s) = self.state.take() {
          3 self.state = Some(s.request_review())
        }
    }
}

trait State {
  4 fn request_review(self: Box<Self>) -> Box<dyn State>;
}

struct Draft {}

impl State for Draft {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
      5 Box::new(PendingReview {})
    }
}

struct PendingReview {}

impl State for PendingReview {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
      6 self
    }
}
```

Lista 17-15: Implementando métodos `request_review` en `Post` y el trato `State`

Le damos a `Post` un método público llamado `request_review` que tomará una referencia mutable a `self` \[1\]. Luego llamamos a un método interno `request_review` en el estado actual de `Post` \[3\], y este segundo método `request_review` consume el estado actual y devuelve un nuevo estado.

Agregamos el método `request_review` al trato `State` \[4\]; todos los tipos que implementen el trato ahora necesitarán implementar el método `request_review`. Tenga en cuenta que en lugar de tener `self`, `&self` o `&mut self` como el primer parámetro del método, tenemos `self: Box<Self>`. Esta sintaxis significa que el método solo es válido cuando se llama en un `Box` que contiene el tipo. Esta sintaxis toma posesión de `Box<Self>`, invalidando el antiguo estado para que el valor de estado de `Post` pueda transformarse en un nuevo estado.

Para consumir el antiguo estado, el método `request_review` necesita tomar posesión del valor de estado. Aquí es donde entra el `Option` en el campo `state` de `Post`: llamamos al método `take` para sacar el valor `Some` del campo `state` y dejar un `None` en su lugar porque Rust no nos permite tener campos no rellenados en structs \[2\]. Esto nos permite mover el valor de `state` fuera de `Post` en lugar de prestarlo. Luego estableceremos el valor de `state` de la publicación en el resultado de esta operación.

Necesitamos establecer `state` en `None` temporalmente en lugar de establecerlo directamente con código como `self.state = self.state.request_review();` para obtener la posesión del valor de `state`. Esto garantiza que `Post` no pueda usar el antiguo valor de `state` después de haberlo transformado en un nuevo estado.

El método `request_review` en `Draft` devuelve una nueva instancia empaquetada de una nueva estructura `PendingReview`, que representa el estado cuando una publicación está esperando una revisión \[5\]. La estructura `PendingReview` también implementa el método `request_review` pero no realiza ninguna transformación. En lugar de eso, devuelve a sí misma \[6\] porque cuando solicitamos una revisión de una publicación ya en el estado `PendingReview`, debería permanecer en el estado `PendingReview`.

Ahora podemos comenzar a ver las ventajas del patrón de estado: el método `request_review` en `Post` es el mismo independientemente del valor de su `state`. Cada estado es responsable de sus propias reglas.

Dejaremos el método `content` en `Post` tal como está, devolviendo una porción de cadena vacía. Ahora podemos tener un `Post` en el estado `PendingReview` así como en el estado `Draft`, pero queremos el mismo comportamiento en el estado `PendingReview`. La Lista 17-11 ahora funciona hasta la línea en \[5\]!
