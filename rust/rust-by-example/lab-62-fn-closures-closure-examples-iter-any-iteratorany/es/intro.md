# Introducción

En este laboratorio, se discute la función `Iterator::any`, que es una función que toma un iterador como entrada y devuelve `true` si algún elemento del iterador satisface una predicado dado, y `false` en caso contrario. La función está definida como un método de trato en la biblioteca estándar de Rust y se puede utilizar en cualquier tipo que implemente el trato `Iterator`. La función toma una clausura como argumento, que determina el predicado que se aplicará a cada elemento del iterador. La clausura está definida con el trato `FnMut`, lo que significa que puede modificar las variables capturadas pero no consumirlas. La función `any` devuelve un valor booleano que indica si el predicado es satisfecho por algún elemento del iterador.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
