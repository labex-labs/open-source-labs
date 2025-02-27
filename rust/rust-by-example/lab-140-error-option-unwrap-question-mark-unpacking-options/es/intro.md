# Introducción

En este laboratorio, exploramos el uso del operador `?` en Rust, que permite la fácil extracción de valores de `Option` sin la necesidad de declaraciones `match` anidadas. El operador `?` se puede utilizar para devolver rápidamente el valor subyacente si la `Option` es `Some`, o terminar la función y devolver `None` si la `Option` es `None`. Este operador se puede encadenar para hacer el código más legible y conciso.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
