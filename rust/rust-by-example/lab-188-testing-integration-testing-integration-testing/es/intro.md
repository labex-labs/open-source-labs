# Introducción

En este laboratorio, se discute el testing de integración, que implica probar múltiples partes de una biblioteca juntas utilizando su interfaz pública. Las pruebas de integración se pueden colocar en el directorio `tests` junto al directorio `src` en un crate de Rust, y se ejecutan utilizando el comando `cargo test`. Además, el código común se puede compartir entre las pruebas de integración creando un módulo con funciones públicas e importándolo dentro de las pruebas.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
