# Introducción

En este laboratorio, se nos presenta la firma de funciones con tiempos de vida en Rust, donde cualquier referencia debe tener un tiempo de vida anotado y cualquier referencia devuelta debe tener el mismo tiempo de vida que una entrada o ser `static`. Es importante destacar que no está permitido devolver referencias sin entrada si eso implicaría devolver referencias a datos no válidos. Los ejemplos proporcionados demuestran formas válidas de funciones con tiempos de vida, incluyendo funciones con una referencia de entrada, funciones con referencias mutables, funciones con múltiples elementos y diferentes tiempos de vida, y funciones que devuelven referencias que se han pasado como parámetros.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
