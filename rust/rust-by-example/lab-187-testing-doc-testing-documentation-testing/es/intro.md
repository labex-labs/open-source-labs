# Introducción

En este laboratorio, la principal forma de documentar un proyecto de Rust es a través de la adición de comentarios de documentación al código fuente, los cuales se escriben en la especificación CommonMark Markdown y admiten bloques de código dentro de ellos. Rust se encarga de la corrección y estos bloques de código se compilan y se usan como pruebas de documentación. Estas pruebas se ejecutan automáticamente al usar el comando `cargo test`. La motivación detrás de las pruebas de documentación es servir como ejemplos que demuestran la funcionalidad y permitir el uso de los ejemplos de la documentación como fragmentos de código completos.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilarlo y ejecutarlo con `rustc main.rs &&./main`.
