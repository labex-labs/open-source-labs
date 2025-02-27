# Introducción

En este laboratorio, exploraremos el tipo `Result` en Rust, que proporciona una forma de manejar errores potenciales en lugar de la posible ausencia de un valor como el tipo `Option`. El tipo `Result` puede tener dos resultados: `Ok(T)` para un resultado exitoso con el elemento `T`, y `Err(E)` para un error con el elemento `E`. Veremos cómo usar `Result` en ejemplos de código y cómo se puede usar como tipo de retorno de la función `main` para manejar errores y proporcionar un mensaje de error más específico.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
