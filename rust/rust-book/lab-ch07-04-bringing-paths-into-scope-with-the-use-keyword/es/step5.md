# Usar paquetes externos

En el Capítulo 2, programamos un proyecto de juego de adivinanza que utilizaba un paquete externo llamado `rand` para obtener números aleatorios. Para usar `rand` en nuestro proyecto, agregamos esta línea a `Cargo.toml`:

Nombre del archivo: `Cargo.toml`

```tomltoml
rand = "0.8.5"
```

Agregar `rand` como dependencia en `Cargo.toml` le indica a Cargo que descargue el paquete `rand` y cualquier dependencia de *https://crates.io*, y haga `rand` disponible para nuestro proyecto.

Luego, para traer las definiciones de `rand` al alcance de nuestro paquete, agregamos una línea `use` que comienza con el nombre del crat, `rand`, y listamos los elementos que queríamos traer al alcance. Recuerde que en "Generating a Random Number", trajimos la característica `Rng` al alcance y llamamos a la función `rand::thread_rng`:

```rust
use rand::Rng;

fn main() {
    let secret_number = rand::thread_rng().gen_range(1..=100);
}
```

Los miembros de la comunidad de Rust han hecho muchos paquetes disponibles en *https://crates.io*, y traer cualquiera de ellos a su paquete implica estos mismos pasos: listarlos en el archivo `Cargo.toml` de su paquete y usar `use` para traer elementos de sus crates al alcance.

Tenga en cuenta que la biblioteca estándar `std` también es un crat externo a nuestro paquete. Debido a que la biblioteca estándar se distribuye con el lenguaje Rust, no es necesario cambiar `Cargo.toml` para incluir `std`. Pero sí necesitamos referirnos a ella con `use` para traer elementos de allí al alcance de nuestro paquete. Por ejemplo, con `HashMap` usaríamos esta línea:

```rust
use std::collections::HashMap;
```

Esta es una ruta absoluta que comienza con `std`, el nombre del crat de la biblioteca estándar.
