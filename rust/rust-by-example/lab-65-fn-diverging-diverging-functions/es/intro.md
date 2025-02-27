# Introducción

En este laboratorio, aprendemos sobre funciones divergentes que se marcan con `!` en Rust. Las funciones divergentes nunca devuelven y su tipo de retorno es un tipo vacío. Esto es diferente del tipo `()` que solo tiene un valor posible. Las funciones divergentes pueden ser útiles cuando se requiere convertir a cualquier otro tipo, como en las ramas `match`. También son el tipo de retorno de las funciones que bucle indefinidamente o terminan el proceso.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
