# Implementando el Trato Deref

Como se discutió en "Implementando un Trato en un Tipo", para implementar un trato necesitamos proporcionar implementaciones para los métodos requeridos por el trato. El trato `Deref`, proporcionado por la biblioteca estándar, nos exige implementar un método llamado `deref` que presta `self` y devuelve una referencia a los datos internos. La Lista 15-10 contiene una implementación de `Deref` para agregar a la definición de `MyBox<T>`.

Nombre de archivo: `src/main.rs`

```rust
use std::ops::Deref;

impl<T> Deref for MyBox<T> {
  1 type Target = T;

    fn deref(&self) -> &Self::Target {
      2 &self.0
    }
}
```

Lista 15-10: Implementando `Deref` en `MyBox<T>`

La sintaxis `type Target = T;` [1] define un tipo asociado para que el trato `Deref` lo use. Los tipos asociados son una forma ligeramente diferente de declarar un parámetro genérico, pero por ahora no tienes que preocuparte por ellos; los cubriremos con más detalle en el Capítulo 19.

Rellenamos el cuerpo del método `deref` con `&self.0` para que `deref` devuelva una referencia al valor que queremos acceder con el operador `*` [2]; recuerda de "Usando Structs Tupla Sin Campos con Nombres para Crear Diferentes Tipos" que `.0` accede al primer valor en una struct tupla. La función `main` de la Lista 15-9 que llama a `*` en el valor `MyBox<T>` ahora se compila y las afirmaciones se pasan correctamente.

Sin el trato `Deref`, el compilador solo puede desreferenciar referencias `&`. El método `deref` le da al compilador la capacidad de tomar un valor de cualquier tipo que implemente `Deref` y llamar al método `deref` para obtener una referencia `&` que sabe cómo desreferenciar.

Cuando escribimos `*y` en la Lista 15-9, detrás de escena Rust realmente ejecutó este código:

```rust
*(y.deref())
```

Rust sustituye el operador `*` con una llamada al método `deref` y luego una desreferencia normal para que no tengamos que pensar en si necesitamos llamar al método `deref` o no. Esta característica de Rust nos permite escribir código que funciona de manera idéntica ya sea que tengamos una referencia normal o un tipo que implemente `Deref`.

La razón por la que el método `deref` devuelve una referencia a un valor y que la desreferencia normal fuera de los paréntesis en `*(y.deref())` todavía es necesaria tiene que ver con el sistema de propiedad. Si el método `deref` devolviera el valor directamente en lugar de una referencia al valor, el valor se movería fuera de `self`. No queremos tomar posesión del valor interno dentro de `MyBox<T>` en este caso o en la mayoría de los casos en los que usamos el operador de desreferencia.

Tenga en cuenta que el operador `*` se reemplaza con una llamada al método `deref` y luego una llamada al operador `*` solo una vez, cada vez que usamos un `*` en nuestro código. Debido a que la sustitución del operador `*` no se recursiva infinitamente, terminamos con datos de tipo `i32`, que coincide con el `5` en `assert_eq!` de la Lista 15-9.
