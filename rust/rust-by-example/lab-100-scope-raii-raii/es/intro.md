# Introducción

En este laboratorio, exploraremos el concepto de RAII en Rust, que fuerza que la adquisición de recursos sea la inicialización. Esto significa que cuando los objetos salen del ámbito, se llaman a sus destructores y se liberan los recursos que poseen, eliminando la necesidad de la gestión manual de memoria y asegurando la protección contra errores de fuga de recursos. También aprenderemos sobre el trato `Drop` en Rust, que permite implementar lógica de destructor personalizada para los tipos que lo requieren.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilarlo y ejecutarlo con `rustc main.rs &&./main`.
