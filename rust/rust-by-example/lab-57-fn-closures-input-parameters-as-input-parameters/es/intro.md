# Introducción

En este laboratorio, aprendemos que al escribir funciones en Rust que toman una clausura como parámetro de entrada, el tipo completo de la clausura debe ser anotado utilizando uno de los `trait`: `Fn`, `FnMut` o `FnOnce`, que determinan cómo la clausura utiliza el valor capturado, ya sea por referencia, referencia mutable o valor. El compilador captura las variables de la manera menos restrictiva posible basada en el `trait` elegido para la clausura.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
