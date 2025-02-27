# Introducción

En este laboratorio, puedes usar `cargo doc` para generar documentación en `target/doc`. También puedes usar `cargo test` para ejecutar todas las pruebas, incluyendo las pruebas de documentación, y `cargo test --doc` para ejecutar solo las pruebas de documentación. Los comentarios de documentación, denotados por `///`, se compilan en documentación por `rustdoc` y admiten Markdown. Estos comentarios son útiles para documentar el código en grandes proyectos. Los atributos de documentación, como `inline`, `no_inline` y `hidden`, se usan con frecuencia con `rustdoc`. Rustdoc es ampliamente utilizado por la comunidad para generar documentación, incluyendo la documentación de la biblioteca estándar.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puedes usar cualquier nombre de archivo que desees. Por ejemplo, puedes usar `main.rs`, compilarlo y ejecutarlo con `rustc main.rs &&./main`.
