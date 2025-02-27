# Introducción

En este laboratorio, aprendemos que las closures pueden usarse como parámetros de entrada y también pueden devolverse como parámetros de salida al utilizar `impl Trait` y especificar los traits válidos (`Fn`, `FnMut`, `FnOnce`). La palabra clave `move` se utiliza para indicar que todas las capturas se realizan por valor, evitando referencias inválidas.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
