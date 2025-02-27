# Introducción

En este laboratorio, exploraremos las operaciones no seguras en Rust, que se utilizan para evitar las protecciones del compilador y se utilizan típicamente para desreferenciar punteros crudos, llamar a funciones no seguras, acceder o modificar variables estáticas mutables e implementar rasgos no seguros. Estas operaciones deben minimizarse en una base de código para garantizar la seguridad.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
