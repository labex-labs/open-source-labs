# Comentando Elementos Contenidos

El comentario de documentación `//!` agrega documentación al elemento que _contiene_ los comentarios en lugar de a los elementos _que siguen_ a los comentarios. Por lo general, usamos estos comentarios de documentación dentro del archivo raíz de la caja (`src/lib.rs` por convención) o dentro de un módulo para documentar la caja o el módulo en su conjunto.

Por ejemplo, para agregar documentación que describa el propósito de la caja `my_crate` que contiene la función `add_one`, agregamos comentarios de documentación que empiecen con `//!` al principio del archivo `src/lib.rs`, como se muestra en la Lista 14-2.

Nombre del archivo: `src/lib.rs`

```rust
//! # Mi Caja
//!
//! `my_crate` es una colección de utilidades para hacer más
//! conveniente la realización de ciertos cálculos.

/// Suma uno al número dado.
--snip--
```

Lista 14-2: Documentación para la caja `my_crate` en su conjunto

Observa que no hay ningún código después de la última línea que comienza con `//!`. Debido a que comenzamos los comentarios con `//!` en lugar de `///`, estamos documentando el elemento que contiene este comentario en lugar de un elemento que sigue a este comentario. En este caso, ese elemento es el archivo `src/lib.rs`, que es la raíz de la caja. Estos comentarios describen toda la caja.

Cuando ejecutamos `cargo doc --open`, estos comentarios se mostrarán en la página principal de la documentación de `my_crate` encima de la lista de elementos públicos de la caja, como se muestra en la Figura 14-2.

Figura 14-2: Documentación renderizada de `my_crate`, incluyendo el comentario que describe la caja en su conjunto

Los comentarios de documentación dentro de los elementos son útiles especialmente para describir cajas y módulos. úsalos para explicar el propósito general del contenedor y ayudar a tus usuarios a entender la organización de la caja.
