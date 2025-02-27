# Introducción

En este laboratorio, tenemos una implementación de una lista enlazada utilizando `enum` en Rust. El `enum List` tiene dos variantes: `Cons`, que representa un nodo con un elemento y un puntero al siguiente nodo, y `Nil`, que significa el final de la lista enlazada. El `enum` tiene métodos como `new` para crear una lista vacía, `prepend` para agregar un elemento al principio de la lista, `len` para devolver la longitud de la lista y `stringify` para devolver una representación en cadena de la lista. La función principal proporcionada demuestra el uso de estos métodos para crear y manipular una lista enlazada.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
