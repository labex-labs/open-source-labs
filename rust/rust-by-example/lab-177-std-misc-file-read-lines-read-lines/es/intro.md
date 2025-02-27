# Introducción

En este laboratorio, se nos da una implementación sencilla y una implementación más eficiente para leer líneas de un archivo en Rust. El enfoque sencillo utiliza `read_to_string` para leer el archivo en una sola cadena y luego la divide en líneas, mientras que el enfoque más eficiente utiliza un `BufReader` para leer el archivo línea por línea sin cargar todo el contenido en memoria.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
