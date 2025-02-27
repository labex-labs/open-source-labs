# Introducción

En este laboratorio, se introduce la función `open` como una manera de abrir un archivo en modo de solo lectura proporcionando la ruta al archivo deseado. La función devuelve un objeto `File` que posee el descriptor de archivo y se encarga de cerrar el archivo cuando ya no es necesario.

Para utilizar la función `open`, es necesario importar los módulos necesarios, como `std::fs::File`, `std::io::prelude::*` y `std::path::Path`. Luego, se llama al método `File::open` con la ruta como argumento. Si el archivo se abre correctamente, la función devuelve un objeto `Result<File, io::Error>`, de lo contrario, se detiene con un mensaje de error.

Una vez que el archivo está abierto, su contenido se puede leer utilizando el método `read_to_string`. Este método lee el contenido del archivo en una cadena y devuelve un `Result<usize, io::Error>`. Si la operación de lectura es exitosa, la cadena contendrá el contenido del archivo. De lo contrario, se detiene con un mensaje de error.

En el ejemplo proporcionado, se lee el contenido del archivo `hello.txt` y se imprime en la consola. La característica `drop` se utiliza para asegurarse de que el archivo se cierre cuando el objeto `file` sale del ámbito.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
