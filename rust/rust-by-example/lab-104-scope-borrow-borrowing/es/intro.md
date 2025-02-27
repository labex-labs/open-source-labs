# Introducción

En este laboratorio, aprendemos sobre el préstamo en Rust, que permite acceder a datos sin tomar posesión de ellos mediante el uso de referencias ('&T') en lugar de pasar objetos por valor ('T'). El verificador de préstamos asegura que las referencias siempre apunten a objetos válidos y evita la destrucción de objetos que se están prestando.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilarlo y ejecutarlo con `rustc main.rs &&./main`.
