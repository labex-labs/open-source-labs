# Aceptando Argumentos de Línea de Comandos

Vamos a crear un nuevo proyecto, como siempre, con `cargo new`. Llamaremos a nuestro proyecto `minigrep` para diferenciarlo de la herramienta `grep` que puede que ya tengas en tu sistema.

```bash
$ cargo new minigrep
     Created binary (application) `minigrep` project
$ cd minigrep
```

La primera tarea es hacer que `minigrep` acepte sus dos argumentos de línea de comandos: la ruta del archivo y una cadena de texto a buscar. Es decir, queremos poder ejecutar nuestro programa con `cargo run`, dos guiones para indicar que los siguientes argumentos son para nuestro programa y no para `cargo`, una cadena de texto a buscar y una ruta a un archivo en el que buscar, así:

```bash
cargo run -- searchstring example-filename.txt
```

En este momento, el programa generado por `cargo new` no puede procesar los argumentos que le damos. Algunas bibliotecas existentes en *https://crates.io* pueden ayudar a escribir un programa que acepte argumentos de línea de comandos, pero como estás aprendiendo este concepto, vamos a implementar esta capacidad nosotros mismos.
