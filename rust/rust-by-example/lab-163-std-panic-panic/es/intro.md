# Introducción

En este laboratorio, aprendemos sobre la macro `panic!` en Rust, que se puede utilizar para generar un error y comenzar a deshacerse de su pila, lo que hace que el programa informe el mensaje de error y salga. La ejecución del programa se encarga de liberar todos los recursos propiedad del hilo llamando al destructor de sus objetos. También examinamos un ejemplo de uso de la macro `panic!` para manejar la división por cero y verificamos que no se produzcan fugas de memoria utilizando Valgrind.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
