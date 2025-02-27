# Introducción

En este laboratorio, exploramos el idioma `newtype`, que ofrece garantías en tiempo de compilación al permitir crear un nuevo tipo que es distinto de su tipo subyacente. Se muestra un ejemplo donde una estructura `Years` se utiliza para representar la edad en años y una estructura `Days` se utiliza para representar la edad en días. Al utilizar el idioma `newtype`, podemos garantizar que se suministra el tipo correcto de valor a un programa, como en la función de verificación de edad `old_enough`, que requiere un valor del tipo `Years`. Además, aprendemos cómo obtener el valor de un `newtype` como su tipo subyacente utilizando la sintaxis de tuplas o de desestructuración.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
