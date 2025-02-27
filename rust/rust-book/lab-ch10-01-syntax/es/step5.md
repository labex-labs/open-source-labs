# En definiciones de enums

Como lo hicimos con los structs, podemos definir enums para almacenar tipos de datos genéricos en sus variantes. Echemos otro vistazo al enum `Option<T>` que proporciona la biblioteca estándar y que usamos en el Capítulo 6:

```rust
enum Option<T> {
    Some(T),
    None,
}
```

Esta definición ahora debería tener más sentido para usted. Como puede ver, el enum `Option<T>` es genérico sobre el tipo `T` y tiene dos variantes: `Some`, que almacena un valor del tipo `T`, y una variante `None` que no almacena ningún valor. Al usar el enum `Option<T>`, podemos expresar el concepto abstracto de un valor opcional, y debido a que `Option<T>` es genérico, podemos usar esta abstracción sin importar el tipo del valor opcional.

Los enums también pueden usar múltiples tipos genéricos. La definición del enum `Result` que usamos en el Capítulo 9 es un ejemplo:

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

El enum `Result` es genérico sobre dos tipos, `T` y `E`, y tiene dos variantes: `Ok`, que almacena un valor del tipo `T`, y `Err`, que almacena un valor del tipo `E`. Esta definición hace conveniente usar el enum `Result` en cualquier lugar donde tengamos una operación que puede tener éxito (devolver un valor de algún tipo `T`) o fracasar (devolver un error de algún tipo `E`). De hecho, esto es lo que usamos para abrir un archivo en la Lista 9-3, donde `T` se llenó con el tipo `std::fs::File` cuando el archivo se abrió correctamente y `E` se llenó con el tipo `std::io::Error` cuando hubo problemas al abrir el archivo.

Cuando reconozca situaciones en su código con múltiples definiciones de struct o enum que difieren solo en los tipos de los valores que almacenan, puede evitar la duplicación usando tipos genéricos en lugar de eso.
