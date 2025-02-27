# Usar rutas anidadas para limpiar listas de `use` grandes

Si estamos usando múltiples elementos definidos en el mismo crat o el mismo módulo, listar cada elemento en una línea separada puede ocupar mucho espacio vertical en nuestros archivos. Por ejemplo, estas dos declaraciones `use` que teníamos en el juego de adivinanza en la Lista 2-4 traen elementos de `std` al alcance:

Nombre del archivo: `src/main.rs`

```rust
--snip--
use std::cmp::Ordering;
use std::io;
--snip--
```

En lugar de eso, podemos usar rutas anidadas para traer los mismos elementos al alcance en una sola línea. Hacemos esto especificando la parte común de la ruta, seguida de dos puntos, y luego corchetes alrededor de una lista de las partes de las rutas que difieren, como se muestra en la Lista 7-18.

Nombre del archivo: `src/main.rs`

```rust
--snip--
use std::{cmp::Ordering, io};
--snip--
```

Lista 7-18: Especificar una ruta anidada para traer múltiples elementos con el mismo prefijo al alcance

En programas más grandes, traer muchos elementos al alcance del mismo crat o módulo usando rutas anidadas puede reducir en gran medida el número de declaraciones `use` separadas necesarias.

Podemos usar una ruta anidada en cualquier nivel de una ruta, lo que es útil al combinar dos declaraciones `use` que comparten una subruta. Por ejemplo, la Lista 7-19 muestra dos declaraciones `use`: una que trae `std::io` al alcance y otra que trae `std::io::Write` al alcance.

Nombre del archivo: `src/lib.rs`

```rust
use std::io;
use std::io::Write;
```

Lista 7-19: Dos declaraciones `use` donde una es una subruta de la otra

La parte común de estas dos rutas es `std::io`, y esa es la primera ruta completa. Para fusionar estas dos rutas en una sola declaración `use`, podemos usar `self` en la ruta anidada, como se muestra en la Lista 7-20.

Nombre del archivo: `src/lib.rs`

```rust
use std::io::{self, Write};
```

Lista 7-20: Combinar las rutas de la Lista 7-19 en una sola declaración `use`

Esta línea trae `std::io` y `std::io::Write` al alcance.
