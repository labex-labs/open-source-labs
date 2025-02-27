# Introducción

En este laboratorio, el código demuestra cómo utilizar el tipo `Box` para preservar los errores originales al envolverlos, lo que permite un manejo dinámico de errores, y el trato `From` de la biblioteca `Std` ayuda a convertir cualquier tipo que implemente el trato `Error` en el objeto de trato `Box<Error>`. Incluye un ejemplo de conversión y manejo de errores utilizando `Box` con un tipo de error personalizado.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
