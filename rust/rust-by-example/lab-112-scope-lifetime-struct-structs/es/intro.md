# Introducción

En este laboratorio, tenemos un código Rust que demuestra el uso de los lifetimes en structs. El código incluye un struct llamado `Borrowed` que contiene una referencia a un `i32`, y la referencia debe sobrevivir al struct mismo. También hay un struct llamado `NamedBorrowed` con dos referencias a `i32`, ambas deben sobrevivir al struct. Además, hay un enum llamado `Either` que puede ser un `i32` o una referencia a uno, y la referencia debe sobrevivir al enum. Finalmente, el código crea instancias de estos structs y enum, e imprime su contenido para mostrar el uso de los lifetimes en Rust.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
