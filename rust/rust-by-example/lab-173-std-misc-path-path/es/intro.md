# Introducción

En este laboratorio, exploraremos la estructura `Path` en Rust, que representa rutas de archivos en el sistema de archivos subyacente. Viene en dos variantes: `posix::Path` para sistemas UNIX-like y `windows::Path` para Windows. La `Path` se puede crear a partir de un `OsStr` y proporciona varios métodos para recuperar información del archivo o directorio al que apunta la ruta. Es importante destacar que una `Path` es inmutable, y su versión con propiedad se llama `PathBuf`, que se puede mutar in situ. La relación entre `Path` y `PathBuf` es similar a la entre `str` y `String`.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
