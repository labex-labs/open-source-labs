# Introducción

En este laboratorio, exploramos el concepto de Lenguajes Específicos de Dominio (DSL, por sus siglas en inglés) en Rust, que son mini "lenguajes" incrustados en macros de Rust. Estas macros se expanden en constructos normales de Rust, pero ofrecen una sintaxis concisa e intuitiva para una funcionalidad específica. Se demuestra un ejemplo práctico utilizando una API de calculadora, donde se suministra una expresión a la macro y la salida se imprime en la consola. Esto permite la creación de interfaces más complejas como las que se encuentran en bibliotecas como `lazy_static` o `clap`.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
