# Introducción

En este laboratorio, la jerarquía de archivos de los módulos en el ejemplo de código puede representarse de la siguiente manera: Existe un directorio llamado "my" que contiene dos archivos, "inaccessible.rs" y "nested.rs". Además, existe un archivo llamado "my.rs" y un archivo llamado "split.rs". El archivo "split.rs" incluye el módulo "my" que está definido en el archivo "my.rs", y el archivo "my.rs" incluye los módulos "inaccessible" y "nested" que están definidos en los archivos "inaccessible.rs" y "nested.rs" respectivamente.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
