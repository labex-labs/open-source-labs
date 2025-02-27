# Introducción

En este laboratorio, puedes acceder a los argumentos de línea de comandos en Rust utilizando la función `std::env::args`, que devuelve un iterador que produce una `String` para cada argumento. El primer argumento en el vector devuelto es la ruta utilizada para llamar al programa, mientras que el resto de los argumentos son los parámetros de línea de comandos. Alternativamente, puedes utilizar cajas como `clap` para un manejo más avanzado de los argumentos de línea de comandos.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puedes utilizar cualquier nombre de archivo que desees. Por ejemplo, puedes utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
