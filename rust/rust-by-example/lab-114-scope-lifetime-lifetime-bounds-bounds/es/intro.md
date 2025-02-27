# Introducción

En este laboratorio, aprendemos sobre los límites en Rust, que se utilizan para restringir los períodos de vida o los rasgos de los tipos genéricos. El carácter `:` se utiliza para indicar que todas las referencias en un tipo deben tener un período de vida mayor que un cierto período de vida, mientras que `+` se utiliza para indicar que un tipo debe implementar un rasgo y todas las referencias en él deben tener un período de vida mayor que un cierto período de vida. Un fragmento de código de ejemplo demuestra la sintaxis y el uso de los límites en Rust.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
