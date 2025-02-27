# Introducción

En este laboratorio, se explora el concepto de coerción en Rust, donde una vida útil más larga puede ser forzada a convertirse en una más corta para habilitar la funcionalidad dentro de un ámbito específico. Esto puede ocurrir a través de la coerción inferida por el compilador de Rust o declarando una diferencia de vida útil utilizando sintaxis como `<'a: 'b, 'b>`.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
