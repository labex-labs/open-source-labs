# Introducción

En este laboratorio, aprenderemos a evitar la limitación de devolver directamente traits en Rust mediante el uso del tipo `Box<dyn Animal>`, que permite que las funciones devuelvan una referencia a un objeto asignado en el montón que implementa el trait `Animal`.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
