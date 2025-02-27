# Actualizando un crado para obtener una nueva versión

Cuando _quieres_ actualizar un crado, Cargo proporciona el comando `update`, que ignorará el archivo _Cargo.lock_ y determinará todas las últimas versiones que coinciden con tus especificaciones en `Cargo.toml`. Luego, Cargo escribirá esas versiones en el archivo _Cargo.lock_. De lo contrario, por defecto, Cargo solo buscará versiones mayores que 0.8.5 y menores que 0.9.0. Si el crado `rand` ha lanzado las dos nuevas versiones 0.8.6 y 0.9.0, verías lo siguiente si ejecutaras `cargo update`:

```bash
$ cargo update
Updating crates.io index
Updating rand v0.8.5 - > v0.8.6
```

Cargo ignora la versión 0.9.0. En este momento, también notarías un cambio en tu archivo _Cargo.lock_ que indica que la versión del crado `rand` que estás usando ahora es 0.8.6. Para usar la versión 0.9.0 de `rand` o cualquier versión en la serie 0.9.\_x\_, tendrías que actualizar el archivo `Cargo.toml` para que se vea así en su lugar:

```rust
[dependencies]
rand = "0.9.0"
```

La próxima vez que ejecutes `cargo build`, Cargo actualizará el registro de crates disponibles y reevaluará tus requisitos de `rand` de acuerdo con la nueva versión que has especificado.

Hay mucho más que decir sobre Cargo y su ecosistema, lo que discutiremos en el Capítulo 14, pero por ahora, eso es todo lo que necesitas saber. Cargo hace muy fácil reutilizar bibliotecas, por lo que los rustaceos pueden escribir proyectos más pequeños que se componen de una serie de paquetes.
