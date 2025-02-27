# Introducción

En este laboratorio, estamos implementando `fmt::Display` para una estructura llamada `List` que contiene un `Vec` en Rust. El desafío es manejar cada elemento secuencialmente utilizando la macro `write!`, ya que genera un `fmt::Result` que debe ser manejado adecuadamente. Para abordar esto, podemos utilizar el operador `?` para comprobar si `write!` devuelve un error y devolverlo si es así, de lo contrario continuar con la ejecución. Al implementar `fmt::Display` para `List`, podemos iterar sobre los elementos del vector y mostrarlos dentro de corchetes, separados por comas. La tarea es modificar el programa para que también muestre el índice de cada elemento del vector. La salida esperada después de la modificación es `[0: 1, 1: 2, 2: 3]`.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
