# Introducción

En este laboratorio, aprendemos sobre el enum `Option` de la librería `std` de Rust, que se utiliza para manejar casos en los que la ausencia es una posibilidad. Proporciona dos opciones: `Some(T)` cuando se encuentra un elemento de tipo `T`, y `None` cuando no se encuentra ningún elemento. Estos casos se pueden manejar explícitamente utilizando `match` o implícitamente utilizando `unwrap`. El manejo explícito permite un mayor control y una salida significativa, mientras que `unwrap` puede devolver el elemento interno o causar un panic.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
