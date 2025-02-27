# Validando el número de subprocesos en new

No estamos haciendo nada con los parámetros de `new` y `execute`. Implementemos los cuerpos de estas funciones con el comportamiento que queremos. Para comenzar, pensemos en `new`. Anteriormente elegimos un tipo sin signo para el parámetro `size` porque un grupo de subprocesos con un número negativo de subprocesos no tiene sentido. Sin embargo, un grupo de subprocesos con cero subprocesos también no tiene sentido, aunque cero es un `usize` perfectamente válido. Agregaremos código para comprobar que `size` es mayor que cero antes de devolver una instancia de `ThreadPool` y hacer que el programa se detenga con un error si recibe un cero usando la macro `assert!`, como se muestra en la Lista 20-13.

Nombre de archivo: `src/lib.rs`

```rust
impl ThreadPool {
    /// Crea un nuevo ThreadPool.
    ///
    /// El tamaño es el número de subprocesos en el grupo.
    ///
  1 /// # Panics
    ///
    /// La función `new` se detendrá con un error si el tamaño es cero.
    pub fn new(size: usize) -> ThreadPool {
      2 assert!(size > 0);

        ThreadPool
    }

    --snip--
}
```

Lista 20-13: Implementando `ThreadPool::new` para detenerse con un error si `size` es cero

También hemos agregado algunos comentarios de documentación para nuestro `ThreadPool` con comentarios de documentación. Tenga en cuenta que seguimos las buenas prácticas de documentación al agregar una sección que señala las situaciones en las que nuestra función puede detenerse con un error \[1\], como se discutió en el Capítulo 14. Intente ejecutar `cargo doc --open` y hacer clic en la estructura `ThreadPool` para ver cómo se ven los documentos generados para `new` ¡

En lugar de agregar la macro `assert!` como lo hicimos aquí \[2\], podríamos cambiar `new` a `build` y devolver un `Result` como lo hicimos con `Config::build` en el proyecto de E/S de la Lista 12-9. Pero en este caso hemos decidido que intentar crear un grupo de subprocesos sin ningún subproceso debe ser un error irreparable. Si estás con ganas de probar, intenta escribir una función llamada `build` con la siguiente firma para compararla con la función `new`:

```rust
pub fn build(
    size: usize
) -> Result<ThreadPool, PoolCreationError> {
```
