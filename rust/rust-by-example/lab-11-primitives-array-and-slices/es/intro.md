# Introducción

En este laboratorio, exploraremos arrays y slices en Rust. Un array es una colección de objetos del mismo tipo almacenados en memoria contigua, y su longitud es conocida en tiempo de compilación. Por otro lado, un slice es similar a un array, pero su longitud no es conocida en tiempo de compilación. Los slices se pueden utilizar para prestar una sección de un array. También cubriremos cómo crear arrays, acceder a elementos, calcular la longitud, asignar memoria, prestar arrays como slices y trabajar con slices vacíos. Además, discutiremos cómo acceder de manera segura a los elementos de un array utilizando el método `.get()` y manejar errores de desbordamiento.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
