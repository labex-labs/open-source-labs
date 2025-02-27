# Introducción

En este laboratorio, se explora el concepto de boxing, asignación en pila y asignación en el montón en Rust. Todos los valores en Rust se asignan en pila por defecto, pero se pueden empaquetar (asignar en el montón) utilizando el tipo `Box<T>`. Una caja es un puntero inteligente a un valor asignado en el montón, y cuando sale del ámbito, se llama a su destructor y se libera la memoria en el montón. El boxing permite la creación de doble indirección y se puede desreferenciar utilizando el operador `*`. El laboratorio proporciona ejemplos de código y explicaciones de cómo funciona el boxing y cómo afecta a la asignación de memoria en la pila.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
