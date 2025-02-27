# Introducción

En este laboratorio, aprenderá sobre el atributo `cfg` y la macro `cfg!` en Rust, que permiten realizar comprobaciones condicionales en la configuración y la evaluación, respectivamente. El atributo `cfg` habilita la compilación condicional, mientras que la macro `cfg!` evalúa a verdadero o falso en tiempo de ejecución. Los bloques de código que usan `cfg!` deben ser válidos independientemente del resultado de la evaluación, a diferencia de `#[cfg]` que puede eliminar código.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilarlo y ejecutarlo con `rustc main.rs &&./main`.
