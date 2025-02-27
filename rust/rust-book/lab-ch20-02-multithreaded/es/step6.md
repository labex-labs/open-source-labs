# Construyendo ThreadPool usando el desarrollo dirigido por el compilador

Haga los cambios de la Lista 20-12 en `src/main.rs`, y luego usemos los errores del compilador de `cargo check` para guiar nuestro desarrollo. Aquí está el primer error que obtenemos:

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0433]: failed to resolve: use of undeclared type `ThreadPool`
  --> src/main.rs:11:16
   |
11 |     let pool = ThreadPool::new(4);
   |                ^^^^^^^^^^ use of undeclared type `ThreadPool`
```

¡Excelente! Este error nos dice que necesitamos un tipo o módulo `ThreadPool`, así que lo construiremos ahora. Nuestra implementación de `ThreadPool` será independiente del tipo de trabajo que está haciendo nuestro servidor web. Entonces, cambiemos el crate `hello` de un crate binario a un crate de biblioteca para contener nuestra implementación de `ThreadPool`. Después de cambiar a un crate de biblioteca, también podríamos usar la biblioteca separada de grupos de subprocesos para cualquier trabajo que queramos hacer usando un grupo de subprocesos, no solo para atender solicitudes web.

Cree un archivo `src/lib.rs` que contenga lo siguiente, que es la definición más simple de una estructura `ThreadPool` que podemos tener por ahora:

Nombre de archivo: `src/lib.rs`

```rust
pub struct ThreadPool;
```

Luego edite el archivo `main.rs` para traer `ThreadPool` al ámbito desde el crate de biblioteca agregando el siguiente código al principio de `src/main.rs`:

Nombre de archivo: `src/main.rs`

```rust
use hello::ThreadPool;
```

Este código todavía no funcionará, pero revisémoslo de nuevo para obtener el siguiente error que necesitamos resolver:

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0599]: no function or associated item named `new` found for struct
`ThreadPool` in the current scope
  --> src/main.rs:12:28
   |
12 |     let pool = ThreadPool::new(4);
   |                            ^^^ function or associated item not found in
`ThreadPool`
```

Este error indica que a continuación necesitamos crear una función asociada llamada `new` para `ThreadPool`. También sabemos que `new` necesita tener un parámetro que pueda aceptar `4` como argumento y debe devolver una instancia de `ThreadPool`. Implementemos la función `new` más simple que tendrá esas características:

Nombre de archivo: `src/lib.rs`

```rust
pub struct ThreadPool;

impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        ThreadPool
    }
}
```

Elegimos `usize` como el tipo del parámetro `size` porque sabemos que un número negativo de subprocesos no tiene sentido. También sabemos que usaremos este `4` como el número de elementos en una colección de subprocesos, que es para lo que es el tipo `usize`, como se discutió en "Tipos enteros".

Revisemos el código de nuevo:

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0599]: no method named `execute` found for struct `ThreadPool` in the
current scope
  --> src/main.rs:17:14
   |
17 |         pool.execute(|| {
   |              ^^^^^^^ method not found in `ThreadPool`
```

Ahora el error ocurre porque no tenemos un método `execute` en `ThreadPool`. Recuerde de "Creación de un número finito de subprocesos" que decidimos que nuestro grupo de subprocesos debería tener una interfaz similar a `thread::spawn`. Además, implementaremos la función `execute` de modo que tome la clausura que se le da y la deje ejecutar por un subproceso ocioso en el grupo.

Definiremos el método `execute` en `ThreadPool` para tomar una clausura como parámetro. Recuerde de "Moviendo valores capturados fuera de las clausuras y los tratos Fn" que podemos tomar clausuras como parámetros con tres tratos diferentes: `Fn`, `FnMut` y `FnOnce`. Necesitamos decidir qué tipo de clausura usar aquí. Sabemos que terminaremos haciendo algo similar a la implementación de `thread::spawn` de la biblioteca estándar, así que podemos ver qué límites tiene la firma de `thread::spawn` en su parámetro. La documentación nos muestra lo siguiente:

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
    where
        F: FnOnce() -> T,
        F: Send + 'static,
        T: Send + 'static,
```

El parámetro de tipo `F` es el que nos interesa aquí; el parámetro de tipo `T` está relacionado con el valor de retorno, y no nos interesa eso. Podemos ver que `spawn` usa `FnOnce` como el trato límite en `F`. Probablemente esto también sea lo que queremos, porque eventualmente pasaremos el argumento que obtenemos en `execute` a `spawn`. Podemos estar más seguros de que `FnOnce` es el trato que queremos usar porque el subproceso para ejecutar una solicitud solo ejecutará la clausura de esa solicitud una vez, lo que coincide con el `Once` en `FnOnce`.

El parámetro de tipo `F` también tiene el trato límite `Send` y el límite de vida `'static`, que son útiles en nuestra situación: necesitamos `Send` para transferir la clausura de un subproceso a otro y `'static` porque no sabemos cuánto tiempo tardará el subproceso en ejecutarse. Cree un método `execute` en `ThreadPool` que tomará un parámetro genérico de tipo `F` con estos límites:

Nombre de archivo: `src/lib.rs`

```rust
impl ThreadPool {
    --snip--
    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() 1 + Send + 'static,
    {
    }
}
```

Todavía usamos los `()` después de `FnOnce` \[1\] porque este `FnOnce` representa una clausura que no toma parámetros y devuelve el tipo unitario `()`. Al igual que las definiciones de funciones, el tipo de retorno se puede omitir de la firma, pero incluso si no tenemos parámetros, todavía necesitamos los paréntesis.

Una vez más, esta es la implementación más simple del método `execute`: no hace nada, pero solo estamos intentando hacer que nuestro código se compile. Revisémoslo de nuevo:

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 0.24s
```

¡Se compila! Pero tenga en cuenta que si intenta `cargo run` y hace una solicitud en el navegador, verá los errores en el navegador que vimos al principio del capítulo. Nuestra biblioteca todavía no está llamando realmente a la clausura pasada a `execute` todavía.

> Nota: Un dicho que es posible que escuche sobre lenguajes con compiladores estrictos, como Haskell y Rust, es "si el código se compila, funciona". Pero este dicho no es universalmente cierto. Nuestro proyecto se compila, pero no hace absolutamente nada. Si estuviéramos construyendo un proyecto real y completo, este sería un buen momento para comenzar a escribir pruebas unitarias para comprobar que el código se compila _y_ tiene el comportamiento que queremos.
