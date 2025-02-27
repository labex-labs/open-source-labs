# Introducción

En este laboratorio, aprendimos sobre el formato en Rust y cómo usar la macro `format!` para formatear variables. Vimos que el formato se especifica mediante una cadena de formato y que diferentes tipos de argumentos se pueden usar para formatear la misma variable de diferentes maneras. El rasgo de formato más común es `Display`, que maneja casos en los que el tipo de argumento no se especifica. Vimos un ejemplo de implementación del rasgo `Display` para una estructura `City`, donde formateamos los valores de latitud y longitud. También vimos un ejemplo de una estructura `Color` y tuvimos la tarea de implementar el rasgo `Display` para que muestre los valores RGB y su representación hexadecimal.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
