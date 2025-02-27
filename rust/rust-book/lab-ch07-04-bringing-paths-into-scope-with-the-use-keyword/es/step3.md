# Proporcionar nuevos nombres con la palabra clave as

Hay otra solución al problema de traer dos tipos con el mismo nombre al mismo alcance con `use`: después de la ruta, podemos especificar `as` y un nuevo nombre local, o _alias_, para el tipo. La Lista 7-16 muestra otra forma de escribir el código de la Lista 7-15 renomblando uno de los dos tipos `Result` usando `as`.

Nombre del archivo: `src/lib.rs`

```rust
use std::fmt::Result;
use std::io::Result as IoResult;

fn function1() -> Result {
    --snip--
}

fn function2() -> IoResult<()> {
    --snip--
}
```

Lista 7-16: Renombrar un tipo cuando se trae al alcance con la palabra clave `as`

En la segunda declaración `use`, elegimos el nuevo nombre `IoResult` para el tipo `std::io::Result`, que no entrará en conflicto con el `Result` de `std::fmt` que también hemos traído al alcance. La Lista 7-15 y la Lista 7-16 se consideran idiómáticas, ¡así que la elección es tuya!
