# Introducción

En este laboratorio, tenemos una función `create` que abre un archivo en modo de solo escritura. Crea un nuevo archivo o destruye el contenido antiguo si el archivo ya existe. La función utiliza la biblioteca estándar de Rust para manejar las operaciones de archivo. El ejemplo proporcionado demuestra cómo usar la función `create` para escribir el contenido de una cadena estática `LOREM_IPSUM` en un archivo llamado "lorem_ipsum.txt". La salida muestra una confirmación de una operación de escritura exitosa, y el contenido del archivo se muestra usando el comando `cat`.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
