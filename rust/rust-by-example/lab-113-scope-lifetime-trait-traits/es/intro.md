# Introducción

En este laboratorio, exploramos la anotación de los períodos de vida en los métodos de tratos, lo cual es similar a las funciones. Esto también implica anotar los períodos de vida en el bloque `impl`. El código proporcionado demuestra un ejemplo en el que una estructura `Borrowed` tiene una anotación de período de vida, y se implementa la característica `Default` para ella utilizando el período de vida anotado. Luego, la función principal crea una instancia de `Borrowed` utilizando el método `Default::default()`, mostrando el uso de los períodos de vida en los métodos de tratos.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
