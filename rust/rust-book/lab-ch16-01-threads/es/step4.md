# Using move Closures with Threads

A menudo usaremos la palabra clave `move` con las clausuras pasadas a `thread::spawn` porque entonces la clausura tomará la propiedad de los valores que utiliza del entorno, transferiendo así la propiedad de esos valores de un hilo a otro. En "Capturing the Environment with Closures", discutimos `move` en el contexto de las clausuras. Ahora nos centraremos más en la interacción entre `move` y `thread::spawn`.

Observa en la Lista 16-1 que la clausura que pasamos a `thread::spawn` no toma argumentos: no estamos usando ningún dato del hilo principal en el código del hilo creado. Para usar datos del hilo principal en el hilo creado, la clausura del hilo creado debe capturar los valores que necesita. La Lista 16-3 muestra un intento de crear un vector en el hilo principal y usarlo en el hilo creado. Sin embargo, esto todavía no funcionará, como verás enseguida.

Nombre de archivo: `src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(|| {
        println!("Here's a vector: {:?}", v);
    });

    handle.join().unwrap();
}
```

Lista 16-3: Intentando usar un vector creado por el hilo principal en otro hilo

La clausura usa `v`, por lo que capturará `v` y lo hará parte del entorno de la clausura. Dado que `thread::spawn` ejecuta esta clausura en un nuevo hilo, deberíamos poder acceder a `v` dentro de ese nuevo hilo. Pero cuando compilamos este ejemplo, obtenemos el siguiente error:

```bash
error[E0373]: closure may outlive the current function, but it borrows `v`,
which is owned by the current function
 --> src/main.rs:6:32
  |
6 |     let handle = thread::spawn(|| {
  |                                ^^ may outlive borrowed value `v`
7 |         println!("Here's a vector: {:?}", v);
  |                                           - `v` is borrowed here
  |
note: function requires argument type to outlive `'static`
 --> src/main.rs:6:18
  |
6 |       let handle = thread::spawn(|| {
  |  __________________^
7 | |         println!("Here's a vector: {:?}", v);
8 | |     });
  | |______^
help: to force the closure to take ownership of `v` (and any other referenced
variables), use the `move` keyword
  |
6 |     let handle = thread::spawn(move || {
  |                                ++++
```

Rust _infiere_ cómo capturar `v`, y dado que `println!` solo necesita una referencia a `v`, la clausura intenta prestar `v`. Sin embargo, hay un problema: Rust no puede saber cuánto tiempo ejecutará el hilo creado, por lo que no sabe si la referencia a `v` siempre será válida.

La Lista 16-4 presenta un escenario en el que es más probable que haya una referencia a `v` que no sea válida.

Nombre de archivo: `src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(|| {
        println!("Here's a vector: {:?}", v);
    });

    drop(v); // oh no!

    handle.join().unwrap();
}
```

Lista 16-4: Un hilo con una clausura que intenta capturar una referencia a `v` de un hilo principal que elimina `v`

Si Rust nos permitiera ejecutar este código, es posible que el hilo creado se colocara inmediatamente en segundo plano sin ejecutarse en absoluto. El hilo creado tiene una referencia a `v` dentro, pero el hilo principal elimina inmediatamente `v`, usando la función `drop` que discutimos en el Capítulo 15. Luego, cuando el hilo creado comienza a ejecutarse, `v` ya no es válido, por lo que una referencia a él también es inválida. ¡Oh no!

Para corregir el error del compilador en la Lista 16-3, podemos seguir el consejo del mensaje de error:

    help: to force the closure to take ownership of `v` (and any other referenced
    variables), use the `move` keyword
      |
    6 |     let handle = thread::spawn(move || {
      |                                ++++

Al agregar la palabra clave `move` antes de la clausura, forzamos a la clausura a tomar la propiedad de los valores que está usando en lugar de permitir que Rust infiera que debe prestar los valores. La modificación de la Lista 16-3 mostrada en la Lista 16-5 se compilará y ejecutará como queremos.

Nombre de archivo: `src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(move || {
        println!("Here's a vector: {:?}", v);
    });

    handle.join().unwrap();
}
```

Lista 16-5: Usando la palabra clave `move` para forzar a una clausura a tomar la propiedad de los valores que utiliza

Podríamos tentarnos a intentar lo mismo para corregir el código de la Lista 16-4 donde el hilo principal llamó a `drop` usando una clausura `move`. Sin embargo, esta corrección no funcionará porque lo que intenta hacer la Lista 16-4 está prohibido por una razón diferente. Si agregamos `move` a la clausura, moveríamos `v` al entorno de la clausura y ya no podríamos llamar a `drop` en él en el hilo principal. En su lugar, obtendríamos este error del compilador:

```bash
error[E0382]: use of moved value: `v`
  --> src/main.rs:10:10
   |
4  |     let v = vec![1, 2, 3];
   |         - move occurs because `v` has type `Vec<i32>`, which does not
implement the `Copy` trait
5  |
6  |     let handle = thread::spawn(move || {
   |                                ------- value moved into closure here
7  |         println!("Here's a vector: {:?}", v);
   |                                           - variable moved due to use in
closure
...
10 |     drop(v); // oh no!
   |          ^ value used here after move
```

¡Las reglas de propiedad de Rust nos han salvado de nuevo! Obtenimos un error del código de la Lista 16-3 porque Rust estaba siendo conservador y solo prestaba `v` para el hilo, lo que significaba que el hilo principal teóricamente podría invalidar la referencia del hilo creado. Al decirle a Rust que mueva la propiedad de `v` al hilo creado, estamos garantizando a Rust que el hilo principal ya no usará `v`. Si cambiamos la Lista 16-4 de la misma manera, entonces estamos violando las reglas de propiedad cuando intentamos usar `v` en el hilo principal. La palabra clave `move` anula el comportamiento conservador predeterminado de Rust de prestar; no nos permite violar las reglas de propiedad.

Ahora que hemos cubierto qué son los hilos y los métodos proporcionados por la API de hilos, echemos un vistazo a algunas situaciones en las que podemos usar hilos.
