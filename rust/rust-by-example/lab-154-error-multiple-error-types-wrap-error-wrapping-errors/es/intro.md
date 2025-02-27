# Introducción

En este laboratorio, se demuestra el enfoque alternativo de envolver errores en un tipo de error personalizado. El ejemplo de código muestra cómo definir un alias de tipo `Result` que utiliza la enumeración `DoubleError` como la variante de error, que envuelve el `ParseIntError` de la biblioteca estándar. Al implementar los rasgos `fmt::Display`, `error::Error` y `From`, el tipo de error personalizado puede proporcionar información adicional y manejar errores subyacentes.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
